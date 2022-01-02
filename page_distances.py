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
#import background as bg
import matplotlib.pyplot as plt
import plot_script as ps
import classes

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

        inputParms = classes.distanceParms(float(z_value), float(H0_value), float(ΩM_value), 
                                   float(ΩDE_value), float(ΩR_value), float(w0_value), float(wa_value))

        st.title('Results')
        st.write('Comoving distance at redshift', str(inputParms.redshift), 'is:', 
                 str(round(inputParms.comovingDistance(), sig_digits)), 'Mpc')
        st.write('Transverse comoving distance at redshift', str(inputParms.redshift), 'is:', 
                 str(round(inputParms.transverseComovingDistance(), sig_digits)), 'Mpc')
        st.write('Luminosity distance at redshift', str(inputParms.redshift), 'is:', 
                 str(round(inputParms.luminosityDistance(), sig_digits)), 'Mpc')
        st.write('Angular diameter distance at redshift', str(inputParms.redshift), 'is:', 
                 str(round(inputParms.angularDiameterDistance(), sig_digits)), 'Mpc')
        st.write('An object spanning an angle of 1 arcsec at redshift', str(inputParms.redshift), 'is therefore', 
                 str(round(inputParms.properSeparation(), sig_digits)), 'kpc across.')
        st.write('Comoving volume at redshift', str(inputParms.redshift), 'is:', 
                 str(round(inputParms.comovingVolume(), sig_digits)), 'Gpc³')
        st.write('Lookback time at redshift', str(inputParms.redshift), 'is:', 
                 str(round(inputParms.lookbackTime(), sig_digits)), 'Gyrs')
        
        z_array = np.linspace(0, inputParms.redshift, 300)

        inputParmsPlot = classes.distanceParms(z_array, float(H0_value), float(ΩM_value), float(ΩDE_value), 
                                       float(ΩR_value), float(w0_value), float(wa_value))

        rz_array = inputParmsPlot.comovingDistance()
        trz_array = inputParmsPlot.transverseComovingDistance()
        DLz_array = inputParmsPlot.luminosityDistance()
        DAz_array = inputParmsPlot.angularDiameterDistance()
        VCz_array = inputParmsPlot.comovingVolume()
        tlz_array = inputParmsPlot.lookbackTime()
    
        stacked_array = np.vstack((inputParmsPlot.redshift, 
                                   inputParmsPlot.comovingDistance(), 
                                   inputParmsPlot.transverseComovingDistance(), 
                                   inputParmsPlot.luminosityDistance(), 
                                   inputParmsPlot.angularDiameterDistance(), 
                                   inputParmsPlot.comovingVolume(), 
                                   inputParmsPlot.lookbackTime())).T
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

                width = st.slider("Plot width Vcz", 1, 25, 10)
                height = st.slider("lot height Vcz", 1, 25, 5)

                log_checkbox = st.checkbox('Switch to semi-log scale Vc(z)')
                
                st.write(" ")

                plot = ps.plot_comoving_volume_lin(plot_VCz, 
                                                   inputParmsPlot.redshift, 
                                                   inputParmsPlot.comovingVolume(), 
                                                   width, 
                                                   height)
                if log_checkbox:
                    plot = ps.plot_comoving_volume_log(plot_VCz, 
                                                       inputParmsPlot.redshift,
                                                       inputParmsPlot.comovingVolume(),
                                                       width, 
                                                       height)

                st.pyplot(plot)
                
            
            if plot_tlz:
                
                width = st.slider("Plot width tlz", 1, 25, 10)
                height = st.slider("Plot height tlz", 1, 25, 5)

                log_checkbox = st.checkbox('Switch to semi-log scale tl(z)')
                
                st.write(" ")

                plot = ps.plot_lookback_time_lin(plot_tlz, 
                                                 inputParmsPlot.redshift,
                                                 inputParmsPlot.lookbackTime(), 
                                                 width, 
                                                 height)
                if log_checkbox:
                    plot = ps.plot_lookback_time_log(plot_tlz, 
                                                     inputParmsPlot.redshift, 
                                                     inputParmsPlot.lookbackTime(), 
                                                     width, 
                                                     height)

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
