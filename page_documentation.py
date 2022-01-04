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
from helpers import read_markdown, read_eq

def show_page():

    for i in range(8):
        st.sidebar.write("")

    definitions = read_markdown("docs/markdown/definitions.md")
    st.markdown(definitions)
    
    st.header("Parameters")

    redshift = read_markdown("docs/markdown/redshift.md")
    redshift_eq = read_eq("docs/equations/redshift")
    st.markdown(redshift)
    st.latex(fr'''{redshift_eq}''')

    hubble = read_markdown("docs/markdown/hubble.md")
    hubble_eq = read_eq("docs/equations/hubble")
    hubble_dimensionless = read_markdown("docs/markdown/hubble_dimensionless.md")
    hubble_dimensionless_eq = read_eq("docs/equations/hubble_dimensionless")
    st.markdown(hubble)
    st.latex(fr'''{hubble_eq}''')
    st.markdown(hubble_dimensionless)
    st.latex(fr'''{hubble_dimensionless_eq}''')

    energy_density = read_markdown("docs/markdown/energy_density.md")
    energy_density_eq = read_eq("docs/equations/energy_density")
    Ωk = read_markdown("docs/markdown/omega_k.md")
    st.markdown(energy_density, unsafe_allow_html=True)
    st.latex(fr'''{energy_density_eq}''')
    st.markdown(Ωk, unsafe_allow_html=True)

    equation_of_state = read_markdown("docs/markdown/eos.md")
    equation_of_state_eq = read_eq("docs/equations/eos")
    st.markdown(equation_of_state)
    st.latex(fr'''{equation_of_state_eq}''')

    st.header("Distance measures")

    comoving_distance = read_markdown("docs/markdown/comoving_distance.md")
    comoving_distance_eq = read_eq("docs/equations/comoving_distance")
    st.markdown(comoving_distance, unsafe_allow_html=True)
    st.latex(fr'''{comoving_distance_eq}''')

    transverse_comoving_distance = read_markdown("docs/markdown/transverse_comoving_distance.md")
    transverse_comoving_distance_eq = read_eq("docs/equations/transverse_comoving_distance")
    st.markdown(transverse_comoving_distance, unsafe_allow_html=True)
    st.latex(fr'''{transverse_comoving_distance_eq}''')

    luminosity_distance = read_markdown("docs/markdown/luminosity_distance.md")
    luminosity_distance_eq = read_eq("docs/equations/luminosity_distance")
    st.markdown(luminosity_distance, unsafe_allow_html=True)
    st.latex(fr'''{luminosity_distance_eq}''')

    angular_diameter_distance = read_markdown("docs/markdown/angular_diameter_distance.md")
    angular_diameter_distance_eq = read_eq("docs/equations/angular_diameter_distance")
    st.markdown(angular_diameter_distance, unsafe_allow_html=True)
    st.latex(fr'''{angular_diameter_distance_eq}''')

    st.header("Associated quantities")

    lookback_time = read_markdown("docs/markdown/lookback_time.md")
    lookback_time_eq = read_eq("docs/equations/lookback_time")
    st.markdown(lookback_time, unsafe_allow_html=True)
    st.latex(fr'''{lookback_time_eq}''')

    comoving_volume = read_markdown("docs/markdown/comoving_volume.md")
    comoving_volume_eq = read_eq("docs/equations/comoving_volume")
    st.markdown(comoving_volume, unsafe_allow_html=True)
    st.latex(fr'''{comoving_volume_eq}''')

    return
