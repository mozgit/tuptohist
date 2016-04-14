"""
Here you may configure behaviour of the package.
"""
#########
#General#
#########
#from binnings.NoBinning_2015 import binning #Choose a time binning
#from binnings.NoBinning_2015 import bin_name #Choose a time binning
from binnings.NoBinning_2012 import binning #Choose a time binning
from binnings.NoBinning_2012 import bin_name #Choose a time binning
#from binnings.BinByMonth_2012 import binning #Choose a time binning
#from binnings.BinByMonth_2012 import bin_name #Choose a time binning
#from binnings.BinByMonth_2015 import binning #Choose a time binning
#from binnings.BinByMonth_2015 import bin_name #Choose a time binning
#from binnings.BinByAlignmentVersions_2015 import binning #Choose a time binning
#from binnings.BinByAlignmentVersions_2015 import bin_name #Choose a time binning


Number_Of_Events = -1 #Choose a number of tracks to proceed from Tuple. Negative values == all tracks
pkl_address ="Pkls/" #Address of dumping .pkl with dictionaries
histogram_address = "Histos/" #Address for storing histograms
plot_address = "Plots/" #Adress for storing plots
residual_limit = 0.5 #limit of residual histograms, in mm.
residual_nBins = 100 #number of bins in residual histograms
dead_sectors = ['IT1BottomX2Sector7', 'IT3TopX1Sector7']

##################
#Histogram ranges#
##################
UsePredefinedRanges = True
ITMeanRange         = [-0.06, 0.06]
ITWidthRange        = [0.044, 0.058]
ITEffRange          = [0.995, 1.0]

TTMeanRange         = [-0.06, 0.06]
TTWidthRange        = [0.03, 0.06]
TTEffRange          = [0.98, 1.0]

##################
#Histogram Titles#
##################
UsePredefinedTitles = True
IncudeMissingSectorsToSummary = False
nBins_in_summary = 30

ITMeanTitle = "Residual bias distribution [mm], 2012"
ITWidthTitle = "Residual width distribution [mm], 2012"
ITEffTitle = "Hit detection efficiency distribution, 2012"

TTMeanTitle =  "Residual bias distribution [mm], 2012"
TTWidthTitle =  "Residual width distribution [mm], 2012"
TTEffTitle =  "Hit detection efficiency distribution, 2012"


###################################################
#Dependence of efficiency from search window study#
###################################################
perform_window_eff_study = True
efficiency_windows = [0.01, 0.025, 0.05, 0.075, 0.1, 0.2, 0.3]