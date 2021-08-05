import numpy as np
import matplotlib.pyplot as plt
import astropy
import pandas as pd
import os
import time
import itertools
import lightkurve as lk
import pickle

# Mount the GCP filesystem onto this VM
data_dir = "/home/parsellsx/tesslcs/"
os.system(f"gcsfuse --implicit-dirs tess-goddard-lcs {data_dir}")

# Note that 'skipinitialspace=True' makes it so that the space at the start of the TIC ID in the file doesn't 
# make pandas interpret it as a NaN. Also, index_col=False makes it not interpret the TIC ID column as indices
# and instead treats it as actual data (which it is)
justesen = pd.read_table('justesen_albrecht_table2_748ebs.txt',sep=' ',header=None,
                     names=['TIC ID','Period','t1','t2','ecosw','d1','d2','Tmag'],index_col=False,skiprows=21,
                    skipinitialspace=True)
good_mags = np.where(np.logical_and(justesen['Tmag'] > 10, justesen['Tmag'] < 15))[0]
tessebs = pd.read_csv('tess_ebs_villanova_tmag_10-15.csv',header=None,names=['TIC ID','Signal ID','BJD0','BJD0_uncert','Period','Period_uncert','Morph','Morph_dist','RA','Dec','Tmag','GLon','GLat','Teff','Log g','Abundance'],index_col=False,skiprows=1)

lookuplist = [] # List to hold all the dataframes
names = ['filename','RA','dec','TIC ID','sector','camera','CCD','mag']
for i in range(1,27):
    print(i)
    lookup = pd.read_csv('~/tesslcs/sector' + str(i) + 'lookup.csv',header=None,names=names,index_col=False,
                        skiprows=1,usecols=['filename','TIC ID'],dtype=str)
    lookuplist.append(lookup)

def TICID_to_filepath(TICID,lookuplist=lookuplist):
    # Takes in a TIC ID, searches the GCP bucket for any corresponding filepaths (could be multiple) and returns
    # a list (which can be empty) containing all such filepaths.
    id_filelist = [] 
    search_str = '_' + str(TICID) + '.pkl' # This is the string we'll actually look for in lookuplist, our df list
    # We include the underscore in search_str to avoid getting other TIC IDs that contain the TIC ID we're looking
    # for but have another digit in front of it
    for i in range(0,26): # Loop through every dataframe in lookuplist (i.e., every lookup table file)
        for j in lookuplist[i]['filename']:
            if search_str in j:
                id_filelist.append(j)
    return id_filelist

filelist = [] # This will hold all the filepaths to the light curves corresponding to our catalog TIC IDs
# Our two data "sets" that we want to iterate through right now are justesen['TIC ID'][good_mags] and 
# tessebs['TIC ID']. We'll count the number of stars that are found in our GCP bucket LCs and compare that to the
# number of stars in the catalog as well as the final size of filelist (which will depend on how many LCs exist
# for a single star on average)
for ind, i in enumerate(justesen['TIC ID'][good_mags]):
    if ind % 10 == 0:
        print(ind)
    filelist.extend(TICID_to_filepath(i)) # Get the filepath(s) for this TIC ID, then append to our list of paths
for ind, i in enumerate(tessebs['TIC ID']):
    if ind % 10 == 0:
        print(ind)
    filelist.extend(TICID_to_filepath(i))
# Now write filelist to a text file so we have it for later. Remember these are all EBs. Remember also that we
# haven't filtered out duplicates yet
with open('eb_filepath_list_justesen_tessebs_with_duplicates.txt', 'w') as f:
    for item in filelist:
        f.write("%s\n" % item)
print(len(filelist))
print("We put in 2596 TIC IDs")