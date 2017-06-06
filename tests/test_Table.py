'''Table unit tests'''

import unittest
from T5_worldgen.util import Table


class TestTable(unittest.TestCase):
    '''Table unit test class'''
    def test_add_row(self):
        '''Table: Test add_row()'''
        tbl = Table()
        tbl.add_row(1, 'Entry 1')          # Should just work
        tbl.add_row((2, 3), 'Entry 2')     # Should ust work
        tbl.add_row('A', 'Entry 3')
        with self.assertRaises(ValueError):
            tbl.add_row(dict(), 'Bogus entry')     # ValueError

    def test_lookup(self):
        '''Table: Test lookup()'''
        tbl = Table()
        tbl.add_row(1, 'Entry 1')
        self.assertEquals(tbl.lookup(1), 'Entry 1')

    def test_roll(self):
        '''Table: Test roll()'''
        tbl = Table()
        tbl.add_row((1, 6), 'Entry 1')
        tbl.dice = 1
        self.assertEquals(tbl.roll(), 'Entry 1')

    def test_table_in_table(self):
        '''Table: Test subtable'''
        tbl2 = Table()
        tbl2.add_row(1, 'Subentry 1')
        tbl2.dice = 1

        tbl1 = Table()
        tbl1.add_row(1, 'Entry 1')
        tbl1.add_row(2, tbl2.roll)
        self.assertEquals(tbl1.lookup(2), 'Subentry 1')
