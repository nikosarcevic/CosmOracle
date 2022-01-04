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
#from scipy import integrate
import background as bg
#import matplotlib.pyplot as plt

from helpers import plot_graph

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

        inputParms = bg.distanceData(float(z_value), float(H0_value), float(ΩM_value), float(ΩDE_value),
                                     float(ΩR_value), float(w0_value), float(wa_value))

        st.title('Results')

        st.write('Comoving distance at redshift', str(inputParms.redshift), 'is:', 
                 str(round(inputParms.comoving_distance, sig_digits)), 'Mpc')
        st.write('Transverse comoving distance at redshift', str(inputParms.redshift), 'is:', 
                 str(round(inputParms.transverse_comoving_distance, sig_digits)), 'Mpc')
        st.write('Luminosity distance at redshift', str(inputParms.redshift), 'is:', 
                 str(round(inputParms.luminosity_distance, sig_digits)), 'Mpc')
        st.write('Angular diameter distance at redshift', str(inputParms.redshift), 'is:', 
                 str(round(inputParms.angular_diameter_distance, sig_digits)), 'Mpc')
        st.write('An object spanning an angle of 1 arcsec at redshift', str(inputParms.redshift), 'is therefore', 
                 str(round(inputParms.proper_separation, sig_digits)), 'kpc across.')
        st.write('Comoving volume at redshift', str(inputParms.redshift), 'is:', 
                 str(round(inputParms.comoving_volume, sig_digits)), 'Gpc³')
        st.write('Lookback time at redshift', str(inputParms.redshift), 'is:', 
                 str(round(inputParms.lookback_time, sig_digits)), 'Gyrs')
        
        z_array = np.linspace(0, inputParms.redshift, 300)

        inputParmsPlot = bg.distanceData(z_array, inputParms.H0, inputParms.ΩM, inputParms.ΩDE, 
                                         inputParms.ΩR, inputParms.w0, inputParms.wa)

        rz_array = inputParmsPlot.comoving_distance
        trz_array = inputParmsPlot.transverse_comoving_distance
        DLz_array = inputParmsPlot.luminosity_distance
        DAz_array = inputParmsPlot.angular_diameter_distance
        VCz_array = inputParmsPlot.comoving_volume
        tlz_array = inputParmsPlot.lookback_time
    
        stacked_array = np.vstack((inputParmsPlot.redshift, 
                                   inputParmsPlot.comoving_distance, 
                                   inputParmsPlot.transverse_comoving_distance, 
                                   inputParmsPlot.luminosity_distance, 
                                   inputParmsPlot.angular_diameter_distance, 
                                   inputParmsPlot.comoving_volume, 
                                   inputParmsPlot.lookback_time)).T
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
        
            plot = plot_graph(width, height, z_array, 
                              (plot_rz, rz_array, "Comoving distance"), 
                              (plot_trz, trz_array, "Transverse comoving distance"), 
                              (plot_DLz, DLz_array, "Luminosity distance"), 
                              (plot_DAz, DAz_array, "Angular diameter distance"), 
                              is_log = log_checkbox)
      
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
                plot = plot_graph(width, height, z_array,
                                  (plot_VCz, inputParmsPlot.comoving_volume, "Comoving Volume [Gpc³]"),
                                  is_log = log_checkbox)

                st.pyplot(plot)
                
            
            if plot_tlz:
                
                width = st.slider("Plot width tl(z)", 1, 25, 10)
                height = st.slider("Plot height tl(z)", 1, 25, 5)

                log_checkbox = st.checkbox('Switch to semi-log scale tl(z)')
                
                st.write(" ")

                plot = plot_graph(width, height, z_array, 
                                  (plot_tlz, inputParmsPlot.lookback_time, "Lookback time [Gyr]"),
                                  is_log = log_checkbox)

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
