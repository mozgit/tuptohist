# tuptohist package

##Analysing output of STTrackTuple

This is python-based framework for analysis of ST perofromance tuples obtained from STTrackTuple monitor.
Tuples may be processed with TupToHist.py script:

```
python TupToHist.py <tuple_name>.root <mode>
```
where mode is a flag indicating what type of a histograms is desired:

1 - IT Hit Monitor mode. As an putput you will have histograms of residuals per-sector in time bins stored in .root file and  2D plots of bias and resolution
2 - TT Hit Monitor mode. As an putput you will have histograms of residuals per-sector in time bins stored in .root file and  2D plots of bias and resolution
3 - TT Hit efficiency mode.  As an putput you will have histograms of hit efficiency per-sector in time bins stored in .root file and  2D plots of hit efficiency
4 - TT Hit efficiency mode.  As an putput you will have histograms of hit efficiency per-sector in time bins stored in .root file and  2D plots of hit efficiency

In addition, all modes will create trend histograms of values of inerest, which shows variation of this value for each sector in time bins.
Plus, .pkl file will be created. This fille allows to redo 2D plots woth PklToHist function if needed. This might be usefull, since processing of original tuple file requires some time. It should be noted, that time binning is already included in .pkl files, so if you need to reanalyze yout data with other time bins, TupToHist function.

All configurables of this package are stored in config.py file. While most of the variables are quite self-explainatory, you may pay an attention on ``binning'' variable. This variable defines time binnning which will be used for processing the data. Some of the binnings are collected in binning/ folder, so you may choose from there or add your own.

Please make sure that you have directories to store outputs of the functions. Default directories are presented in config.py.

##Making 2D plots

This package also has functions creating 2D maps of IT and TT. These functions are stored in drawing/ folder. The main scripts which you will want to run are Create{IT,TT}Hist.py. Corresponding fuctions are docimented in a code.
