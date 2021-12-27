# %%
import numpy as np
import streamlit as st
from scipy import integrate
import background as bg
import matplotlib.pyplot as plt

#Default values
H0=67
ΩM=0.32
ΩR=0
ΩDE=0.68
w0=-1.
wa=0
speed_of_light=2.99792458e5

st.set_page_config(page_title='CosmoCompute')

logo, name = st.sidebar.columns(2)
#with logo:
    #image = 'https://raw.githubusercontent.com/rdzudzar/DistributionAnalyser/main/images/logo_da.png?token=AIAWV2ZRCFKYM42DVFTD3OLAN3CQK'
    #st.image(image, use_column_width=True)
with name:
    st.markdown("<h1 style='text-align: left; color: orange;'> \
                Cosmo \n Compute </h1>", unsafe_allow_html=True)

st.sidebar.write(" ")

z_value = st.sidebar.text_input('Redshift z')
H0_value = st.sidebar.text_input('Hubble Constant H0', str(H0))
ΩM_value = st.sidebar.text_input('Matter Density ΩM', str(ΩM))
ΩDE_value = st.sidebar.text_input('Dark Energy Density ΩΛ', str(ΩDE))
ΩR_value = st.sidebar.text_input('Radiation Density ΩR', str(ΩR))
w0_value = st.sidebar.text_input('w0', str(w0))
wa_value = st.sidebar.text_input('wa', str(wa))

sig_digits = int(st.sidebar.text_input('Significant Digits', str(4)))

# Write About
st.sidebar.header("About")
st.sidebar.warning(
                """
                CosmoCompute app is created and maintained by 
                [**Marco Bonici**](https://github.com/marcobonici), [**Niko Sarcevic**](https://github.com/nikosarcevic) and [**Matthijs van der Wild**](https://github.com/lonbar). If you like this app please star its
                [**GitHub**](https://github.com/nikosarcevic/CosmoCompute/)
                repo, share it and feel free to open an issue if you find a bug 
                or if you want some additional features.
                """)


if z_value:
    st.write('Comoving distance at redshift', z_value, 'is:', str(round(bg.comoving_distance(float(z_value), H0=float(H0_value), ΩM=float(ΩM_value), ΩDE=float(ΩDE_value), ΩR=float(ΩR_value), w0=float(w0_value) , wa=float(wa_value) ), sig_digits)), 'Mpc')
    st.write('Luminosity distance at redshift', z_value, 'is:', str(round(bg.luminosity_distance(float(z_value), H0=float(H0_value), ΩM=float(ΩM_value), ΩDE=float(ΩDE_value), ΩR=float(ΩR_value), w0=float(w0_value) , wa=float(wa_value) ), sig_digits)), 'Mpc')
    st.write('Angular diameter distance at redshift', z_value, 'is:', str(round(bg.angular_diameter_distance(float(z_value), H0=float(H0_value), ΩM=float(ΩM_value), ΩDE=float(ΩDE_value), ΩR=float(ΩR_value), w0=float(w0_value) , wa=float(wa_value) ), sig_digits)), 'Mpc')
    z_array = np.linspace(0, float(z_value), 300)
    
    
    plot_rz = st.checkbox('Plot Comoving Distance Dc')
    plot_DLz = st.checkbox('Plot Luminosity Distance Dl')
    plot_DAz = st.checkbox('Plot Angular Diameter Distance Da')

    if plot_rz or plot_DLz or plot_DAz:
        
        width = st.slider("plot width", 1, 25, 10)
        height = st.slider("plot height", 1, 25, 5)
        
        fig, ax = plt.subplots(figsize=(width, height))
   
        if plot_rz:
            ax.plot(z_array, bg.comoving_distance(z_array, H0=float(H0_value), ΩM=float(ΩM_value), ΩDE=float(ΩDE_value), ΩR=float(ΩR_value), w0=float(w0_value) , wa=float(wa_value) ), 
                    label='Comoving Distance')
        if plot_DLz:
            ax.plot(z_array, bg.luminosity_distance(z_array, H0=float(H0_value), ΩM=float(ΩM_value), ΩDE=float(ΩDE_value), ΩR=float(ΩR_value), w0=float(w0_value) , wa=float(wa_value) ),
                   label='Luminosity Distance')
        if plot_DAz:
            ax.plot(z_array, bg.angular_diameter_distance(z_array, H0=float(H0_value), ΩM=float(ΩM_value), ΩDE=float(ΩDE_value), ΩR=float(ΩR_value), w0=float(w0_value) , wa=float(wa_value) ),
                   label='Angular Diameter Distance')
        

        ax.set_xlabel("REDSHIFT")
        ax.set_ylabel("DISTANCE [MPC]")
        ax.legend()

        st.pyplot(fig)

        st.download_button('Download binary file', z_array)
        
        

    
