import numpy as np

from dataclasses import dataclass, field
from helpers import get_constants, check_redshift_valid_array, integration_wrapper
import conversion_functions as cf

constants = get_constants()

@dataclass
class distanceData:
    """
    Class that computes distance measures from the given input parameters.
    """

    redshift: float
    H0: float = constants['Hubble0']
    ΩM: float = constants['matter-density']
    ΩDE: float = constants['DE-density']
    ΩR: float = constants['rad-density']
    w0: float = constants['w0']
    wa: float = constants['wa']

    comoving_distance: float = field(init = False)
    transverse_comoving_distance: float = field(init = False)
    angular_diameter_distance: float = field(init = False)
    luminosity_distance: float = field(init = False)
    comoving_volume: float = field(init = False)
    lookback_time: float = field(init = False)
    proper_separation: float = field(init = False)

    def __post_init__(self):
        self.comoving_distance = get_comoving_distance(self.redshift, self.H0, self.ΩM, self.ΩDE, 
                                                  self.ΩR, self.w0, self.wa)
        self.transverse_comoving_distance = get_transverse_comoving_distance(self.redshift, self.H0, 
                                                                        self.ΩM, self.ΩDE, 
                                                                        self.ΩR, self.w0, self.wa)
        self.angular_diameter_distance = get_angular_diameter_distance(self.redshift, self.H0, self.ΩM, 
                                                                  self.ΩDE, self.ΩR, self.w0, self.wa)
        self.luminosity_distance = get_luminosity_distance(self.redshift, self.H0, self.ΩM, self.ΩDE,
                                                      self.ΩR, self.w0, self.wa)
        self.comoving_volume = 1e-9*get_comoving_volume(self.redshift, self.H0, self.ΩM, self.ΩDE, 
                                                   self.ΩR, self.w0, self.wa)
        self.proper_separation = get_proper_separation(cf.convert_unit(1, "arcsec", "radian"), 
                                                       self.redshift, self.H0, self.ΩM, 
                                                       self.ΩDE, self.ΩR, self.w0, self.wa)
        self.lookback_time = get_lookback_time(self.redshift, self.H0, self.ΩM, self.ΩDE, 
                                          self.ΩR, self.w0, self.wa)


def get_E_z(z, ΩM=constants['matter-density'], ΩDE=constants['DE-density'], 
        ΩR=constants['rad-density'], w0=constants['w0'], wa=constants['wa']):
    """
    Method to compute the adimensional Hubble rate in the w0waCDm cosmology
    """
    _ = check_redshift_valid_array(z)
    ΩK = 1 - ΩM - ΩDE - ΩR
    return np.sqrt(ΩM*(1+z)**3+ΩR*(1+z)**4+ΩDE*(1+z)**(3*(1+w0+wa))*np.exp(-3*wa*z/(1+z))+ΩK*(1+z)**2)

def get_H_z(z, H0=constants['Hubble0'], ΩM=constants['matter-density'], 
            ΩDE=constants['DE-density'], ΩR=constants['rad-density'], 
            w0=constants['w0'], wa=constants['wa']):
    """
    Method to compute the Hubble rate in the w0waCDm cosmology
    """
    _ = check_redshift_valid_array(z)
    return H0*get_E_z(z, ΩM, ΩDE, ΩR, w0, wa)

def get_comoving_distance(z, H0=constants['Hubble0'], ΩM=constants['matter-density'], 
                          ΩDE=constants['DE-density'], ΩR=constants['rad-density'], 
                          w0=constants['w0'], wa=constants['wa']):
    """
    Method to compute the comoving distance
    """
    integrand = lambda x: 1/get_E_z(x, ΩM, ΩDE, ΩR, w0, wa)
    is_array = check_redshift_valid_array(z)
    if is_array:
        result = np.vectorize(lambda x: integration_wrapper(integrand, x))(z)
    else:
        result = integration_wrapper(integrand, z)
    c0 = constants['speed-of-light']
    return c0/H0*result

def get_transverse_comoving_distance(z, H0=constants['Hubble0'], ΩM=constants['matter-density'],
                                     ΩDE=constants['DE-density'], ΩR=constants['rad-density'],
                                     w0=constants['w0'], wa=constants['wa']):
    """
    Compute the transverse comoving distance
    """
    _ = check_redshift_valid_array(z)
    D_c = get_comoving_distance(z, H0, ΩM, ΩDE, ΩR, w0, wa)
    ΩK = 1 - ΩM - ΩDE - ΩR
    c0 = constants['speed-of-light']
    x = np.sqrt(-ΩK + 0j) * D_c / (c0 / H0)
    if ΩDE == 0:
        D_m = c0 / H0 * 2 * (2 - ΩM(1-z) - (2-ΩM)*np.sqrt(1+ΩM*z)) / (ΩM**2*(1+z))
    else:
        D_m = D_c * np.sinc(x / np.pi)
    #if ΩK >= 0:
    #    D_m = D_c * np.sinh(x) / x
    #if ΩK <= 0:
    #    D_m = D_c * np.sin(x) / x
    return D_m.real

def get_angular_diameter_distance(z, H0=constants['Hubble0'], ΩM=constants['matter-density'],
                                  ΩDE=constants['DE-density'], ΩR=constants['rad-density'],
                                  w0=constants['w0'], wa=constants['wa']):
    """
    Compute the angular diameter distance
    """
    return get_transverse_comoving_distance(z, H0, ΩM, ΩDE, ΩR, w0, wa) / (1 + z)

