# %%
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt


def m_to_pc(value):
    
    '''
    Convert a distance in meters to distance in parsecs.
    
    Args: distance in meters
    
    Returns: distance in parsecs
    '''
    
    conv_fac = 3.0857e16 # unit: m/pc
    dist_pc = value / conv_fac # unit: pc
    
    return dist_pc
    
def pc_to_m(value):
    
    '''
    Convert a distance in parsecs to distance in meters.
    
    Args: distance in parsecs
    
    Returns: distance in meters
    '''
    
    conv_fac = 3.0857e16 # unit: m/pc
    dist_m = value * conv_fac # unit: m
    
    return dist_m

def m_to_mpc(value):
    
    '''
    Convert a distance in meters to distance in megaparsecs.
    
    Args: distance in meters
    
    Returns: distance in megaparsecs
    '''
    
    conv_fac = 3.0857e16 * 1e6
    dist_mpc = value / conv_fac # unit: mpc
    
    return dist_mpc
    
    
def mpc_to_m(value):
    
    '''
    Convert a distance in megaparsecs to distance in meters.
    
    Args: distance in megaparsecs
    
    Returns: distance in meters
    '''
    
    conv_fac = 3.0857e16 * 1e6
    dist_m = value * conv_fac # unit: m
    
    return dist_m   
    

def ly_to_m(value):
    
    '''
    Convert a distance in light years to distance in meters.
    
    Args: distance in light years
    
    Returns: distance in meters
    '''
    
    conv_fac = 9.4607e15 # unit: m/ly
    dist_m = value * conv_fac # unit: ly
    
    return dist_m
    
    
def m_to_ly(value):
    
    '''
    Convert a distance in meters to distance in light years.
    
    Args: distance in meters
    
    Returns: distance in light years
    '''
    
    conv_fac = 9.4607e15 # unit: m/ly
    dist_ly = value / conv_fac # unit_ ly
    
    return dist_ly
    
    
def pc_to_ly(value):
    
    '''
    Convert a distance in parsecs to distance in light years.
    
    Args: distance in parsecs
    
    Returns: distance in light years
    '''
    
    conv_fac = 3.26156
    dist_ly = value * conv_fac
    
    return dist_ly


def ly_to_pc(value):
    
    '''
    Convert a distance in light years to distance in parsecs.
    
    Args: distance in light years
    
    Returns: distance in parsecs
    '''
    
    conv_fac = 3.26156
    dist_pc = value / conv_fac
    
    return dist_pc


def mpc_to_ly(value):
    
    '''
    Convert a distance in megaparsecs to distance in light years.
    
    Args: distance in megaparsecs
    
    Returns: distance in light years
    '''
    
    conv_fac = 3.26156e6
    dist_ly = value * conv_fac
    
    return dist_ly


def ly_to_mpc(value):
    
    '''
    Convert a distance in light years to distance in megaparsecs.
    
    Args: distance in light years
    
    Returns: distance in megaparsecs
    '''
    
    conv_fac = 3.26156e6
    dist_mpc = value / conv_fac
    
    return dist_mpc
    
    
    