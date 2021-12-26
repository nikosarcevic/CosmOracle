# %%
import numpy as np
import streamlit as st
from scipy import integrate
import background as bg
import matplotlib.pyplot as plt

plt.rcParams.update({
    'text.usetex': True,
    'text.latex.preamble': r'\usepackage{bm} \usepackage{booktabs}',
    'legend.loc' : "best", 'font.weight' : "bold",
    
})

H0=67
ΩM=0.32
ΩR=0
ΩDE=0.68
w0=-1.
wa=0
speed_of_light=2.99792458e5

st.set_page_config(page_title='CosmoCalc')

logo, name = st.sidebar.columns(2)
#with logo:
    #image = 'https://raw.githubusercontent.com/rdzudzar/DistributionAnalyser/main/images/logo_da.png?token=AIAWV2ZRCFKYM42DVFTD3OLAN3CQK'
    #st.image(image, use_column_width=True)
with name:
    st.markdown("<h1 style='text-align: left; color: orange;'> \
                CosmoCalc </h1>", unsafe_allow_html=True)

st.sidebar.write(" ")





#distance_value = st.sidebar.text_input('Distance') 

z_value = st.sidebar.text_input('Redshift')
H0_value = st.sidebar.text_input('Hubble', str(H0))
ΩM_value = st.sidebar.text_input('Matter Density', str(ΩM))
ΩDE_value = st.sidebar.text_input('Dark Energy Density', str(ΩDE))
ΩR_value = st.sidebar.text_input('Radiation Density', str(ΩR))
w0_value = st.sidebar.text_input('w0', str(w0))
wa_value = st.sidebar.text_input('wa', str(wa))

sig_digits = int(st.sidebar.text_input('Significant Digits', str(4)))

  


# Write About
st.sidebar.header("About")
st.sidebar.warning(
                """
                CosmoCalc app is created and maintained by 
                **Marco Bonici, Niko Sarcevic and Matthijs van der Wild**. If you like this app please star its
                [**GitHub**](ADD URL HERE)
                repo, share it and feel free to open an issue if you find a bug 
                or if you want some additional features.
                """)




#if distance_value :
    #st.write('The distance modulus is:', round(bg.calculate_distance_modulus(float(distance_value)), sig_digits), '[no units]')
    
 

if z_value:
    st.write('comoving distance is:', round(bg.comoving_distance(float(z_value), H0=float(H0_value), ΩM=float(ΩM_value), ΩDE=float(ΩDE_value), ΩR=float(ΩR_value), w0=float(w0_value) , wa=float(wa_value) ), sig_digits), 'Mpc')
    z_array = np.linspace(0,float(z_value), 300)
    fig, ax = plt.subplots()
    ax.plot(z_array, bg.comoving_distance(float(z_array), H0=float(H0_value), ΩM=float(ΩM_value), ΩDE=float(ΩDE_value), ΩR=float(ΩR_value), w0=float(w0_value) , wa=float(wa_value) ))
    ax.xlabel(r"$z$")
    ax.ylabel(r"$r(z)$")
    st.pyplot(fig)

    
