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

