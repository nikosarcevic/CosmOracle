![CosmOracle logo](https://github.com/nikosarcevic/CosmOracle/blob/main/images/LogowName.png)

# CosmΩracle


[![Continuous Integration](https://github.com/nikosarcevic/CosmOracle/actions/workflows/main.yaml/badge.svg?branch=main)](https://github.com/nikosarcevic/CosmOracle/actions/workflows/main.yaml)
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/nikosarcevic/cosmoracle/main)
[![DOI](https://zenodo.org/badge/440653118.svg)](https://zenodo.org/badge/latestdoi/440653118)

Consult CosmΩracle at [www.cosmoracle.com](https://www.cosmoracle.com).

---

CosmΩracle aims to be a useful computing aid for people who have a need to know the structure of the universe, and who need this need to be met anywhere, anytime.

Currently, CosmΩracle supports the following features:

## Distance measures in cosmology

In order to let CosmΩracle do some actual computing, select the *Cosmological distances* button in the sidebar.
CosmΩracle will prompt you with fields for a reference redshift and parameters for different cosmologies.
Once you have input your referred set of parameters, CosmΩracle will compute:
- the comoving distance,
- the transverse comoving distance,
- the luminosity distance,
- the angular diameter distance,
- the comoving volume,
- the lookback time,
all evaluated at the redshift of your choice.
In addition, CosmΩracle will compute the physical size of an object spanning an angle of 1'' at your chosen redshift.

## Visual data

Once CosmΩracle has the parameters of your preferred cosmology, you have the option to plot your favorite distance measures over the course of the expansion history of the Universe.
Simply tick the boxes of the distance measure of your choice.
You can set the size of the plot, and CosmΩracle even has the option to plot on a semi-log scale if that is more to your liking!

In addition to the distance measures, CosmΩracle also supports the plotting of associated quantities (currently the comoving volume and lookback time).
To do so, click the dropdown menu below the distance measure plots, and select your quantity of interest.

**But wait; there's more!** In addition to plotting the data directly in CosmΩracle, you can export the data to a text file, to be used at your leisure. 
To export the data, go to the bottom of the page, insert your preferred filename, and click the download button.

## Definitions of quantities

Confused about what CosmΩracle considers to be the luminosity distance? 
Wondering about the difference between the comoving distance and the transverse comoving distance?
Fear not, because CosmΩracle has a list of definitions for each and every one of the quantities that it computes. 
Simply select the *Definitions* button in the sidebar and all definitions will be delivered straight to your screen!

# Contribute

If you like CosmΩracle please star its [GitHub Repo](https://github.com/nikosarcevic/CosmOracle/).
If you run into an bugs or other issues, or want to see additional features, feel free to [open a new issue on GitHub](https://github.com/nikosarcevic/CosmOracle/issues/new/choose).

# Cite

CosmΩracle is registered on Zenodo. 
If you use this calculator while preparing a paper, please use this DOI code to cite our work:
[![DOI](https://zenodo.org/badge/440653118.svg)](https://zenodo.org/badge/latestdoi/440653118)

# References

- D. Hogg, Distance Measures in Cosmology, 2000 [astro-ph/9905116v4](https://arxiv.org/abs/astro-ph/9905116)
- E. V. Linder, Exploring the Expansion History of the Universe, 2002 [astro-ph/0208512](https://arxiv.org/abs/astro-ph/0208512)
