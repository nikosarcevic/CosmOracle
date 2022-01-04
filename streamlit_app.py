"""
CosmOracleApp
Created December 2021
@authors: 
[Marco Bonici](https://github.com/marcobonici), 
[Niko Sarcevic](https://github.com/nikosarcevic) and 
[Matthijs van der Wild](https://github.com/lonbar)
"""

import streamlit as st
from helpers import read_markdown

import page_introduction as pi
import page_distances as pd
import page_documentation as doc


# Page settings

st.set_page_config(page_title='CosmΩracle')

#Sidebar settings

logo, name = st.sidebar.columns(2)
with logo:
    image = 'https://github.com/nikosarcevic/CosmOracle/blob/main/images/LogowName.png?raw=true'
    st.image(image, use_column_width=True)

st.sidebar.write(" ")

pages = {
        "Introduction": pi,
        "Cosmological Distances": pd,
        "Definitions": doc,
    }

st.sidebar.title("Main options")

# Radio buttons to select desired option
page = st.sidebar.radio("", tuple(pages.keys()))

pages[page].show_page()
        
# About
about = read_markdown("docs/markdown/about.md")
st.sidebar.markdown(about)
