'''test_planet.py'''
from __future__ import print_function

import unittest
import json

from T5_worldgen.planet import Planet
from T5_worldgen import upp

SAMPLE_SIZE = 1000


class TestPlanet(unittest.TestCase):
    '''Planet unit tests'''
    def test_tech_level(self):
        '''Test tech level results'''
        planet = Planet()
        for starport in 'ABCX':
            for siz in '01234':
                for atm in '0123ABCDEF':
                    for hyd in '9A':
                        for pop in '123459A':
                            for gov in '05D':
                                planet.starport = starport
                                planet.size = upp.Size(siz)
                                planet.atmosphere = upp.Atmosphere(atm)
                                planet.hydrographics = upp.Hydrographics(hyd)
                                planet.population = upp.Population(pop)
                                planet.government = upp.Government(gov)
                                planet.determine_tech()
                                starport_dm =\
                                    self._starport_dm(planet.starport)
                                siz_dm = self._size_dm(str(planet.size))
                                atm_dm = self._atm_dm(str(planet.atmosphere))
                                hyd_dm = self._hyd_dm(str(
                                    planet.hydrographics))
                                pop_dm = self._pop_dm(str(planet.population))
                                gov_dm = self._gov_dm(str(planet.government))
                                print('port: {} siz: {} atm: {} hyd: {} pop: {} gov: {}'.format(
                                    starport_dm, siz_dm, atm_dm, hyd_dm, pop_dm, gov_dm))
                                tl_dm = starport_dm + siz_dm + atm_dm + hyd_dm
                                tl_dm = tl_dm + pop_dm + gov_dm
                                tech_level = int(planet.tech_level)
                                print('upp: {} TL: {} TL DM: {}'.format(
                                    str(planet), tech_level, tl_dm))
                                self.assertTrue(
                                    tech_level - tl_dm in range(1, 7))

    @staticmethod
    def _starport_dm(starport):
        '''Return starport DM'''
        if starport == 'A':
            return 6
        elif starport == 'B':
            return 4
        elif starport == 'C':
            return 2
        elif starport == 'X':
            return -4
        else:
            return 0

    @staticmethod
    def _size_dm(size):
        '''Return size DM'''
        if size in '01':
            return 2
        elif size in '234':
            return 1
        else:
            return 0

    @staticmethod
    def _atm_dm(atm):
        '''Return atmosphere DM'''
        if atm in '0123ABCDEF':
            return 1
        else:
            return 0

    @staticmethod
    def _hyd_dm(hyd):
        '''Return hydrographics DM'''
        if hyd == '9':
            return 1
        elif hyd == 'A':
            return 2
        else:
            return 0

    @staticmethod
    def _pop_dm(pop):
        '''Return population DM'''
        if pop in '12345':
            return 1
        elif pop == '9':
            return 2
        elif pop in 'ABCDEF':
            return 4
        else:
            return 0

    @staticmethod
    def _gov_dm(gov):
        '''Return government DM'''
        if gov in '05':
            return 1
        elif gov == 'D':
            return -2
        else:
            return 0


class TestJson(unittest.TestCase):
    '''Test JSON importer, exporter'''
    def test_as_json(self):
        '''Test planet.as_json() exporter'''
        planet = Planet()
        jdata = planet.as_json()
        print(jdata)
        p_data = json.loads(jdata)
        self.assertTrue(p_data['uwp'] == planet.uwp())
        self.assertTrue(p_data['trade_codes'] == planet.trade_codes)
        self.assertTrue(p_data['travel_code'] == planet.travel_code)
        self.assertTrue(p_data['bases'] == planet.bases)
        self.assertTrue(p_data['orbit'] == planet.orbit)
        self.assertTrue(p_data['is_mainworld'] == planet.is_mainworld)

    def test_json_import(self):
        '''Test planet.json_import() importer'''
        jdata = u'{"trade_codes": ["Fl", "Lo"], "travel_code": "", ' +\
            '"is_mainworld": true, "uwp": "D9A6313-3", "orbit": 5, ' +\
            '"bases": "", "mainworld_type": "Planet", ' +\
            '"parent_type": null, "orbit_around_parent": null  }'
        p_data = json.loads(jdata)
        planet = Planet()
        planet.json_import(jdata)
        self.assertTrue(p_data['uwp'] == planet.uwp())
        self.assertTrue(p_data['trade_codes'] == planet.trade_codes)
        self.assertTrue(p_data['travel_code'] == planet.travel_code)
        self.assertTrue(p_data['bases'] == planet.bases)
        self.assertTrue(p_data['orbit'] == planet.orbit)
        self.assertTrue(p_data['is_mainworld'] == planet.is_mainworld)


class TestDistributions(unittest.TestCase):
    '''Test distribution of UWP data'''
    @staticmethod
    def generate_worlds():
        '''Generate many worlds'''
        planets = []
        for _ in range(0, SAMPLE_SIZE):
            planet = Planet()
            planets.append(planet)
        return planets

    def test_starport_distribution(self):
        '''Test starport type distribution'''
        starports = {
            'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'X':0
        }
        expected = {
            'A': 0.14, 'B': 0.25, 'C': 0.31,
            'D': 0.11, 'E': 0.14, 'X': 0.03
        }
        for code in expected.keys():
            expected[code] = expected[code] * SAMPLE_SIZE
        for planet in self.generate_worlds():
            starports[planet.starport] += 1
        for code in starports.keys():
            print(code, starports[code], expected[code])
            self.assertAlmostEqual(
                starports[code],
                expected[code],
                delta=0.05 * SAMPLE_SIZE
            )


