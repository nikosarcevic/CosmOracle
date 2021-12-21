import numpy as np
from scipy import integrate

def E_z(z, ΩM=0.32, ΩDE=0.68, ΩR=0., w0=-1., wa=0.):
    """
    Method to compute the adimensional Hubble rate in the w0waCDm cosmology
    """
    ΩK = 1-ΩM-ΩDE-ΩR
    return np.sqrt(ΩM*(1+z)**3+ΩR*(1+z)**4+ΩDE*(1+z)**(3*(1+w0+wa))*np.exp(-3*wa*z/(1+z))+ΩK*(1+z)**2)

def H_z(z, H0=67, ΩM=0.32, ΩDE=0.68, ΩR=0., w0=-1., wa=0.):
    """
    Method to compute the Hubble rate in the w0waCDm cosmology
    """
    return H0*E_z(z, ΩM, ΩDE, ΩR, w0, wa)

def comoving_distance(z, H0=67, ΩM=0.32, ΩDE=0.68, ΩR=0., w0=-1., wa=0.):
    """
    Method to compute the comoving distance
    """
    integrand = lambda x: 1/E_z(x, ΩM, ΩDE, ΩR, w0, wa)
    int, err = integrate.quad(integrand, 0, z)
    c0 = 2.99792458e5
    #TODO: this is not beautiful, maybe we could define some global constants
    return c0/H0*int