import numpy as np

def convert_unit(value, from_unit, to_unit):
    """
    Converts quantity value in from_unit to value' in to_unit
    """

    conversion_table = {
        "meter" : {
            "meter"      : 1,
            "parsec"     : 1/(3.0857e16),
            "kiloparsec" : 1/(3.0857e16 * 1e3),
            "megaparsec" : 1/(3.0857e16 * 1e6),
            "gigaparsec" : 1/(3.0857e16 * 1e6),
            "lightyear"  : 1/(9.4607e15)
        },
        "parsec" : {
            "meter"     : 3.0857e16,
            "kilometer" : 3.0857e16 * 1e-3,
            "parsec"    : 1,
            "lightyear" : 3.26156
        },
        "megaparsec" : {
            "meter"     : 3.0857e16 * 1e6,
            "megaparsec": 1,
            "lightyear" : 3.26156e6
        },
        "lightyear" : {
            "meter"      : 9.4607e15,
            "parsec"     : 1/3.26156,
            "megaparsec" : 1/3.26156e6,
            "lightyear"  : 1
        },
        "arcsec" : {
            "arcsec" : 1,
            "radian" : 1/(180 / np.pi * 3600)
        },
        "radian" : {
            "arcsec" : 180 / np.pi * 3600,
            "radian" : 1
        }
    }

    if not (isinstance(value, int) or isinstance(value, float)):
        raise TypeError("Invalid numerical value.")
    if not (isinstance(from_unit, str) and isinstance(to_unit, str)):
        raise TypeError("Ensure that your units are valid strings.")
    elif not all(unit in conversion_table.keys() for unit in [from_unit, to_unit]):
        raise TypeError("Some units are unavailable.")

    return value * conversion_table[from_unit][to_unit]
