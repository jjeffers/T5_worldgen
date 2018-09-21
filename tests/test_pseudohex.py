'''Psuedohex unit test module'''

from __future__ import print_function
import unittest

from T5_worldgen.pseudohex import Pseudohex


class TestEqualOperator(unittest.TestCase):
    """Tests that equality operators return true when psuedohex values are the same"""

    def test_base_equality_int(self):
        """Base class check"""

        p = Pseudohex('A')

        assert(10 == (int(p)))

    def test_base_equality_str(self):
        """Base class check"""

        p = Pseudohex('A')

        assert ('A' == (str(p)))

    def test_base_equality(self):
        """Base class check"""

        p = Pseudohex('A')

        assert (Pseudohex('A') == p)

class TestNotEqualOperator(unittest.TestCase):
    """Tests that equality operators return true when psuedohex values are not the same"""

    def test_base_inequality_int(self):
        """Base class check"""

        p = Pseudohex('A')

        assert(11 != (int(p)))

    def test_base_inequality_str(self):
        """Base class check"""

        p = Pseudohex('A')

        assert ('4' != (str(p)))

    def test_base_inequality(self):
        """Base class check"""

        p = Pseudohex('A')

        assert (Pseudohex('C') != p)

class TestGreaterThanOperator(unittest.TestCase):
    """Tests that gt operators return true when psuedohex values are greater than the other"""

    def test_base_gt_int(self):
        """Base class check"""

        p = Pseudohex('A')

        assert(int(p) > 8)

    def test_base_gt_str(self):
        """Base class check"""

        p = Pseudohex('A')

        assert ((str(p)) > '1')

    def test_base_gt(self):
        """Base class check"""

        p = Pseudohex('A')

        assert (p > Pseudohex('5'))

class TestLessThanOperator(unittest.TestCase):
    """Tests that lt operators return true when psuedohex value are less than the other"""

    def test_base_gt_int(self):
        """Base class check"""

        p = Pseudohex('A')

        assert(int(p) < 12)

    def test_base_gt_str(self):
        """Base class check"""

        p = Pseudohex('A')

        assert ((str(p)) < 'B')

    def test_base_gt(self):
        """Base class check"""

        p = Pseudohex('A')

        assert (p < Pseudohex('B'))


class TestLessThanOrEqualOperator(unittest.TestCase):
    """Tests that le operators return true when psuedohex value are less than or equal to the other"""

    def test_base_le_int(self):
        """Base class check"""

        p = Pseudohex('A')

        assert (int(p) <= 12)
        assert (int(p) <= 10)

    def test_base_le_str(self):
        """Base class check"""

        p = Pseudohex('A')

        assert ((str(p)) <= 'B')
        assert ((str(p)) <= 'A')

    def test_base_le(self):
        """Base class check"""

        p = Pseudohex('A')

        assert (p <= Pseudohex('B'))
        assert (p <= Pseudohex('A'))


class TestGreaterThanOrEqualOperator(unittest.TestCase):
    """Tests that ge operators return true when psuedohex value are greater than or equal to the other"""

    def test_base_ge_int(self):
        """Base class check"""

        p = Pseudohex('A')

        assert (int(p) >= 10)
        assert (int(p) >= 9)

    def test_base_ge_str(self):
        """Base class check"""

        p = Pseudohex('A')

        assert ((str(p)) >= '9')
        assert ((str(p)) >= 'A')

    def test_base_ge(self):
        """Base class check"""

        p = Pseudohex('A')

        assert (p >= Pseudohex('5'))
        assert (p >= Pseudohex('A'))

class TestAddOperator(unittest.TestCase):
    """Tests that add operator works"""

    def test_base_add_int(self):
        """Base class check"""

        p = Pseudohex('A')

        assert (int(p+1) == 11)
        assert (int(p) == 10)

    def test_base_radd_int(self):
        """Base class check"""

        p = Pseudohex('A')

        assert (int(1 + p) == 11)

    def test_base_add_str(self):
        """Base class check"""

        p = Pseudohex('A')

        assert ((str(p+1)) == 'B')

    def test_base_radd_str(self):
        """Base class check"""

        p = Pseudohex('A')

        assert ((str(1 + p)) == 'B')

    def test_base_add_overflow(self):
        """Check that adding over the max valid value just returns the same max value"""

        p = Pseudohex('Z')
        assert(len(p.valid) == 34)
        assert ((str(p+1)) == Pseudohex('Z'))

    def test_base_add_other(self):
        """Base class check"""

        p = Pseudohex('A')

        assert (Pseudohex('B') == (p + Pseudohex('1')))


class TestSubtractOperator(unittest.TestCase):
    """Tests that subtract operator works"""

    def test_base_subtract_int(self):
        """Base class check"""

        p = Pseudohex('A')

        assert (int(p-1) == 9)
        assert (int(p) == 10)

    def test_base_rsubtract_int(self):
        """Base class check"""

        p = Pseudohex('A')

        assert (int(1 - p) == 9)

    def test_base_subtract_str(self):
        """Base class check"""

        p = Pseudohex('A')

        assert ((str(p-1)) == '9')

    def test_base_rsubtract_str(self):
        """Base class check"""

        p = Pseudohex('A')

        assert (str(1 - p) == '9')

    def test_base_subtract_underflow(self):
        """Check that subtracting below the miniumum value just returns the same min value"""

        p = Pseudohex('0')

        assert ((str(p-1)) == Pseudohex('0'))

    def test_base_subtract_other(self):
        """Base class check"""

        p = Pseudohex('A')

        assert (Pseudohex('4') == (p - Pseudohex('6')))

