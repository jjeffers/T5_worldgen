'''T5_worldgen system module'''

import logging
import json
from T5_worldgen.util import Die, Flux, Table
from T5_worldgen.trade_codes import TradeCodes
from T5_worldgen.planet import Planet
from T5_worldgen.star import Primary

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

D3 = Die(3)
D6 = Die(6)
D10 = Die(10)
FLUX = Flux()


class System(object):
    '''Return a T5 basic system with the specified name and location hex'''

    naval_base_presence = Table()
    naval_base_presence.add_row('A', 6)
    naval_base_presence.add_row('B', 5)

    scout_base_presence = Table()
    scout_base_presence.add_row('A', 4)
    scout_base_presence.add_row('B', 5)
    scout_base_presence.add_row('C', 6)
    scout_base_presence.add_row('D', 7)

    mw_orbit_flux_table = Table()
    mw_orbit_flux_table.add_row(-6, -2)
    mw_orbit_flux_table.add_row((-5, -3), -1)
    mw_orbit_flux_table.add_row((-2, 2), 0)
    mw_orbit_flux_table.add_row((3, 5), 1)
    mw_orbit_flux_table.add_row(6, 2)

    def __init__(self, name='', location_hex='0000'):
        self.hex = location_hex
        self.name = name
        self.stellar = Primary()
        self.mainworld = Planet()
        self.determine_mw_orbit()

        self.bases = self.determine_bases()
        self.pbg = Pbg(self.mainworld)
        self.allegiance = 'Na'
        self.importance_x = ImportanceExtension(
            self.mainworld,
            self)
        self.economic_x = EconomicExtension(
            self.pbg,
            int(self.mainworld.population),
            int(self.mainworld.tech_level),
            self.mainworld.trade_codes,
            int(self.importance_x))
        self.cultural_x = CulturalExtension(
            int(self.mainworld.population),
            int(self.importance_x),
            int(self.mainworld.tech_level))
        self.nobility = self.determine_nobility()
        self.num_worlds = (
            self.pbg.belts +
            self.pbg.gasgiants +
            D6.roll(1) + 1)
        self.determine_trade_codes()
        self.zone = ''

    def display(self):
        '''Display'''
        return '{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
            self.hex,
            self.name,
            self.mainworld.uwp(),
            ' '.join(self.mainworld.trade_codes),
            str(self.importance_x),
            str(self.economic_x),
            str(self.cultural_x),
            self.nobility,
            self.bases,
            self.zone,
            str(self.pbg),
            self.num_worlds,
            self.allegiance,
            self.stellar.display()
        )

    def __str__(self):
        oformat = '{:4} {:20} {:9} {:18} {:4} {:7} {:6} ' +\
            '{:7} {:2} {:1} {:3} {:2} {:2} {:14}'
        return oformat.format(
            self.hex,
            self.name,
            self.mainworld.uwp(),
            ' '.join(self.mainworld.trade_codes),
            str(self.importance_x),
            str(self.economic_x),
            str(self.cultural_x.display()),
            self.nobility,
            self.bases,
            self.zone,
            str(self.pbg),
            self.num_worlds,
            self.allegiance,
            self.stellar)

    def determine_nobility(self):
        '''Determine noble representation'''
        nobility = 'B'  # Every world gets a knight
        # Baronet
        if (
                'Pa' in self.mainworld.trade_codes or
                'Pr' in self.mainworld.trade_codes):
            nobility += 'c'
        # Baron
        if (
                'Ag' in self.mainworld.trade_codes or
                'Ri' in self.mainworld.trade_codes):
            nobility += 'C'
        if 'Pi' in self.mainworld.trade_codes:
            nobility += 'D'     # Marquis
        if 'Ph' in self.mainworld.trade_codes:
            nobility += 'e'     # Viscount
        # Count
        if (
                'In' in self.mainworld.trade_codes or
                'Hi' in self.mainworld.trade_codes):
            nobility += 'E'
        if int(self.importance_x) >= 4:
            nobility += 'f'     # Duke
        return nobility

    def determine_bases(self):
        '''Determine bases'''
        bases = ''
        # Naval base
        target = self.naval_base_presence.lookup(self.mainworld.starport)
        if target is not None:
            if D6.roll(1) <= target:
                bases += 'N'
        # Scout base
        target = self.scout_base_presence.lookup(self.mainworld.starport)
        if target is not None:
            if D6.roll(1) <= target:
                bases += 'S'
        return bases

    def determine_trade_codes(self):
        '''Determine climate trade codes'''
        tcs = TradeCodes(self.mainworld, self)
        self.mainworld.trade_codes = tcs.generate()

    def determine_mw_orbit(self):
        '''Determine mainworld orbit'''
        orbit = self.stellar.habitable_zone +\
            self.mw_orbit_flux_table.lookup(FLUX.flux())
        orbit = max(orbit, 0)
        self.mainworld.orbit = orbit

    def as_json(self):
        '''Return JSON representation of system'''
        system_dict = {
            'name': self.name,
            'hex': self.hex,
            'stellar': self.stellar.as_json(),
            'mainworld': self.mainworld.as_json(),
            'bases': self.bases,
            'pbg': str(self.pbg),
            'allegiance': self.allegiance,
            'Ix': str(self.importance_x),
            'Ex': str(self.economic_x),
            'Cx': str(self.cultural_x),
            'nobility': self.nobility,
            'worlds': self.num_worlds,
            'zone': self.zone
        }
        return json.dumps(system_dict)


