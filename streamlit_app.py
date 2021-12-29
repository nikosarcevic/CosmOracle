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

# Page settings

st.set_page_config(page_title='CosmΩracle')

#Sidebar settings

logo, name = st.sidebar.columns(2)
with logo:
    image = 'https://github.com/nikosarcevic/CosmOracle/blob/main/images/LogowNameOld.png?raw=true'
    st.image(image, use_column_width=True)

st.sidebar.write(" ")

#Default values
H0=67
ΩM=0.32
ΩR=0
ΩDE=0.68
w0=-1.
wa=0
speed_of_light=2.99792458e5

z_value = st.sidebar.text_input('Redshift')
H0_value = st.sidebar.text_input('Hubble Constant', str(H0))
ΩM_value = st.sidebar.text_input('Matter Density', str(ΩM))
ΩDE_value = st.sidebar.text_input('Dark Energy Density', str(ΩDE))
ΩR_value = st.sidebar.text_input('Radiation Density', str(ΩR))
w0_value = st.sidebar.text_input('w0', str(w0))
wa_value = st.sidebar.text_input('wa', str(wa))

sig_digits = int(st.sidebar.text_input('Significant Digits', str(4)))

if not z_value:
    st.title('CosmΩracle')
    st.markdown('Hello and welcome to CosmΩracle!')
    st.markdown('Computing distances in cosmology is not straightforward. If you wish to compute the values of the comoving distance, luminosity distance or angular diameter distance - just enter the values of cosmological parameters in the sidebar and press enter. Note that the default cosmology is already set.')
    st.markdown('CosmΩracle will also plot those distances as a function of redshift. In case you want to plot it yourself - you can easily download the data in a .txt format.')
    
    my_expander = st.expander(label='Click here for demo')
    with my_expander:
        'Here we give a short tutorial on how the app works and what it can be done with it.'
        #clicked = st.button('Click me!')

if not z_value:
    st.title("About")
    st.markdown('CosmΩracle app is created and maintained by [**Marco Bonici**](https://github.com/marcobonici), [**Niko Sarcevic**](https://github.com/nikosarcevic) and [**Matthijs van der Wild**](https://github.com/lonbar).') 
    st.markdown('If you like this app please star its [**GitHub**](https://github.com/nikosarcevic/CosmOracle/) repo, share it and feel free to open an issue if you find a bug or if you want some additional features.')

if not z_value:
    st.title('Cite')
    
if not z_value:
    st.title('References')
    
   
if z_value:
    st.write('Comoving distance at redshift', z_value, 'is:', str(round(bg.comoving_distance(float(z_value), H0=float(H0_value), ΩM=float(ΩM_value), ΩDE=float(ΩDE_value), ΩR=float(ΩR_value), w0=float(w0_value) , wa=float(wa_value) ), sig_digits)), 'Mpc')
    st.write('Transverse comoving distance at redshift', z_value, 'is:', str(round(bg.transverse_comoving_distance(float(z_value), H0=float(H0_value), ΩM=float(ΩM_value), ΩDE=float(ΩDE_value), ΩR=float(ΩR_value), w0=float(w0_value) , wa=float(wa_value) ), sig_digits)), 'Mpc')
    st.write('Luminosity distance at redshift', z_value, 'is:', str(round(bg.luminosity_distance(float(z_value), H0=float(H0_value), ΩM=float(ΩM_value), ΩDE=float(ΩDE_value), ΩR=float(ΩR_value), w0=float(w0_value) , wa=float(wa_value) ), sig_digits)), 'Mpc')
    st.write('Angular diameter distance at redshift', z_value, 'is:', str(round(bg.angular_diameter_distance(float(z_value), H0=float(H0_value), ΩM=float(ΩM_value), ΩDE=float(ΩDE_value), ΩR=float(ΩR_value), w0=float(w0_value) , wa=float(wa_value) ), sig_digits)), 'Mpc')
    z_array = np.linspace(0, float(z_value), 300)

    rz_array = bg.comoving_distance(z_array, H0=float(H0_value), ΩM=float(ΩM_value), ΩDE=float(ΩDE_value), ΩR=float(ΩR_value), w0=float(w0_value) , wa=float(wa_value) )
    trz_array = bg.transverse_comoving_distance(z_array, H0=float(H0_value), ΩM=float(ΩM_value), ΩDE=float(ΩDE_value), ΩR=float(ΩR_value), w0=float(w0_value) , wa=float(wa_value) )
    DLz_array = bg.luminosity_distance(z_array, H0=float(H0_value), ΩM=float(ΩM_value), ΩDE=float(ΩDE_value), ΩR=float(ΩR_value), w0=float(w0_value) , wa=float(wa_value) )
    DAz_array = bg.angular_diameter_distance(z_array, H0=float(H0_value), ΩM=float(ΩM_value), ΩDE=float(ΩDE_value), ΩR=float(ΩR_value), w0=float(w0_value) , wa=float(wa_value) )
    
    stacked_array = np.vstack((z_array, rz_array, trz_array, DLz_array, DAz_array)).T
    np.savetxt("output.txt", stacked_array, header='z,DCz,DMz,DLz,DAz', delimiter=',', comments='')
    
    st.write(" ")

    plot_rz = st.checkbox('Plot Comoving Distance Dc')
    plot_trz = st.checkbox('Plot Transverse Comoving Distance Dm')
    plot_DLz = st.checkbox('Plot Luminosity Distance Dl')
    plot_DAz = st.checkbox('Plot Angular Diameter Distance Da')
    
    st.write(" ")

    if plot_rz or plot_trz or plot_DLz or plot_DAz:
        
        width = st.slider("plot width", 1, 25, 10)
        height = st.slider("plot height", 1, 25, 5)
        
        lin_plot = ps.plot_distances_lin(plot_rz, plot_trz, plot_DLz, plot_DAz, z_array, rz_array, trz_array, DLz_array, DAz_array, width, height)
        
        log_plot = ps.plot_distances_log(plot_rz, plot_trz, plot_DLz, plot_DAz, z_array, rz_array, trz_array, DLz_array, DAz_array, width, height)
        
        st.pyplot(log_plot)
        
        
    st.write(" ")

    f = open("output.txt", encoding = 'utf-8')
    file_name = st.text_input('Name your file', "filename.txt")
    st.download_button('Download text file', f, file_name = file_name)
        
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
    
