# %%
import numpy as np
import streamlit as st
from scipy import integrate
import background as bg
import matplotlib.pyplot as plt


#import plotly.figure_factory as ff



# This code is different for each deployed app.
CURRENT_THEME = "blue"
IS_DARK_THEME = True
EXPANDER_TEXT = """
    This is a custom theme. You can enable it by copying the following code
    to `.streamlit/config.toml`:
    ```python
    [theme]
    primaryColor = "#E694FF"
    backgroundColor = "#00172B"
    secondaryBackgroundColor = "#0083B8"
    textColor = "#C6CDD4"
    font = "sans-serif"
    ```
    """


# This code is the same for each deployed app.
st.image(
    "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/271/artist-palette_1f3a8.png",
    width=100,
)

"""
# Try out Theming!
Click on the images below to view this app with different themes. 
"""

""

THEMES = [
    "light",
    "dark",
    "green",
    "blue",
]
GITHUB_OWNER = "nikosarcevic"

# Show thumbnails for available themes.
# As html img tags here, so we can add links on them.
cols = st.beta_columns(len(THEMES))
for col, theme in zip(cols, THEMES):

    # Get repo name for this theme (to link to correct deployed app)-
    if theme == "light":
        repo = "theming-showcase"
    else:
        repo = f"theming-showcase-{theme}"

    # Set border of current theme to red, otherwise black or white
    if theme == CURRENT_THEME:
        border_color = "red"
    else:
        border_color = "lightgrey" if IS_DARK_THEME else "black"

    col.markdown(
        #f'<p align=center><a href="https://share.streamlit.io/{GITHUB_OWNER}/{repo}/main"><img style="border: 1px solid {border_color}" alt="{theme}" src="https://raw.githubusercontent.com/{GITHUB_OWNER}/theming-showcase/main/thumbnails/{theme}.png" width=150></a></p>',
        f'<p align=center><a href="https://apps.streamlitusercontent.com/{GITHUB_OWNER}/{repo}/main/streamlit_app.py/+/"><img style="border: 1px solid {border_color}" alt="{theme}" src="https://raw.githubusercontent.com/{GITHUB_OWNER}/theming-showcase/main/thumbnails/{theme}.png" width=150></a></p>',
        unsafe_allow_html=True,
    )
    if theme in ["light", "dark"]:
        theme_descriptor = theme.capitalize() + " theme"
    else:
        theme_descriptor = "Custom theme"
    col.write(f"<p align=center>{theme_descriptor}</p>", unsafe_allow_html=True)


""
with st.beta_expander("Not loading?"):
    st.write(
        "You probably played around with themes before and overrode this app's theme. Go to ☰ -> Settings -> Theme and select *Custom Theme*."
    )
with st.beta_expander("How can I use this theme in my app?"):
    st.write(EXPANDER_TEXT)

""
""

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

    rz_array = bg.comoving_distance(z_array, H0=float(H0_value), ΩM=float(ΩM_value), ΩDE=float(ΩDE_value), ΩR=float(ΩR_value), w0=float(w0_value) , wa=float(wa_value) )
    DLz_array = bg.luminosity_distance(z_array, H0=float(H0_value), ΩM=float(ΩM_value), ΩDE=float(ΩDE_value), ΩR=float(ΩR_value), w0=float(w0_value) , wa=float(wa_value) )
    DAz_array = bg.angular_diameter_distance(z_array, H0=float(H0_value), ΩM=float(ΩM_value), ΩDE=float(ΩDE_value), ΩR=float(ΩR_value), w0=float(w0_value) , wa=float(wa_value) )
    
    stacked_array = np.vstack((z_array, rz_array, DLz_array, DAz_array)).T
    np.savetxt("output.txt", stacked_array, header='z, rz, DLz, DAz')

    plot_rz = st.checkbox('Plot Comoving Distance Dc')
    plot_DLz = st.checkbox('Plot Luminosity Distance Dl')
    plot_DAz = st.checkbox('Plot Angular Diameter Distance Da')

    if plot_rz or plot_DLz or plot_DAz:
        
        width = st.slider("plot width", 1, 25, 10)
        height = st.slider("plot height", 1, 25, 5)
        
        fig, ax = plt.subplots(figsize=(width, height))
   
        if plot_rz:
            ax.plot(z_array, rz_array, label='Comoving Distance')
        if plot_DLz:
            ax.plot(z_array, DLz_array, label='Luminosity Distance')
        if plot_DAz:
            ax.plot(z_array, DAz_array, label='Angular Diameter Distance')
        

        ax.set_xlabel("REDSHIFT")
        ax.set_ylabel("DISTANCE [MPC]")
        ax.legend()

        st.pyplot(fig)

    f = open("output.txt", encoding = 'utf-8')
    file_name = st.text_input('Filename', "filename.txt")
    st.download_button('Download text file', f, file_name = file_name)
        
        

    
