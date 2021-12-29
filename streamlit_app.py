"""
CosmOracleApp
Created December 2021
@authors: 
[Marco Bonici](https://github.com/marcobonici), 
[Niko Sarcevic](https://github.com/nikosarcevic) and 
[Matthijs van der Wild](https://github.com/lonbar)
"""

# %%
import numpy as np
import streamlit as st
from scipy import integrate
import background as bg
import matplotlib.pyplot as plt
import plot_script as ps
import page_introduction as pi
import page_distances as pd

# Page settings

st.set_page_config(page_title='CosmΩracle')

#Sidebar settings

logo, name = st.sidebar.columns(2)
with logo:
    image = 'https://github.com/nikosarcevic/CosmOracle/blob/main/images/LogowNameOld.png?raw=true'
    st.image(image, use_column_width=True)

st.sidebar.write(" ")

pages = {
        "Introduction": pi,
        "Cosmological Distances": pd
    }

st.sidebar.title("Main options")

    # Radio buttons to select desired option
#page = st.sidebar.radio("Select:", tuple(pages.keys()))
page = st.sidebar.selectbox('Page', tuple(pages.keys()))

pages[page].show_page()
        
# About
st.sidebar.header("About")
st.sidebar.markdown(
                """
                CosmΩracle app is created and maintained by 
                [**Marco Bonici**](https://github.com/marcobonici), [**Niko Sarcevic**](https://github.com/nikosarcevic) and [**Matthijs van der Wild**](https://github.com/lonbar). If you like this app please star its
                [**GitHub**](https://github.com/nikosarcevic/CosmoCompute/)
                repo, share it and feel free to open an issue if you find a bug 
                or if you want some additional features.
                """)
    
