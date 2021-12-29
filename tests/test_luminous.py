import unittest
import background as bg

class LuminosityDistanceTest(unittest.TestCase):
    def test_redshift(self):
        data = 1.
        result = bg.luminosity_distance(data)
        self.assertAlmostEqual(result, 6823.4666, delta=0.1)
    def test_redshift_int(self):
        data = 1
        result = bg.luminosity_distance(data)
        self.assertAlmostEqual(result, 6823.4666, delta=0.1)
    def test_redshift_negative(self):
        data = -1.
        self.assertRaises(TypeError, bg.luminosity_distance, data)