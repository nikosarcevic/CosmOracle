# %%
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from scipy import integrate

def calculate_distance_modulus(d):
    '''
    Method to compute the distance modulus for a given distance.
    
    Distance modulus nu is defined as the difference between the apparent magnitude m and
    the absolute magnitude  M of an astronomical object, nu = m - M.
    
    The distance modulus is then: nu = m - M = 5 * log10(d/{10 pc})
    
    Args: distance d in parsecs
    
    Returns: the distance modulus
    '''
    mu = 5 * np.log10(d/10)
    
    return mu

mu = calculate_distance_modulus(d)
value = st.text_input('distance', 'enter distance [in pc] here') 

if value:
    st.write(my_model.predict(value))

test = st.text_input('distance', 'enter distance [in pc] here')