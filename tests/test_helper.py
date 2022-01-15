import unittest
import helpers as hlp
from numpy import ndarray

class GetRedshiftsTest(unittest.TestCase):
    def test_redshift_float(self):
        data = 1.
        result = hlp.get_redshifts(data)
        self.assertIsInstance(result, ndarray)
    def test_redshift_int(self):
        data = 1
        result = hlp.get_redshifts(data)
        self.assertIsInstance(result, ndarray)
    def test_redshift_string(self):
        data = "A"
        self.assertRaises(TypeError, hlp.get_redshifts, data)
