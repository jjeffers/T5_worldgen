'''Trade codes unit test module'''

import unittest
from T5_worldgen.planet import Planet
import T5_worldgen.upp as uwp
from T5_worldgen.trade_codes import TradeCodes


def gen_trade_codes(planet):
    '''Generate planet'''
    codes = TradeCodes(planet)
    trade_codes = codes.generate()
    print planet.uwp(), trade_codes
    return trade_codes


class TestPlanetaryTradeCodes(unittest.TestCase):
    '''Trade codes: planetary unit tests - test for match'''
    def test_as(self):
        '''Test As'''
        planet = Planet()
        planet.size = uwp.Size(0)
        planet.atmosphere = uwp.Atmosphere(0)
        planet.hydrographics = uwp.Hydrographics(0)
        self.assertTrue('As' in gen_trade_codes(planet))

    def test_de(self):
        '''Test De'''
        hyd = 0
        for atm in '23456789':
            planet = Planet()
            planet.atmosphere = uwp.Atmosphere(atm)
            planet.hydrographics = uwp.Hydrographics(hyd)
            self.assertTrue('De' in gen_trade_codes(planet))

    def test_fl(self):
        '''Test Fl'''
        for atm in 'ABC':
            for hyd in '123456789A':
                planet = Planet()
                planet.atmosphere = uwp.Atmosphere(atm)
                planet.hydrographics = uwp.Hydrographics(hyd)
                self.assertTrue('Fl' in gen_trade_codes(planet))

    def test_ga(self):
        '''Test Ga'''
        for siz in '678':
            for atm in '568':
                for hyd in '567':
                    planet = Planet()
                    planet.size = uwp.Size(siz)
                    planet.atmosphere = uwp.Atmosphere(atm)
                    planet.hydrographics = uwp.Hydrographics(hyd)
                    self.assertTrue('Ga' in gen_trade_codes(planet))

    def test_he(self):
        '''Test He'''
        for siz in '3456789ABC':
            for atm in '2479ABC':
                for hyd in '012':
                    planet = Planet()
                    planet.size = uwp.Size(siz)
                    planet.atmosphere = uwp.Atmosphere(atm)
                    planet.hydrographics = uwp.Hydrographics(hyd)
                    self.assertTrue('He' in gen_trade_codes(planet))

    def test_ic(self):
        '''Test Ic'''
        for atm in '01':
            for hyd in '123456789A':
                planet = Planet()
                planet.atmosphere = uwp.Atmosphere(atm)
                planet.hydrographics = uwp.Hydrographics(hyd)
                self.assertTrue('Ic' in gen_trade_codes(planet))

    def test_oc(self):
        '''Test Oc'''
        for siz in 'ABCDEF':
            for atm in '3456789ABC':
                hyd = 'A'
                planet = Planet()
                planet.size = uwp.Size(siz)
                planet.atmosphere = uwp.Atmosphere(atm)
                planet.hydrographics = uwp.Hydrographics(hyd)
                self.assertTrue('Oc' in gen_trade_codes(planet))

    def test_va(self):
        '''Test Va'''
        atm = 0
        planet = Planet()
        planet.atmosphere = uwp.Atmosphere(atm)
        self.assertTrue('Va' in gen_trade_codes(planet))

    def test_wa(self):
        '''Test Wa'''
        for siz in '3456789A':
            for atm in '3456789ABC':
                hyd = 'A'
                planet = Planet()
                planet.size = uwp.Size(siz)
                planet.atmosphere = uwp.Atmosphere(atm)
                planet.hydrographics = uwp.Hydrographics(hyd)
                self.assertTrue('Wa' in gen_trade_codes(planet))


