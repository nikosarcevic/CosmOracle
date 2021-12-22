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
    ΩK = 1-ΩM-ΩDE-ΩR
    return np.sqrt(ΩM*(1+z)**3+ΩR*(1+z)**4+ΩDE*(1+z)**(3*(1+w0+wa))*np.exp(-3*wa*z/(1+z))+ΩK*(1+z)**2)

def H_z(z, H0=constants['Hubble0'], ΩM=constants['matter-density'], 
        ΩDE=constants['DE-density'], ΩR=constants['rad-density'], 
        w0=constants['w0'], wa=constants['wa']):
    """
    Method to compute the Hubble rate in the w0waCDm cosmology
    """
    return H0*E_z(z, ΩM, ΩDE, ΩR, w0, wa)

def comoving_distance(z, H0=constants['Hubble0'], ΩM=constants['matter-density'], 
                      ΩDE=constants['DE-density'], ΩR=constants['rad-density'], 
                      w0=constants['w0'], wa=constants['wa']):
    """
    Method to compute the comoving distance
    """
    integrand = lambda x: 1/E_z(x, ΩM, ΩDE, ΩR, w0, wa)
    int, err = integrate.quad(integrand, 0, z)
    c0 = constants['speed-of-light']
    return c0/H0*int

def transverse_comoving_distance(z, H0=constants['Hubble0'], ΩM=constants['matter-density'],
                                 ΩDE=constants['DE-density'], ΩR=constants['rad-density'],
                                 w0=constants['w0'], wa=constants['wa']):
    """
    Compute the transverse comoving distance
    """
    D_c = comoving_distance(z, H0, ΩM, ΩDE, ΩR, w0, wa)
    ΩK = 1 - ΩM - ΩDE - ΩR
    c0 = constants['speed-of-light']
    x = np.sqrt(ΩK + 0j) * D_c / (c0 / H0)
    if ΩDE == 0:
        D_m = c0 / H0 * 2 * (2 - ΩM(1-z) - (2-ΩM)*np.sqrt(1+ΩM*z)) / (ΩM**2*(1+z))
    else:
        D_m = D_c * np.sinc(x / np.pi)
    #elif ΩK <= 0:
    #    D_m = D_c * np.sinh(x) / x
    #elif ΩK >= 0:
    #    D_m = D_c * np.sin(x) / x
    return D_m.real

def angular_diameter_distance(z, H0=constants['Hubble0'], ΩM=constants['matter-density'],
                              ΩDE=constants['DE-density'], ΩR=constants['rad-density'],
                              w0=constants['w0'], wa=constants['wa']):
    """
    Computer the angular diameter distance
    """
    return transverse_comoving_distance(z, H0, ΩM, ΩDE, ΩR, w0, wa) / (1 + z)
