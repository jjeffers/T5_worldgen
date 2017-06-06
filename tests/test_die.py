'''Die unit test module'''

import unittest

from T5_worldgen.util import Die, Flux

NUM_TESTS = 1000


class TestDie(unittest.TestCase):
    '''Die unit test class'''
    def test_roll(self):
        '''Die: Test roll results'''
        rolls = []
        die6 = Die(6)
        for _ in range(0, NUM_TESTS):
            rolls.append(die6.roll(1))
        print rolls
        for roll in rolls:
            self.assertTrue(roll in range(1, 7))

    def test_roll_floor(self):
        '''Die: Test roll floor()'''
        rolls = []
        die6 = Die(6)
        for _ in range(0, NUM_TESTS):
            rolls.append(die6.roll(1, floor=3))
        for roll in rolls:
            self.assertTrue(roll in range(3, 7))

    def test_roll_ceiling(self):
        '''Die: Test roll ceiling()'''
        rolls = []
        die6 = Die(6)
        for _ in range(0, NUM_TESTS):
            rolls.append(die6.roll(1, ceiling=4))
        for roll in rolls:
            self.assertTrue(roll in range(1, 5))

    def test_roll_dm(self):
        '''Die: Test roll DM'''
        rolls = []
        die6 = Die(6)
        for _ in range(0, NUM_TESTS):
            rolls.append(die6.roll(1, -2))     # dm = -2
        for roll in rolls:
            self.assertTrue(roll in range(-1, 5))


class TestFlux(unittest.TestCase):
    '''Flux unit test class'''
    def test_flux(self):
        '''Flux: Test flux() results'''
        flx = Flux()
        for _ in range(0, NUM_TESTS):
            roll = flx.flux()
            print roll
            self.assertTrue(roll in range(-5, 6))

    def test_good_flux(self):
        '''Flux: test good() results'''
        flx = Flux()
        for _ in range(0, NUM_TESTS):
            roll = flx.good()
            print roll
            self.assertTrue(roll in range(0, 6))

    def test_bad_flux(self):
        '''Flux: test bad() results'''
        flx = Flux()
        for _ in range(0, NUM_TESTS):
            roll = flx.bad()
            print roll
            self.assertTrue(roll in range(-5, 1))