class TestPlanetaryTradeCodesExclude(unittest.TestCase):
    '''Planetary trade codes unit tests - test no match'''
    def test_not_as(self):
        '''Test !As'''
        for siz in '123456789A':
            for atm in '123456789ABC':
                for hyd in '123456789A':
                    planet = Planet()
                    planet.size = uwp.Size(siz)
                    planet.atmosphere = uwp.Atmosphere(atm)
                    planet.hydrographics = uwp.Hydrographics(hyd)
                    self.assertFalse('As' in gen_trade_codes(planet))

    def test_not_de(self):
        '''Test !De'''
        for atm in '0123456789':
            for hyd in '123456789A':
                planet = Planet()
                planet.atmosphere = uwp.Atmosphere(atm)
                planet.hydrographics = uwp.Hydrographics(hyd)
                self.assertFalse('De' in gen_trade_codes(planet))

    def test_not_fl(self):
        '''Test !Fl'''
        for atm in '0123456789':
            hyd = 0
            planet = Planet()
            planet.atmosphere = uwp.Atmosphere(atm)
            planet.hydrographics = uwp.Hydrographics(hyd)
            self.assertFalse('Fl' in gen_trade_codes(planet))

    def test_not_ga(self):
        '''Test !Ga'''
        for siz in '0123459ABC':
            for atm in '0123459ABC':
                for hyd in '0123489A':
                    planet = Planet()
                    planet.size = uwp.Size(siz)
                    planet.atmosphere = uwp.Atmosphere(atm)
                    planet.hydrographics = uwp.Hydrographics(hyd)
                    self.assertFalse('Ga' in gen_trade_codes(planet))

    def test_not_he(self):
        '''Test !He'''
        for siz in '01':
            for atm in '013568':
                for hyd in '3456789A':
                    planet = Planet()
                    planet.size = uwp.Size(siz)
                    planet.atmosphere = uwp.Atmosphere(atm)
                    planet.hydrographics = uwp.Hydrographics(hyd)
                    self.assertFalse('He' in gen_trade_codes(planet))

    def test_not_ic(self):
        '''Test !Ic'''
        for atm in '23456789ABC':
            hyd = 0
            planet = Planet()
            planet.atmosphere = uwp.Atmosphere(atm)
            planet.hydrographics = uwp.Hydrographics(hyd)
            self.assertFalse('Ic' in gen_trade_codes(planet))

    def test_not_oc(self):
        '''Test !Oc'''
        for siz in '0123456789':
            for atm in '012':
                hyd = '0123456789'
                planet = Planet()
                planet.size = uwp.Size(siz)
                planet.atmosphere = uwp.Atmosphere(atm)
                planet.hydrographics = uwp.Hydrographics(hyd)
                self.assertFalse('Oc' in gen_trade_codes(planet))

    def test_not_va(self):
        '''Test !Va'''
        for atm in '123456789ABC':
            for hyd in '123456789A':
                planet = Planet()
                planet.atmosphere = uwp.Atmosphere(atm)
                planet.hydrographics = uwp.Hydrographics(hyd)
                self.assertFalse('Va' in gen_trade_codes(planet))

    def test_not_wa(self):
        '''Test !Wa'''
        for siz in '012BC':
            for atm in '012':
                for hyd in '0123456789':
                    planet = Planet()
                    planet.size = uwp.Size(siz)
                    planet.atmosphere = uwp.Atmosphere(atm)
                    planet.hydrographics = uwp.Hydrographics(hyd)
                    self.assertFalse('Wa' in gen_trade_codes(planet))


class TestPopulationTradeCodes(unittest.TestCase):
    '''Trade codes: test population trade codes'''
    def test_di(self):
        '''Test Di'''
        pop = 0
        gov = 0
        law = 0
        planet = Planet()
        planet.population = uwp.Population(pop)
        planet.government = uwp.Government(gov)
        planet.law_level = uwp.LawLevel(law)
        self.assertTrue('Di' in gen_trade_codes(planet))

    def test_ba(self):
        '''Test Ba'''
        pop = 0
        gov = 0
        law = 0
        for starport in 'EX':
            planet = Planet()
            planet.starport = starport
            planet.population = uwp.Population(pop)
            planet.government = uwp.Government(gov)
            planet.law_level = uwp.LawLevel(law)
            self.assertTrue('Ba' in gen_trade_codes(planet))

    def test_lo(self):
        '''Test Lo'''
        for pop in '123':
            planet = Planet()
            planet.population = uwp.Population(pop)
            self.assertTrue('Lo' in gen_trade_codes(planet))

    def test_ni(self):
        '''Test Ni'''
        for pop in '456':
            planet = Planet()
            planet.population = uwp.Population(pop)
            self.assertTrue('Ni' in gen_trade_codes(planet))

    def test_ph(self):
        '''Test Ph'''
        pop = 8
        planet = Planet()
        planet.population = uwp.Population(pop)
        self.assertTrue('Ph' in gen_trade_codes(planet))

    def test_hi(self):
        '''Test Hi'''
        for pop in '9ABCDEF':
            planet = Planet()
            planet.population = uwp.Population(pop)
            self.assertTrue('Hi' in gen_trade_codes(planet))