def get_luminosity_distance(z, H0=constants['Hubble0'], ΩM=constants['matter-density'],
                            ΩDE=constants['DE-density'], ΩR=constants['rad-density'],
                            w0=constants['w0'], wa=constants['wa']):
    
    '''
    Compute the angular diameter distance d_l
    '''
    
    d_l = get_transverse_comoving_distance(z, H0, ΩM, ΩDE, ΩR, w0, wa) * (1 + z) 
    
    return d_l

def get_comoving_volume(z, H0=constants['Hubble0'], ΩM=constants['matter-density'],
                        ΩDE=constants['DE-density'], ΩR=constants['rad-density'],
                        w0=constants['w0'], wa=constants['wa']):

    """
    Compute the comoving volume
    """
    
    c0 = constants['speed-of-light']
    Dm = get_transverse_comoving_distance(z, H0, ΩM, ΩDE, ΩR, w0, wa)
    Dh = c0 / H0
    ΩK = round(1 - ΩM - ΩDE - ΩR, 7)
    # the rounding is necessary since the expression is quite sensitive to the Universe geometry and,
    # due to the floating point precision, we are nver gonna really obtain ΩK = 0
    if ΩK > 0:
        return (4*np.pi*Dh**3/(2*ΩK))*(Dm/Dh*np.sqrt(1+ΩK*(Dm/Dh)**2)-1/np.sqrt(ΩK)*np.arcsinh(np.sqrt(ΩK)*Dm/Dh))
    elif  ΩK < 0:
        return (4*np.pi*Dh**3/(2*ΩK))*(Dm/Dh*np.sqrt(1+ΩK*(Dm/Dh)**2)-1/np.sqrt(-ΩK)*np.arcsin(np.sqrt(-ΩK)*Dm/Dh))
    else:
        return 4*np.pi/3*Dm**3

def hubble_time(H0=constants['Hubble0']):
    """
    Method to compute the Hubble time in Gyrs
    """
    return (9.78e2)/H0

def get_lookback_time(z, H0=constants['Hubble0'], ΩM=constants['matter-density'],
                      ΩDE=constants['DE-density'], ΩR=constants['rad-density'],
                      w0=constants['w0'], wa=constants['wa']):
    """
    Method to compute the lookback time in Gyrs
    """
    integrand = lambda x: 1/(get_E_z(x, ΩM, ΩDE, ΩR, w0, wa)*(1+x))
    is_array = check_redshift_valid_array(z)
    if is_array:
        result = np.vectorize(lambda x: integration_wrapper(integrand, x))(z)
    else:
        result = integration_wrapper(integrand, z)
    c0 = constants['speed-of-light']
    return result*hubble_time(H0)
    
def calculate_distance_modulus(d):
    '''
    Method to compute the distance modulus for a given distance.
    
    Distance modulus mu is defined as the difference between the apparent magnitude m and
    the absolute magnitude  M of an astronomical object, mu = m - M.
    
    The distance modulus is then: mu = m - M = 5 * log10(d/{10 pc})
    
    Args: distance d in parsecs
    
    Returns: the distance modulus
    '''
    mu = 5 * np.log10(d/10)
    
    return mu

def calculate_absolute_magnitude_from_distance_modulus(m, d):
    '''
    Method to compute the absolute magnitude M from the distance modulus
    given the apparent magnitude m and distance d (in parsecs).
    
    Args: apparent magnitude m and distance d (in parsecs)
    
    Returns: the absolute magnitude M
    '''
    M = m - 5 * np.log10(d/10)
    
    return M
    
def calculate_apparent_magnitude_from_distance_modulus(M, d):
    
    '''
    Method to compute the apparent magnitude m from the distance modulus
    given the absolute magnitude M and distance d (in parsecs).
    
    Args: absolute magnitude M and distance d (in parsecs)
    
    Returns: the apparent magnitude m
    '''
    
    m = M + 5 * np.log10(d/10)
    
    return m

def calculate_distance_from_distance_modulus_for_given_nu(nu):
    
    '''
    Method to compute distance d (in parsecs) from distance modulus nu.
    
    Args: distance modulus mu (dimensionless) 
    
    Returns: distance in parsecs
    '''
    
    d = 10**((nu/5) + 1)
    
    return d

def calculate_distance_from_distance_modulus_for_given_nu(nu):
    
    '''
    Method to compute distance d (in parsecs) from distance modulus nu.
    
    Args: distance modulus mu (dimensionless) 
    
    Returns: distance in parsecs
    '''
    
    d = 10**((nu/5) + 1)
    
    return d

def calculate_distance_from_distance_modulus_for_given_M_and_m(M, m):
    
    '''
    Method to compute the distance d (in parsecs) from distance modulus given
    the absolute and apparent magnitudes.
    
    Args: absolute magnitude M and apparent magnitude m
    
    Returns: distance in parsecs
    '''
    
    d = 10**((m-M)/5 + 1)
    
    return d

def hubble_distance(H0=constants['Hubble0']):
    
    DH = c/H0
    
    return DH

def get_proper_separation(θ, z, H0=constants['Hubble0'], ΩM=constants['matter-density'],
                          ΩDE=constants['DE-density'], ΩR=constants['rad-density'],
                          w0=constants['w0'], wa=constants['wa']):
    '''
    Computes the spatial separation of a distant object

    Args: 
    angular separation θ, 
    redshift z, 
    Hubble constant H0, 
    energy densities ΩM, ΩDE, ΩR
    EOS parameters w0, wa

    Returns: spatial separation in kpc
    '''

    return 1e3 * np.tan(θ) * get_angular_diameter_distance(z, H0, ΩM, ΩDE, ΩR, w0, wa)
