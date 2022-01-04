# %%
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

def show_page():

    for i in range(8):
        st.sidebar.write("")

    intro_markdown = read_markdown("docs/markdown/introduction.md")
    st.markdown(intro_markdown)

    return
