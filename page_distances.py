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

    #Default values
    H0=67
    ΩM=0.32
    ΩR=0
    ΩDE=0.68
    w0=-1.
    wa=0
    speed_of_light=2.99792458e5

    z_value = st.sidebar.text_input('Redshift')
    H0_value = st.sidebar.text_input('Hubble Constant [km/s/Mpc]', str(H0))
    ΩM_value = st.sidebar.text_input('Matter Density', str(ΩM))
    ΩDE_value = st.sidebar.text_input('Dark Energy Density', str(ΩDE))
    ΩR_value = st.sidebar.text_input('Radiation Density', str(ΩR))
    w0_value = st.sidebar.text_input('w0', str(w0))
    wa_value = st.sidebar.text_input('wa', str(wa))

    sig_digits = int(st.sidebar.text_input('Significant Digits', str(4)))

    if z_value:
        st.title('Results')
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
        
            lin = ps.plot_distances_lin(plot_rz, plot_trz, plot_DLz, plot_DAz, z_array, rz_array, trz_array, DLz_array, DAz_array, width, height)
        
            log = ps.plot_distances_log(plot_rz, plot_trz, plot_DLz, plot_DAz, z_array, rz_array, trz_array, DLz_array, DAz_array, width, height)
        
            lin_plot = st.pyplot(lin)
        
        
            log_checkbox = st.checkbox('Semi-log scale')
        
            if log_checkbox:
                log_plot = st.pyplot(log)
        
        
        st.write(" ")

        f = open("output.txt", encoding = 'utf-8')
        file_name = st.text_input('Name your file', "filename.txt")
        st.download_button('Download text file', f, file_name = file_name)
        
    return
  