class TestPopulationTradeCodesExclude(unittest.TestCase):
    '''Trade codes: population trade codes - test no match'''
    def test_not_di(self):
        '''Test !Di'''
        for pop in '123456789ABCDEF':
            for gov in '123456789ABCDEF':
                for law in '123456789ABCDEFGHJ':
                    planet = Planet()
                    planet.population = uwp.Population(pop)
                    planet.government = uwp.Government(gov)
                    planet.law_level = uwp.LawLevel(law)
                    self.assertFalse('Di' in gen_trade_codes(planet))

    def test_not_ba(self):
        '''Test !Ba'''
        for pop in '123456789A':
            for gov in '123456789AB':
                for law in '123456789A':    # Assume the rest are OK
                    for tech in '123456':   # Assume the rest are OK
                        for starport in 'ABCD':
                            planet = Planet()
                            planet.starport = starport
                            planet.population = uwp.Population(pop)
                            planet.government = uwp.Government(gov)
                            planet.law_level = uwp.LawLevel(law)
                            planet.tech_level = uwp.TechLevel(tech)
                            self.assertFalse('Ba' in gen_trade_codes(planet))

    def test_not_lo(self):
        '''Test !Lo'''
        for pop in '0456789ABCDEF':
            planet = Planet()
            planet.population = uwp.Population(pop)
            self.assertFalse('Lo' in gen_trade_codes(planet))

    def test_not_ni(self):
        '''Test !Ni'''
        for pop in '0123789ABC':
            planet = Planet()
            planet.population = uwp.Population(pop)
            self.assertFalse('Ni' in gen_trade_codes(planet))

    def test_not_ph(self):
        '''Test !Ph'''
        for pop in '012345679ABCDEF':
            planet = Planet()
            planet.population = uwp.Population(pop)
            self.assertFalse('Ph' in gen_trade_codes(planet))

    def test_not_hi(self):
        '''Test !Hi'''
        for pop in '012345678':
            planet = Planet()
            planet.population = uwp.Population(pop)
            self.assertFalse('Hi' in gen_trade_codes(planet))


class TestEconomicTradeCodes(unittest.TestCase):
    '''Trade codes: test economic trade codes'''
    def test_pa(self):
        '''Test Pa'''
        for atm in '456789':
            for hyd in '45678':
                for pop in '48':
                    planet = Planet()
                    planet.atmosphere = uwp.Atmosphere(atm)
                    planet.hydrographics = uwp.Hydrographics(hyd)
                    planet.population = uwp.Population(pop)
                    self.assertTrue('Pa' in gen_trade_codes(planet))

    def test_ag(self):
        '''Test Ag'''
        for atm in '456789':
            for hyd in '45678':
                for pop in '567':
                    planet = Planet()
                    planet.atmosphere = uwp.Atmosphere(atm)
                    planet.hydrographics = uwp.Hydrographics(hyd)
                    planet.population = uwp.Population(pop)
                    self.assertTrue('Ag' in gen_trade_codes(planet))

    def test_na(self):
        '''Test Na'''
        for atm in '0123':
            for hyd in '0123':
                for pop in '6789ABCDEF':
                    planet = Planet()
                    planet.atmosphere = uwp.Atmosphere(atm)
                    planet.hydrographics = uwp.Hydrographics(hyd)
                    planet.population = uwp.Population(pop)
                    self.assertTrue('Na' in gen_trade_codes(planet))

    def test_px(self):
        '''Test Px'''
        for atm in '23AB':
            for hyd in '12345':
                for pop in '3456':
                    for law in '6789':
                        # Also need to check MW
                        planet = Planet()
                        planet.atmosphere = uwp.Atmosphere(atm)
                        planet.hydrographics = uwp.Hydrographics(hyd)
                        planet.population = uwp.Population(pop)
                        planet.law_level = uwp.LawLevel(law)
                        self.assertTrue('Px' in gen_trade_codes(planet))

    def test_pi(self):
        '''Test Pu'''
        for atm in '012479':
            for pop in '78':
                planet = Planet()
                planet.atmosphere = uwp.Atmosphere(atm)
                planet.population = uwp.Population(pop)
                self.assertTrue('Pi' in gen_trade_codes(planet))

    def test_in(self):
        '''Test In'''
        for atm in '012479':
            for pop in '9A':
                planet = Planet()
                planet.atmosphere = uwp.Atmosphere(atm)
                planet.population = uwp.Population(pop)
                self.assertTrue('In' in gen_trade_codes(planet))

    def test_po(self):
        '''Test Po'''
        for atm in '2345':
            for hyd in '0123':
                planet = Planet()
                planet.atmosphere = uwp.Atmosphere(atm)
                planet.hydrographics = uwp.Hydrographics(hyd)
                self.assertTrue('Po' in gen_trade_codes(planet))

    def test_ri(self):
        '''Test Ri'''
        for atm in '68':
            for pop in '678':
                for gov in '456789':
                    planet = Planet()
                    planet.atmosphere = uwp.Atmosphere(atm)
                    planet.population = uwp.Population(pop)
                    planet.government = uwp.Government(gov)
                    self.assertTrue('Ri' in gen_trade_codes(planet))


