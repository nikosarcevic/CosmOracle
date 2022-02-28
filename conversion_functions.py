import numpy as np
from helpers import get_constants

def convert_unit(value, from_unit, to_unit):
    """
    Converts quantity value in from_unit to value' in to_unit
    """
    # constants
    speed_of_light = get_constants()["speed-of-light"] * 1e3 # in km / s

    # angle conversions
    rad_per_deg    = 180 / np.pi
    deg_per_arcsec = 3600.

    # time conversions
    year_per_sec = 3600 * 24 * 365.25 # note, this is a Julian year

    # length conversions
    meter_per_au     = 1 / 149597870700.
    au_per_parsec    = np.tan(1 / rad_per_deg / deg_per_arcsec)
    meter_per_parsec = meter_per_au * au_per_parsec
    ly_per_meter     = speed_of_light * year_per_sec
    ly_per_parsec    = ly_per_meter * meter_per_au * au_per_parsec 

    conversion_table = {
        "meter" : {
            "meter"      : 1,
            "parsec"     : meter_per_parsec,
            "kiloparsec" : meter_per_parsec / 1e3,
            "megaparsec" : meter_per_parsec / 1e6,
            "gigaparsec" : meter_per_parsec / 1e9,
            "lightyear"  : 1 / ly_per_meter
        },
        "parsec" : {
            "meter"     : 1 / meter_per_parsec,
            "parsec"    : 1,
            "kilometer" : 1e-3 / meter_per_parsec,
            "lightyear" : 1 / ly_per_parsec
        },
        "megaparsec" : {
            "meter"     : 1e6 / meter_per_parsec,
            "kilometer" : 1e3 / meter_per_parsec,
            "lightyear" : 1e6 / ly_per_parsec
        },
        "lightyear" : {
            "meter"      : ly_per_meter,
            "parsec"     : ly_per_parsec,
            "megaparsec" : ly_per_parsec / 1e6,
            "lightyear"  : 1
        },
        "arcsec" : {
            "arcsec" : 1,
            "radian" : 1 / deg_per_arcsec / rad_per_deg
        },
        "radian" : {
            "radian" : 1,
            "arcsec" : rad_per_deg * deg_per_arcsec
        },
        "second" : {
            "year" : 1 / year_per_sec
        },
        "year" : {
            "second" : year_per_sec
        }
    }

    if not (isinstance(value, int) or isinstance(value, float)):
        raise TypeError("Invalid numerical value.")
    if not (isinstance(from_unit, str) and isinstance(to_unit, str)):
        raise TypeError("Ensure that your units are valid strings.")
    elif not all(unit in conversion_table.keys() for unit in [from_unit, to_unit]):
        raise TypeError("Some units are unavailable.")

    return value * conversion_table[from_unit][to_unit]
