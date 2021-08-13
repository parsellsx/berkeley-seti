# berkeley-seti
This repository contains Python code and related data files for making a machine learning classifier to categorize variable star light curves from the TESS satellite. I (Alex Parsells) worked on this project with guidance from Daniel Giles (SETI Institute), Ann Marie Cody (SETI Institute), and Steve Croft (UC Berkeley) over 10 weeks in summer 2021 as part of an internship with Berkeley SETI Research Center. This work was supported by the National Science Foundation through its Research Experiences for Undergraduates (REU) program.

## Project Background and Related Work
The goal of this project is to develop a machine learning (ML) model that can automatically classify TESS light curves into their respective variable star categories. Such a classifier can then be used in conjunction with an anomaly detection pipeline (see Giles & Walkowicz, 2020) which is designed to take in thousands of light curves and flag any whose brightness patterns seem "weird" or unusual. Those light curves can then be passed into a well-trained classifier to see if it identifies them as members of a particular variable star class, or if it can't determine a likely class. In the latter case, the stars in question might be well-suited for follow-up observation to determine if they are in fact members of a rare variable type, a totally new variable type, or even candidates to have transiting megastructures (e.g., Dyson spheres) built by extraterrestrial intelligence in orbit around them. Searching for stars in this last category is the SETI relevance of this project.

## My Work in Summer 2021


## How to Use this Repository
Code is stored in Jupyter Notebooks in one of two directories: notebooks_streamlined and notebooks_messy. The notebooks_streamlined folder contains the core code required to reproduce my results and can be easily modified to add new experiments. The notebooks_messy folder contains most of the same notebooks, but as I originally wrote them, with few or no modifications. As such, these notebooks contain all of my false starts/dead ends in trying to achieve a particular goal, as well as many notes I took while acquiring data, training models, etc. I include them so that if something in the streamlined notebooks is unclear or someone wants to know exactly the thought process I went through in deciding to do something a certain way, they can find that out.

Each directory in the repository has its own README.md file which describes in more detail the files in that directory. Here are the general contents of each directory:
* __catalogs__ contains raw (unmodified) data files downloaded from astronomical research papers that catalog eclipsing binaries. These files include keplerebs_villanova_complete.csv, which with some modifications (see the __input_data__ directory) is the primary set of EBs I used to train models
* __input_data__ contains modified versions of the data files in __catalogs__. 

## References
1. Giles & Walkowicz, 2020