class Pbg(object):
    '''PBG storage'''
    def __init__(self, population=0):
        self.pop = self._determine_pop_digit(population)
        self.belts = self._determine_belts()
        self.gasgiants = self._determine_gas_giants()

    def __str__(self):
        return '{}{}{}'.format(
            self.pop,
            self.belts,
            self.gasgiants)

    @staticmethod
    def _determine_pop_digit(population):
        '''Determine population digit'''
        if population == 0:
            return 0
        else:
            return D10.roll(1, -1)

    @staticmethod
    def _determine_belts():
        '''Determine number of belts'''
        return D3.roll(1, -3, floor=0)

    @staticmethod
    def _determine_gas_giants():
        '''Determne number of gas giants'''
        return max(int(D6.roll(2) / 2) - 2, 0)


class ImportanceExtension(object):
    '''Importance extension'''
    def __init__(self, planet, system):
        self.value = 0
        # Starport
        if planet.starport in 'AB':
            self.value += 1
        elif planet.starport in 'DEX':
            self.value -= 1
        # Tech level
        if int(planet.tech_level) >= 16:
            self.value += 1
        if int(planet.tech_level) >= 10:
            self.value += 1
        if int(planet.tech_level) <= 8:
            self.value -= 1
        # Trade codes, population
        if int(planet.population) <= 6:
            self.value -= 1
        for code in ['Ag', 'Hi', 'In', 'Ri']:
            if code in planet.trade_codes:
                self.value += 1
        # Bases
        if 'N' in system.bases and 'S' in system.bases:
            self.value += 1
        if 'W' in system.bases:
            self.value += 1

    def display(self):
        '''Display Ix'''
        return '{' + '{:+X}'.format(self.value) + '}'

    def __str__(self):
        return self.display()

    def __int__(self):
        return self.value


class EconomicExtension(object):
    '''Economic extension data'''
    def __init__(
            self,
            pbg,
            population=0,
            tech_level=0,
            trade_codes=[],
            importance_x=0
    ):
        self.resources = self._calculate_resources(
            tech_level, pbg)
        self.labor = max(population - 1, 0)
        self.infrastructure = self._calculate_infrastructure(
            importance_x, trade_codes)
        self.efficiency = FLUX.flux()

    @staticmethod
    def _calculate_resources(tech_level, pbg):
        '''Resources stuff'''
        resources = D6.roll(2)
        if tech_level >= 8:
            resources += pbg.gasgiants
            resources += pbg.belts
        resources = max(resources, 0)
        return resources

    @staticmethod
    def _calculate_infrastructure(importance_x, trade_codes):
        '''Determine infrastructure rating'''
        infrastructure = D6.roll(2, importance_x)
        if (
                'Ba' in trade_codes or
                'Di' in trade_codes
        ):
            infrastructure = 0
        if 'Lo' in trade_codes:
            infrastructure = 1
        if 'Ni' in trade_codes:
            infrastructure = D6.roll(1, importance_x)
        infrastructure = max(infrastructure, 0)
        return infrastructure

    def display(self):
        '''Display Ex'''
        return '({:X}{:X}{:X}{:+X})'.format(
            self.resources,
            self.labor,
            self.infrastructure,
            self.efficiency
        )

    def __str__(self):
        '''str() representation'''
        return self.display()


class CulturalExtension(object):
    '''Cultural extension data'''
    def __init__(self, population=0, importance_x=0, tech_level=0):
        # Reverse-engineer Traveller map checks
        if population == 0:
            self.homogeneity = 0
            self.acceptance = 0
            self.strangeness = 0
            self.symbols = 0
        else:
            self.homogeneity = population + FLUX.flux()
            self.acceptance = population + importance_x
            self.strangeness = FLUX.flux() + 5
            self.symbols = FLUX.flux() + tech_level
            self.homogeneity = max(self.homogeneity, 1)
            self.acceptance = max(self.acceptance, 1)
            self.strangeness = max(self.strangeness, 1)
            self.symbols = max(self.symbols, 1)

    def display(self):
        '''Display Cx'''
        return '[{:X}{:X}{:X}{:X}]'.format(
            self.homogeneity,
            self.acceptance,
            self.strangeness,
            self.symbols
        )

    def __str__(self):
        '''str() representation'''
        return self.display()
