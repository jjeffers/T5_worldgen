'''UPP unit test module'''

import unittest

import T5_worldgen.upp as upp


class TestUpp(unittest.TestCase):
    '''UPP unit test class'''
    def test_upp_str1(self):
        '''UPP: Test _set str (1)'''
        siz = upp.Size()
        siz._set('A')
        self.assertEqual(str(siz), 'A')
        self.assertEqual(int(siz), 10)

    def test_upp_str2(self):
        '''UPP: Test _set str (2)'''
        siz = upp.Size()
        siz._set('3')
        self.assertEqual(str(siz), '3')
        self.assertEqual(int(siz), 3)

    def test_upp_int(self):
        '''UPP: Test _set int'''
        siz = upp.Size()
        siz._set(3)
        self.assertEqual(str(siz), '3')
        self.assertEqual(int(siz), 3)

    def test_upp_outside_limits(self):
        '''UPP: Test _set outside limits'''
        pop = upp.Population()
        with self.assertRaises(ValueError):
            pop._set('Z')

    def test_upp_set_on_instantiate_int(self):
        '''UPP: Test set on instantiate (int)'''
        siz = upp.Size(3)
        self.assertEqual(str(siz), '3')
        self.assertEqual(int(siz), 3)

    def test_upp_set_on_instantiate_str(self):
        '''UPP: Test set on instantiate (str)'''
        siz = upp.Size('A')
        self.assertEqual(str(siz), 'A')
        self.assertEqual(int(siz), 10)


class TestUppSubclasses(unittest.TestCase):
    '''UPP subclass unit test class'''
    _ = upp.Size()
    _ = upp.Atmosphere()
    _ = upp.Hydrographics()
    _ = upp.Population()
    _ = upp.Government()
    _ = upp.LawLevel()
    _ = upp.TechLevel()


class TestUppBiosphere(unittest.TestCase):
    '''UPP biosphere unit test class'''
    def test_biosphere(self):
        '''UPP:biosphere: Test default chemistry lookup'''
        bio = upp.Biosphere()
        row = bio.generate_chemistry(
            [(1, 4), (5, 6), (7, 8)],
            5
        )
        self.assertEquals(row, ('Ammonia', 1))

    def test_biosphere_chem_table(self):
        '''UPP:biosphere: Test custom chemistry lookup'''
        bio = upp.Biosphere()
        bio.chemistry_values = [('Water', 0), ('Sulfur', 0), ('Chlorine', 0)]
        row = bio.generate_chemistry(
            [(2, 8), (9, 11), 12],
            11
        )
        self.assertEquals(row, ('Sulfur', 0))
