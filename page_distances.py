"""
CosmOracleApp
Created December 2021
@authors: 
[Marco Bonici](https://github.com/marcobonici), 
[Niko Sarcevic](https://github.com/nikosarcevic) and 
[Matthijs van der Wild](https://github.com/lonbar)
"""

import streamlit as st
import background as bg

from helpers import plot_graph, get_constants, store_data, get_redshifts

def show_page():

    #Default values
    constants = get_constants()
    speed_of_light=constants['speed-of-light']
    ΩM=constants['matter-density']
    ΩDE=constants['DE-density']
    ΩR=constants['rad-density']
    w0=constants['w0']
    wa=constants['wa']
    H0=constants['Hubble0']

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

        z_array = get_redshifts(float(z_value))

        inputParms = bg.distanceData(z_array, float(H0_value), float(ΩM_value), float(ΩDE_value),
                                     float(ΩR_value), float(w0_value), float(wa_value))

        st.title('Results')

        st.write('The age of the Universe is now', str(round(inputParms.age, sig_digits)), 'Gyrs')
        st.write('Comoving distance at redshift', str(inputParms.redshift[-1]), 'is:',
                 str(round(inputParms.comoving_distance[-1], sig_digits)), 'Mpc')
        st.write('Transverse comoving distance at redshift', str(inputParms.redshift[-1]), 'is:',
                 str(round(inputParms.transverse_comoving_distance[-1], sig_digits)), 'Mpc')
        st.write('Luminosity distance at redshift', str(inputParms.redshift[-1]), 'is:',
                 str(round(inputParms.luminosity_distance[-1], sig_digits)), 'Mpc')
        st.write('Angular diameter distance at redshift', str(inputParms.redshift[-1]), 'is:',
                 str(round(inputParms.angular_diameter_distance[-1], sig_digits)), 'Mpc')
        st.write('An object spanning an angle of 1 arcsec at redshift', str(inputParms.redshift[-1]), 'is therefore',
                 str(round(inputParms.proper_separation[-1], sig_digits)), 'kpc across.')
        st.write('Comoving volume at redshift', str(inputParms.redshift[-1]), 'is:',
                 str(round(inputParms.comoving_volume[-1], sig_digits)), 'Gpc³')
        st.write('Lookback time at redshift', str(inputParms.redshift[-1]), 'is:',
                 str(round(inputParms.lookback_time[-1], sig_digits)), 'Gyrs')
        
       
        rz_array  = inputParms.comoving_distance
        trz_array = inputParms.transverse_comoving_distance
        DLz_array = inputParms.luminosity_distance
        DAz_array = inputParms.angular_diameter_distance
        VCz_array = inputParms.comoving_volume
        tlz_array = inputParms.lookback_time
    
        store_data(inputParms)

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
                                  (plot_VCz, inputParms.comoving_volume, "Comoving Volume"),
                                  axis_label = "Comoving volume [Gpc³]", is_log = log_checkbox)

                st.pyplot(plot)
                
            
            if plot_tlz:
                
                width = st.slider("Plot width tl(z)", 1, 25, 10)
                height = st.slider("Plot height tl(z)", 1, 25, 5)

                log_checkbox = st.checkbox('Switch to semi-log scale tl(z)')
                
                st.write(" ")

                plot = plot_graph(width, height, z_array, 
                                  (plot_tlz, inputParms.lookback_time, "Lookback time"),
                                  axis_label = "Lookback time [Gyr]", is_log = log_checkbox)

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
