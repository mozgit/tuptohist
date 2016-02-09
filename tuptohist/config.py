"""
Here you may configure behaviour of the package.
"""
from binnings.BinByMonth_2015 import binning #Choose a time binning
Number_Of_Events = 1000 #Choose a number of tracks to proceed from Tuple. Negative values == all tracks
create_pkl = True #Dump dictionaries in .pkl files?
histogram_address = "" #Address for storing histograms
plot_address = "Plots/" #Adress for storing plots