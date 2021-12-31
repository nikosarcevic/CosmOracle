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
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")

    st.title('Definitions of quantities')
    st.markdown('This page collates the definitions and meaning of the quantities that are computed by CosmΩracle.')
    
    st.markdown('Details can be found in *Distance Measures in Cosmology* by D. Hogg, [astro-ph/9905116](https://arxiv.org/abs/astro-ph/9905116).')

    st.header("Parameters")

    st.subheader("Redshift z")
    st.markdown("The redshift _z_ is the increase in wavelength of electromagnetic radiation as a result of the increase in the cosmological scale factor _a_. It can be computed in terms of the scale factor via the relation")
    st.latex(r'''1 + z = \frac{1}{a},''')
    st.markdown("where it is conventional to take the present value of the scale factor to be equal to 1.")

    st.subheader("Hubble constant H₀")
    st.markdown("The Hubble parameter _H₀_ quantifies the relative expansion of space. It is computed from the scale factor _a_ and its time derivative via the relation")
    st.latex(r'''H = \frac{\dot{a}}{a}.''')

    st.subheader("Energy density")
    st.markdown("The evolution of the scale factor is driven by the energy density of the matter content of the Universe. The dimensionless matter density Ω<sub>M</sub>, photon density Ω<sub>R</sub> and dark energy density Ω<sub>DE</sub> parametrise energy contents of baryonic matter, radiation and dark energy, respectively. A curvature density parameter Ω<sub>K</sub> is defined through the relation", unsafe_allow_html=True)
    st.latex(r'''\Omega_{\rm M} + \Omega_{\rm R} + \Omega_{\rm DE} + \Omega_{\rm K} = 1.''')
    st.markdown("Ω<sub>K</sub> characterises the curvature of space: if Ω<sub>K</sub> < 0, then the Universe has a finite spatial extent. If Ω<sub>K</sub> = 0, then the Universe is spatially flat. If Ω<sub>K</sub> > 0, then the Universe is spatially curved, but infinite in extent.", unsafe_allow_html=True)

    st.subheader("Equation of state parameters")

    st.markdown("The Friedmann equations can only be solved once an equation of state has been imposed. The equation of state relates the energy density and pressure of a given component of the total mass density of the Universe.")
    st.markdown("In order to model the accelerated expansion of the Universe it is convenient to allow the equation of state parameter _w_ to evolve over the course of the Universe's expansion history. A convenient parametrisation in terms of two new parameters _w_₀ and _w_ₐ is")
    st.latex(r'''w(z) = w_0 + w_a\frac{z}{1+z}.''')

    st.header("Distance measures")

    st.subheader("Comoving distance")

    st.markdown("The comoving distance _D_<sub>c</sub> is the distance between two nearby points that move strictly along the Hubble flow. As a result, it is constant in time.", unsafe_allow_html=True)
    st.markdown("The comoving distance can be calculated from the dimensionless Hubble parameter")
    st
    st.latex(r'''E(z) = \sqrt{ \Omega_r(1+z)^4 + \Omega_m(1+z)^3 + \Omega_k(1+z)^2 + \Omega_\Lambda(1+z)^{3(1+w_0+w_a)}e^{-3w_a z/(1+z)},}''')
    st.markdown("in terms of which the comoving distance can be expressed as")
    st.latex(r'''D_{\rm C} = \frac{c}{H_0} \int_0^z\frac{{\rm d}z'}{E(z')}.''')
    st.markdown("The (line-of-sight) comoving distance is the fundamental distance measure in cosmology, as all others are derived from it.")

    st.subheader("Transverse comoving distance")

    st.markdown("The distance between two comoving objects, at equal redshift but separated by an angle _δθ_, in the sky is _D_<sub>M</sub>_δθ_. The quantity _D_<sub>M</sub> is the transverse comoving distance, which can be expressed in terms of the comoving distance _D_<sub>C</sub>:",unsafe_allow_html=True)
    st.latex(r'''D_{\rm M} = D_{\rm C} 
                            \begin{cases}
                            \frac{\sinh\left(\sqrt{\Omega_k}\frac{H_0D_{\rm C}}{c}\right)}{ \sqrt{\Omega_k}\frac{H_0D_{\rm C}}{c}} & \text{ for } \Omega_k > 0,\\
                            1 & \text{ for } \Omega_k = 0,\\
                            \frac{\sin\left(\sqrt{\vert\Omega_k\vert}\frac{H_0D_{\rm C}}{c}\right)}{ \sqrt{\vert\Omega_k\vert}\frac{H_0D_{\rm C}}{c}} & \text{ for } \Omega_k < 0.
                            \end{cases}''')
    st.markdown("The trigonometric functions account for the different spatial geometries.")

    st.subheader("Luminosity distance")
    st.markdown("The luminosity distance _D_<sub>L</sub> is defined by the relationship between bolometric luminosity _L_ and bolometric flux _S_:", unsafe_allow_html=True)
    st.latex(r'''D_{\rm L} = \sqrt{\frac{L}{4\pi S}}.''')
    st.markdown("It is related to the angular diameter distance (and hence the transverse comoving distance) via the relation")
    st.latex(r'''D_{\rm L} = (1+z) D_{\rm M} = (1+z)^2D_{\rm A}.''')


    st.subheader("Angular diameter distance")
    st.markdown("The angular diameter distance _D_<sub>A</sub> is the ratio between an object's physical transverse extension and its angular size. It is expressible in terms of the transverse comoving distance via the relation", unsafe_allow_html=True)
    st.latex(r'''D_{\rm A} = \frac{D_{\rm M}}{1+z}.''')


    st.header("Associated quantities")

    st.subheader("Lookback time")
    st.markdown("The lookback time _t_<sub>L</sub> to an object is the time difference between the moment in which a photon is emitted by this object and the moment in which that photon is observed.", unsafe_allow_html=True)
    st.markdown("If the object of interest is located at redshift _z_ the lookback time can be computed in terms of the function _E(z)_ defined above via the relation")
    st.latex(r'''t_{\rm L}(z) = H_0^{-1}\int_0^z\frac{{\rm d}z'}{(1+z')E(z')}.''')


    st.subheader("Comoving volume")
    st.markdown("The comoving volume _V_<sub>C</sub> is the volume measure in which the density of particles (e.g. galaxies) moving along the Hubble flow is constant with respect to the redshift. The exact form of the comoving volume depends on the geometry; integrated over the whole sky up to redshift _z_, it has the following forms:",unsafe_allow_html=True)
    st.latex(r'''V_{\rm C} = \frac{4\pi}{3}
             \begin{cases}
                \frac{3}{2}\frac{c^3}{H_0^3\Omega_k}\left[\sqrt{1+\Omega_k\left(\frac{H_0D_{\rm M}}{c}\right)^2}-\vert\Omega_k\vert^{-1/2}\sinh^{-1}\left(\vert\Omega_k\vert^{1/2}\frac{H_0D_{\rm M}}{c}\right)\right] & \text{for } \Omega_k > 0,\\ 
                D_\mathrm{M}^3 & \text{for }\Omega_k = 0,\\
                \frac{3}{2}\frac{c^3}{H_0^3\Omega_k}\left[\sqrt{1+\Omega_k\left(\frac{H_0D_{\rm M}}{c}\right)^2}-\vert\Omega_k\vert^{-1/2}\sin^{-1}\left(\vert\Omega_k\vert^{1/2}\frac{H_0 D_{\rm M}}{c}\right)\right] & \text{for } \Omega_k < 0,\\ 
            \end{cases}''')


    return
