import unittest
import background as bg

class ComovingDistanceTest(unittest.TestCase):
    def test_redshift(self):
        data = 1.
        result = bg.get_comoving_distance(data)
        self.assertAlmostEqual(result, 3411.733, delta=0.1)
    def test_redshift_int(self):
        data = 1
        result = bg.get_comoving_distance(data)
        self.assertAlmostEqual(result, 3411.733, delta=0.1)
    def test_redshift_negative(self):
        data = -1.
        self.assertRaises(TypeError, bg.get_comoving_distance, data)
    #def test_redshift_string(self):
    #    data = "1."
    #    results = bg.comoving_distance(data)
    #    self.assertEqual(result, 3411.733,)
    #    with

