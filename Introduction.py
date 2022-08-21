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
from helpers import read_markdown, add_logo, add_colophon

st.set_page_config(page_title='CosmΩracle')
add_logo()
add_colophon()

intro_markdown = read_markdown("docs/markdown/introduction.md")
st.markdown(intro_markdown)
