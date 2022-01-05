import numpy as np

def convert_unit(value, from_unit, to_unit):
    """
    Converts quantity value in from_unit to value' in to_unit
    """

    conversion_table = {
        "meter" : {
            "parsec"     : 1/(3.0857e16),
            "kiloparsec" : 1/(3.0857e16 * 1e3),
            "megaparsec" : 1/(3.0857e16 * 1e6),
            "gigaparsec" : 1/(3.0857e16 * 1e6),
            "lightyear"  : 1/(9.4607e15)
        },
        "parsec" : {
            "meter"     : 3.0857e16,
            "kilometer" : 3.0857e16 * 1e-3,
            "lightyear" : 3.26156
        },
        "megaparsec" : {
            "meter"     : 3.0857e16 * 1e6,
            "lightyear" : 3.26156e6
        },
        "lightyear" : {
            "meter"      : 9.4607e15,
            "parsec"     : 1/3.26156,
            "megaparsec" : 1/3.26156e6
        },
        "arcsec" : {
            "radian" : 1/(180 / np.pi * 3600)
        },
        "radian" : {
            "arcsec" : 180 / np.pi * 3600
        }
    }

    return value * conversion_table[from_unit][to_unit]
