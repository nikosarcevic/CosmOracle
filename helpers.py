import io
import matplotlib.pyplot as plt
import yaml
import numpy as np
import streamlit as st

from scipy import integrate
from pathlib import Path
from itertools import cycle

def get_constants():
    '''
    Load the constants from YAML file
    '''
    with open("cosmology-constants.yaml", "r") as f:
        constants = yaml.load(f, Loader=yaml.FullLoader)
    return constants['constants']

def get_parametersets():
    '''
    Load a list of the parameter sets available in YAML file
    '''
    with open("cosmology-constants.yaml", "r") as f:
        constants = yaml.load(f, Loader=yaml.FullLoader)
        parameterset = constants['cosmologies'].keys()
    return parameterset

def get_cosmologies(dataset):
    '''
    Load the default parameters from YAML file
    '''
    with open("cosmology-constants.yaml", "r") as f:
        constants = yaml.load(f, Loader=yaml.FullLoader)
        if dataset not in constants['cosmologies'].keys():
            error = f'''{dataset} is not a valid dataset. 
                         Possible choices are:
                         {constants['cosmologies'].keys()}.'''
            ValueError(error)
    return constants['cosmologies'][dataset]

def get_redshifts(z_max):
    '''
    takes a redshift value and returns a redshift interval
    '''
    if not (isinstance(z_max, int) or isinstance(z_max, float)):
            TypeError("Enter a valid redshift.")
    return np.linspace(0, z_max, 300)

def store_data(params):
    '''
    Takes a set of data and stores it in a file
    '''

    stacked_array = np.vstack((params.redshift,
                               params.comoving_distance,
                               params.transverse_comoving_distance,
                               params.luminosity_distance,
                               params.angular_diameter_distance,
                               params.comoving_volume,
                               params.lookback_time)).T
    np.savetxt("output.txt", stacked_array, header='z,DCz [Mpc],DMz [Mpc],DLz [Mpc],DAz [Mpc],VCz [Gpc^3],tlz [Gyr]', delimiter=',', comments='')

def read_markdown(markdown_file):
        return Path(markdown_file).read_text()

def read_eq(equation_file):
        return Path(equation_file).read_text()

def save_plot_to_memory():
    '''
    store the plot in memory to prepare for download
    '''
    filename = "plot.pdf"
    image = io.BytesIO()
    plt.savefig(image, format="pdf")

    return image, filename

def plot_graph(width, height, 
               redshifts, *args, 
               axis_label = "Distance [Mpc]", is_log = False): 
    '''
    Plot the calculated distances as a function of redshift in a linear scale.
    '''
    
    fig, ax = plt.subplots(figsize=(width, height))
    
    colors = {
     'orange' : '#ffc345',
     'gray'   : '#333333',
     'white'  : '#FFFFFF',
    }
    
    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_color(colors['orange'])
        ax.spines[axis].set_linewidth(3)

    ax.tick_params(axis='x', colors=colors['orange'])
    ax.tick_params(axis='y', colors=colors['orange'])
    ax.tick_params(width=3)
    ax.tick_params(axis='both', labelsize=12)    

    ax.yaxis.label.set_color(colors['orange'])
    ax.xaxis.label.set_color(colors['orange'])
    
    ax.set_facecolor(colors['white'])
    fig.patch.set_facecolor(colors['white'])
    
    linestyle = cycle(('-', '-.', '--', ':'))
    for graph in args:
        if graph[0]:
            ax.plot(redshifts, 
                    graph[1], 
                    label=graph[2], 
                    color=colors['gray'], 
                    ls=next(linestyle), 
                    lw=3)
    
    legend = plt.legend(frameon = 1)
    plt.setp(legend.get_texts(), color=colors['gray'])
    frame = legend.get_frame()
    frame.set_facecolor(colors['white'])
    frame.set_edgecolor(colors['white'])
    
    if is_log:
        ax.set_yscale('log')
    ax.set_xlabel('Redshift', size=15)
    ax.set_ylabel(axis_label, size=15)
    
    return fig

def integration_wrapper(integrand, upper_limit):
    """
    Integrates a given function of a single variable from 0 to upper_limit
    """
    result = integrate.quad(integrand, 0, upper_limit,
                            epsabs = 1e-12, epsrel = 1e-12, limit = 100)[0]
    return result

def check_redshift_valid_array(redshift):
    """
    Ensures that the given redshift is either a float/integer ≥ 0,
    or a numpy array of floats/integers each of which ≥ 0
    """
    if isinstance(redshift, float) or isinstance(redshift, int):
        is_array = False
        if redshift < 0:
            raise ValueError("Enter a non-negative redshift.")
    elif isinstance(redshift, np.ndarray):
        is_array = True
        if any(t < 0 for t in redshift):
            raise ValueError("Enter a non-negative redshift.")
    else:
        raise TypeError(f'Expected "Union[float, int, np.ndarray]", got {type(redshift)}')
    return is_array

def add_colophon():
    about = read_markdown("docs/markdown/about.md")
    st.sidebar.markdown(about)

def add_logo():
    """
    Temporary workaround for placing the CosmΩracle logo, until Streamlit resolves their
    markdown issue in multiple pages. See https://github.com/streamlit/streamlit/issues/4848
    """
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://github.com/nikosarcevic/CosmOracle/blob/main/images/LogowName.png?raw=true);
                background-repeat: no-repeat;
                background-size: contain;
                padding-top: 130px;
                padding-bottom: 30px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
