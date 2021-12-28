import numpy as np
import yaml

from scipy import integrate

# Load all the default values / constants from YAML file
with open("cosmology-constants.yaml", "r") as constantslist:
    constants = yaml.load(constantslist, Loader=yaml.FullLoader)

def E_z(z, ΩM=constants['matter-density'], ΩDE=constants['DE-density'], 
        ΩR=constants['rad-density'], w0=constants['w0'], wa=constants['wa']):
    """
    Method to compute the adimensional Hubble rate in the w0waCDm cosmology
    """
    if isinstance(z, float) or isinstance(z, int):
        if z < 0:
            raise TypeError("Enter a non-negative redshift.")
    elif isinstance(z, np.ndarray):
        if any(t < 0 for t in z):
            raise TypeError("Enter a non-negative redshift.")
    ΩK = 1-ΩM-ΩDE-ΩR
    return np.sqrt(ΩM*(1+z)**3+ΩR*(1+z)**4+ΩDE*(1+z)**(3*(1+w0+wa))*np.exp(-3*wa*z/(1+z))+ΩK*(1+z)**2)

def H_z(z, H0=constants['Hubble0'], ΩM=constants['matter-density'], 
        ΩDE=constants['DE-density'], ΩR=constants['rad-density'], 
        w0=constants['w0'], wa=constants['wa']):
    """
    Method to compute the Hubble rate in the w0waCDm cosmology
    """
    if isinstance(z, float) or isinstance(z, int):
        if z < 0:
            raise TypeError("Enter a non-negative redshift.")
    elif isinstance(z, np.ndarray):
        if any(t < 0 for t in z):
            raise TypeError("Enter a non-negative redshift.")
    return H0*E_z(z, ΩM, ΩDE, ΩR, w0, wa)

def comoving_distance(z, H0=constants['Hubble0'], ΩM=constants['matter-density'], 
                      ΩDE=constants['DE-density'], ΩR=constants['rad-density'], 
                      w0=constants['w0'], wa=constants['wa']):
    """
    Method to compute the comoving distance
    """
    integrand = lambda x: 1/E_z(x, ΩM, ΩDE, ΩR, w0, wa)
    if isinstance(z, float) or isinstance(z, int):
        if z < 0:
            raise TypeError("Enter a non-negative redshift.")
        result, _ = integrate.quad(integrand, 0, z)
    elif isinstance(z, np.ndarray):
        if any(t < 0 for t in z):
            raise TypeError("Enter a non-negative redshift.")
        result = np.vectorize(lambda x: integrate.quad(integrand, 0, x)[0])(z)
    else:
        raise TypeError(f'Expected "Union[float, np.ndarray]", got {type(z)}')
    c0 = constants['speed-of-light']
    return c0/H0*result

def transverse_comoving_distance(z, H0=constants['Hubble0'], ΩM=constants['matter-density'],
                                 ΩDE=constants['DE-density'], ΩR=constants['rad-density'],
                                 w0=constants['w0'], wa=constants['wa']):
    """
    Compute the transverse comoving distance
    """
    if isinstance(z, float) or isinstance(z, int):
        if z < 0:
            raise TypeError("Enter a non-negative redshift.")
    elif isinstance(z, np.ndarray):
        if any(t < 0 for t in z):
            raise TypeError("Enter a non-negative redshift.")
    D_c = comoving_distance(z, H0, ΩM, ΩDE, ΩR, w0, wa)
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

def angular_diameter_distance(z, H0=constants['Hubble0'], ΩM=constants['matter-density'],
                              ΩDE=constants['DE-density'], ΩR=constants['rad-density'],
                              w0=constants['w0'], wa=constants['wa']):
    """
    Compute the angular diameter distance
    """
    return transverse_comoving_distance(z, H0, ΩM, ΩDE, ΩR, w0, wa) / (1 + z)

def luminosity_distance(z, H0=constants['Hubble0'], ΩM=constants['matter-density'],
                              ΩDE=constants['DE-density'], ΩR=constants['rad-density'],
                              w0=constants['w0'], wa=constants['wa']):
    
    '''
    Compute the angular diameter distance d_l
    '''
    
    d_l = transverse_comoving_distance(z, H0, ΩM, ΩDE, ΩR, w0, wa) * (1 + z) 
    
    return d_l

def comoving_volume(z, H0=constants['Hubble0'], ΩM=constants['matter-density'],
                    ΩDE=constants['DE-density'], ΩR=constants['rad-density'],
                    w0=constants['w0'], wa=constants['wa']):

    """
    Compute the comoving volume
    """
    
    c0 = constants['speed-of-light']
    Dm = transverse_comoving_distance(z, H0, ΩM, ΩDE, ΩR, w0, wa)
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
    return (9.78e11)/H0

def lookback_time(z, H0=constants['Hubble0'], ΩM=constants['matter-density'],
                              ΩDE=constants['DE-density'], ΩR=constants['rad-density'],
                              w0=constants['w0'], wa=constants['wa']):
    """
    Method to compute the lookback time
    """
    integrand = lambda x: 1/(E_z(x, ΩM, ΩDE, ΩR, w0, wa)*(1+x))
    if isinstance(z, float) or isinstance(z, int):
        if z < 0:
            raise TypeError("Enter a non-negative redshift.")
        result, _ = integrate.quad(integrand, 0, z)
    elif isinstance(z, np.ndarray):
        if any(t < 0 for t in z):
            raise TypeError("Enter a non-negative redshift.")
        result = np.vectorize(lambda x: integrate.quad(integrand, 0, x)[0])(z)
    else:
        raise TypeError(f'Expected "Union[float, np.ndarray]", got {type(z)}')
    c0 = constants['speed-of-light']
    return result*hubble_time(H0)*1e-9
    
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
