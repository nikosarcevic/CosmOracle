import unittest
import background as bg

class Transverse_CDistance(unittest.TestCase):
    def test_cdistance(self):
        data = 1.
        result = bg.transverse_comoving_distance(data)
        self.assertAlmostEqual(result, 3411.733, delta=0.1)
    def test_cdistance_int(self):
        data = 1
        result = bg.transverse_comoving_distance(data)
        self.assertAlmostEqual(result, 3411.733, delta=0.1)
    def test_cdistance_negative(self):
        data = -1.
        result = bg.transverse_comoving_distance(data)
        self.assertEqual(result, "Booh, no negative redshifts!")
