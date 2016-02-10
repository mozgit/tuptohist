"""
Here you may configure behaviour of the package.
"""
#########
#General#
#########
from binnings.NoBinning import binning #Choose a time binning
Number_Of_Events = 1000 #Choose a number of tracks to proceed from Tuple. Negative values == all tracks
pkl_address ="Pkls/" #Address of dumping .pkl with dictionaries
histogram_address = "Histos/" #Address for storing histograms
plot_address = "Plots/" #Adress for storing plots

##################
#Histogram ranges#
##################
UsePredefinedRanges = True
ITMeanRange         = [-0.03, 0.03]
ITWidthRange        = [0.02, 0.06]
ITEffRange          = [0.07, 1.0]

TTMeanRange         = [-0.03, 0.03]
TTWidthRange        = [0.02, 0.06]
TTEffRange          = [0.07, 1.0]
