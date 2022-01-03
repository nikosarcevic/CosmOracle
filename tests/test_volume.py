import unittest
import background as bg

class ComovingVolumeTest(unittest.TestCase):
    def test_redshift(self):
        data = 1.
        result = bg.get_comoving_volume(data)
        self.assertAlmostEqual(1e-9*result, 166.3466 , delta=0.1)
    def test_redshift_int(self):
        data = 1
        result = bg.get_comoving_volume(data)
        self.assertAlmostEqual(1e-9*result, 166.3466, delta=0.1)
    def test_redshift_negative(self):
        data = -1.
        self.assertRaises(TypeError, bg.get_comoving_volume, data)