class TestEconomicTradeCodesExclude(unittest.TestCase):
    '''Trade codes: economic trade codes - ttest no match'''
    def test_no_pa(self):
        '''Test !Pa'''
        for atm in '0123ABC':
            for hyd in '01239A':
                for pop in '01235679ABCDEF':
                    planet = Planet()
                    planet.atmosphere = uwp.Atmosphere(atm)
                    planet.hydrographics = uwp.Hydrographics(hyd)
                    planet.population = uwp.Population(pop)
                    self.assertFalse('Pa' in gen_trade_codes(planet))

    def test_no_ag(self):
        '''Test !Ag'''
        for atm in '0123ABC':
            for hyd in '01239A':
                for pop in '012389ABCDEF':
                    planet = Planet()
                    planet.atmosphere = uwp.Atmosphere(atm)
                    planet.hydrographics = uwp.Hydrographics(hyd)
                    planet.population = uwp.Population(pop)
                    self.assertFalse('Ag' in gen_trade_codes(planet))

    def test_no_na(self):
        '''Test !Na'''
        for atm in '456789ABC':
            for hyd in '456789A':
                for pop in '012345':
                    planet = Planet()
                    planet.atmosphere = uwp.Atmosphere(atm)
                    planet.hydrographics = uwp.Hydrographics(hyd)
                    planet.population = uwp.Population(pop)
                    self.assertFalse('Na' in gen_trade_codes(planet))

    def test_no_px(self):
        '''Test !Px'''
        for atm in '01456789C':
            for hyd in '6789A':
                for pop in '012789ABCDEF':
                    for law in '012345ABCDEF':
                        # Also need to check MW
                        planet = Planet()
                        planet.atmosphere = uwp.Atmosphere(atm)
                        planet.hydrographics = uwp.Hydrographics(hyd)
                        planet.population = uwp.Population(pop)
                        planet.law_level = uwp.LawLevel(law)
                        self.assertFalse('Px' in gen_trade_codes(planet))

    def test_no_pi(self):
        '''Test !Pi'''
        for atm in '3568ABC':
            for pop in '01234569ABC':
                planet = Planet()
                planet.atmosphere = uwp.Atmosphere(atm)
                planet.population = uwp.Population(pop)
                self.assertFalse('Pi' in gen_trade_codes(planet))

    def test_in(self):
        '''Test In'''
        for atm in '3568ABC':
            for pop in '012345678':
                planet = Planet()
                planet.atmosphere = uwp.Atmosphere(atm)
                planet.population = uwp.Population(pop)
                self.assertFalse('In' in gen_trade_codes(planet))

    def test_po(self):
        '''Test Po'''
        for atm in '016789ABC':
            for hyd in '456789A':
                planet = Planet()
                planet.atmosphere = uwp.Atmosphere(atm)
                planet.hydrographics = uwp.Hydrographics(hyd)
                self.assertFalse('Po' in gen_trade_codes(planet))

    def test_ri(self):
        '''Test Ri'''
        for atm in '01234579ABC':
            for pop in '0123459ABCDEF':
                for gov in '012ABCDEF':
                    planet = Planet()
                    planet.atmosphere = uwp.Atmosphere(atm)
                    planet.population = uwp.Population(pop)
                    planet.government = uwp.Government(gov)
                    self.assertFalse('Ri' in gen_trade_codes(planet))
