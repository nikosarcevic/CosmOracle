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
    H0=67.
    ΩM=0.32
    ΩR=0.
    ΩDE=0.68
    w0=-1.
    wa=0.
    speed_of_light=2.99792458e5

    section_title = "Cosmological Distances"

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
        st.write('An object spanning an angle of 1 arcsec at redshift', z_value, 'is therefore', str(round(bg.proper_separation(180/3600/np.pi, float(z_value), H0=float(H0_value), ΩM=float(ΩM_value), ΩDE=float(ΩDE_value), ΩR=float(ΩR_value), w0=float(w0_value) , wa=float(wa_value)), sig_digits)), 'kpc across.')
        st.write('Comoving volume at redshift', z_value, 'is:', str(round(1e-9*bg.comoving_volume(float(z_value), H0=float(H0_value), ΩM=float(ΩM_value), ΩDE=float(ΩDE_value), ΩR=float(ΩR_value), w0=float(w0_value) , wa=float(wa_value) ), sig_digits)), 'Gpc³')
        st.write('Lookback time at redshift', z_value, 'is:', str(round(bg.lookback_time(float(z_value), H0=float(H0_value), ΩM=float(ΩM_value), ΩDE=float(ΩDE_value), ΩR=float(ΩR_value), w0=float(w0_value) , wa=float(wa_value) ), sig_digits)), 'Gyrs')
        
        z_array = np.linspace(0, float(z_value), 300)

        rz_array = bg.comoving_distance(z_array, H0=float(H0_value), ΩM=float(ΩM_value), ΩDE=float(ΩDE_value), ΩR=float(ΩR_value), w0=float(w0_value) , wa=float(wa_value) )
        trz_array = bg.transverse_comoving_distance(z_array, H0=float(H0_value), ΩM=float(ΩM_value), ΩDE=float(ΩDE_value), ΩR=float(ΩR_value), w0=float(w0_value) , wa=float(wa_value) )
        DLz_array = bg.luminosity_distance(z_array, H0=float(H0_value), ΩM=float(ΩM_value), ΩDE=float(ΩDE_value), ΩR=float(ΩR_value), w0=float(w0_value) , wa=float(wa_value) )
        DAz_array = bg.angular_diameter_distance(z_array, H0=float(H0_value), ΩM=float(ΩM_value), ΩDE=float(ΩDE_value), ΩR=float(ΩR_value), w0=float(w0_value) , wa=float(wa_value) )
        VCz_array = bg.comoving_volume(z_array, H0=float(H0_value), ΩM=float(ΩM_value), ΩDE=float(ΩDE_value), ΩR=float(ΩR_value), w0=float(w0_value) , wa=float(wa_value) )
        tlz_array = bg.lookback_time(z_array, H0=float(H0_value), ΩM=float(ΩM_value), ΩDE=float(ΩDE_value), ΩR=float(ΩR_value), w0=float(w0_value) , wa=float(wa_value) )
    
        stacked_array = np.vstack((z_array, rz_array, trz_array, DLz_array, DAz_array, VCz_array, tlz_array)).T
        np.savetxt("output.txt", stacked_array, header='z,DCz [Mpc],DMz [Mpc],DLz [Mpc],DAz [Mpc],VCz [Gpc^3],tlz [Gyr]', delimiter=',', comments='')
    
        st.write(" ")

        plot_rz = st.checkbox('Plot Comoving Distance Dc(z)')
        plot_trz = st.checkbox('Plot Transverse Comoving Distance Dm(z)')
        plot_DLz = st.checkbox('Plot Luminosity Distance Dl(z)')
        plot_DAz = st.checkbox('Plot Angular Diameter Distance Da(z)')
        
        st.write(" ")

        if plot_rz or plot_trz or plot_DLz or plot_DAz:
            
            width = st.slider("plot width", 1, 25, 10)
            height = st.slider("plot height", 1, 25, 5)
            
            log_checkbox = st.checkbox('Switch to semi-log scale')
            
            st.write(" ")
        
            plot = ps.plot_distances_lin(plot_rz, plot_trz, plot_DLz, plot_DAz, z_array, rz_array, trz_array, DLz_array, DAz_array, width, height)
            if log_checkbox:
                plot = ps.plot_distances_log(plot_rz, plot_trz, plot_DLz, plot_DAz, z_array, rz_array, trz_array, DLz_array, DAz_array, width, height)
      
            st.pyplot(plot)
        
        st.write(" ")
        
        my_expander = st.expander(label='Click for more plots')
        with my_expander:
            
            plot_VCz = st.checkbox('Plot Comoving Volume Vc(z)')
            plot_tlz = st.checkbox('Plot Lookback Time tl(z)')

            if plot_VCz:

                width = st.slider("Plot width Vc(z)", 1, 25, 10)
                height = st.slider("Plot height Vc(z)", 1, 25, 5)

                log_checkbox = st.checkbox('Switch to semi-log scale Vc(z)')
                
                st.write(" ")

                plot = ps.plot_comoving_volume_lin(plot_VCz, z_array, VCz_array, width, height)
                if log_checkbox:
                    plot = ps.plot_comoving_volume_log(plot_VCz, z_array, VCz_array, width, height)

                st.pyplot(plot)
                
            
            if plot_tlz:
                
                width = st.slider("Plot width tlz", 1, 25, 10)
                height = st.slider("Plot height tlz", 1, 25, 5)

                log_checkbox = st.checkbox('Switch to semi-log scale tl(z)')
                
                st.write(" ")

                plot = ps.plot_lookback_time_lin(plot_tlz, z_array, tlz_array, width, height)
                if log_checkbox:
                    plot = ps.plot_lookback_time_log(plot_tlz, z_array, tlz_array, width, height)

                st.pyplot(plot)
            
        st.write(" ")

        st.header('Download calculated data as a text file')
        f = open("output.txt", encoding = 'utf-8')
        file_name = st.text_input('Name the file', "filename.txt")
        st.download_button('Click to download', f, file_name = file_name)
    else:
        st.title(section_title)
        st.write('Enter the value of redshift and cosmological parameters in the sidebar and press enter.')
        
    return
  
