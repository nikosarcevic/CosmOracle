import unittest
import background as bg

class ComovingVolumeTest(unittest.TestCase):
    def test_redshift(self):
        data = 1.
        result = bg.comoving_volume(data)
        self.assertAlmostEqual(result, 1.663466e12 , delta=0.1)
    def test_redshift_int(self):
        data = 1
        result = bg.comoving_volume(data)
        self.assertAlmostEqual(result, 1.663466e12, delta=0.1)
    def test_redshift_negative(self):
        data = -1.
        self.assertRaises(TypeError, bg.comoving_volume, data)