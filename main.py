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
from page_intro import page_intro
from page_distances import page_distances

st.set_page_config(page_title='CosmΩracle')


#Sidebar settings

logo, name = st.sidebar.columns(2)
with logo:
    image = 'https://github.com/nikosarcevic/CosmOracle/blob/main/images/LogowNameOld.png?raw=true'
    st.image(image, use_column_width=True)

st.sidebar.write(" ")

def main():
    """
    Register pages Introduction and Distances:
        page_intro - contains a page with app information
        page_distances - contains a page to calculate distances in
        cosmology
    """

    pages = {
        "Introduction": page_intro,
        "Calculate Distances": page_distances
    }

    st.sidebar.title("Main options")

    # Radio buttons to select desired option
    page = st.sidebar.radio("Select:", tuple(pages.keys()))
                                
    # Display the selected page with the session state
    pages[page]()

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


if __name__ == "__main__":
    main()
        
