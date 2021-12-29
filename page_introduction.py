# %%
"""
CosmOracleApp
Created December 2021
@authors: 
[Marco Bonici](https://github.com/marcobonici), 
[Niko Sarcevic](https://github.com/nikosarcevic) and 
[Matthijs van der Wild](https://github.com/lonbar)
"""

import numpy as np
import streamlit as st
from scipy import integrate
import background as bg
import matplotlib.pyplot as plt
import plot_script as ps
def show_page():
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")



    st.title('CosmΩracle')
    st.markdown('Hello and welcome to CosmΩracle!')
    st.markdown('Computing distances in cosmology is not straightforward. If you wish to compute the values of the comoving distance, luminosity distance or angular diameter distance - just enter the values of cosmological parameters in the sidebar and press enter. Note that the default cosmology is already set.')
    st.markdown('CosmΩracle will also plot those distances as a function of redshift. In case you want to plot it yourself - you can easily download the data in a .txt format.')
    
    my_expander = st.expander(label='Click here for demo')
    with my_expander:
        'Here we give a short tutorial on how the app works and what it can be done with it.'
        #clicked = st.button('Click me!')


    st.title("About")
    st.markdown('CosmΩracle app is created and maintained by [**Marco Bonici**](https://github.com/marcobonici), [**Niko Sarcevic**](https://github.com/nikosarcevic) and [**Matthijs van der Wild**](https://github.com/lonbar).') 
    st.markdown('If you like this app please star its [**GitHub**](https://github.com/nikosarcevic/CosmOracle/) repo, share it and feel free to open an issue if you find a bug or if you want some additional features.')


    st.title('Cite')


    st.title('References')
    st.markdown('D. Hogg, *Distance Measures in Cosmology*, 2000 [astro-ph/9905116v4](https://arxiv.org/abs/astro-ph/9905116)')
    return
