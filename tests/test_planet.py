'''test_planet.py'''

import unittest

from T5_worldgen.planet import Planet
from T5_worldgen import upp


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
                                print 'port: {} siz: {} atm: {} hyd: {} pop: {} gov: {}'.format(
                                    starport_dm, siz_dm, atm_dm, hyd_dm, pop_dm, gov_dm)
                                tl_dm = starport_dm + siz_dm + atm_dm + hyd_dm
                                tl_dm = tl_dm + pop_dm + gov_dm
                                tech_level = int(planet.tech_level)
                                print 'upp: {} TL: {} TL DM: {}'.format(
                                    str(planet), tech_level, tl_dm)
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
