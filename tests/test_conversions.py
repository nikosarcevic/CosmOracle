import unittest
import conversion_functions as cf

class unit_conversion_test(unittest.TestCase):

    def test_is_distance_zero(self):
        data = 0
        distances = ["meter", "parsec", "lightyear"]
        for old_unit in distances:
            for new_unit in distances: 
                with self.subTest(new_unit = new_unit):
                    result = cf.convert_unit(data, old_unit, new_unit)
                    self.assertEqual(result, 0)

    def test_is_negative(self):
        data = -2.0
        result = cf.convert_unit(data, "meter", "lightyear")
        self.assertAlmostEqual(result, -2.1140016680494e-16)
    
    def test_type_value(self):
        data = "A"
        self.assertRaises(TypeError,
                          lambda x: cf.convert_unit(x, "meter", "parsec"), 
                          data)

    def test_type_from(self):
        data = 1
        self.assertRaises(TypeError, 
                          lambda x: cf.convert_unit(1, x, "meter"),
                          data)

    def test_type_to(self):
        data = 2
        self.assertRaises(TypeError, 
                          lambda x: cf.convert_unit(1, "meter", x),
                          data)

    def test_is_angle_zero(self):
        data = 0
        angles = ["arcsec", "radian"]
        for old_unit in angles:
            for new_unit in angles: 
                with self.subTest(new_unit = new_unit):
                    result = cf.convert_unit(data, old_unit, new_unit)
                    self.assertEqual(result, 0)
