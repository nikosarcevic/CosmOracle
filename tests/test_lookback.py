import unittest
import background as bg

class LookbackTest(unittest.TestCase):
    def test_redshift(self):
        data = 1.
        result = bg.get_lookback_time(data)
        self.assertAlmostEqual(result, 7.977 , delta=0.1)
    def test_redshift_int(self):
        data = 1
        result = bg.get_lookback_time(data)
        self.assertAlmostEqual(result, 7.977, delta=0.1)
    def test_redshift_negative(self):
        data = -1.
        self.assertRaises(ValueError, bg.get_lookback_time, data)
