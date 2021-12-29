import unittest
import background as bg

class AngularDistanceTest(unittest.TestCase):
    def test_redshift(self):
        data = 1.
        result = bg.angular_diameter_distance(data)
        self.assertAlmostEqual(result, 1705.8666, delta=0.1)
    def test_redshift_int(self):
        data = 1
        result = bg.angular_diameter_distance(data)
        self.assertAlmostEqual(result, 1705.8666, delta=0.1)
    def test_redshift_negative(self):
        data = -1.
        self.assertRaises(TypeError, bg.angular_diameter_distance, data)