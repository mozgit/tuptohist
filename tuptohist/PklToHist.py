import os
import inspect
from pprint import pprint
from itertools import product
import math
import numpy as n
import sys
import pickle
from datetime import datetime
from suppl.Structure import *
from drawing.CreateTTHist import CreateTTHist
from drawing.CreateITHist import CreateITHist
from config import binning
from config import histogram_address
from config import plot_address
import ROOT as R
from ROOT import gStyle
gStyle.SetOptStat(False)
#from ROOT import RooFit as RF


def PklToHist(data, oparation_mode, histogram_address=histogram_address, plot_address=plot_address):
    if (oparation_mode=='1'):
        print "Opening file "+data+"  (it may take several minutes)"
        start = datetime.now()
        with open(data, 'r') as basket:
            coll_ITHitMonitor = pickle.load(basket)
        print "File oppened (took  "+str(datetime.now()-start)+" ) \nCreating 2D plots"
        for run_bin in coll_ITHitMonitor:
            try:
                suffix =coll_ITHitMonitor[run_bin]["comment"].replace(" ","_")
            except:
                suffix =str(coll_ITHitMonitor[run_bin]["run_start"])+"__"+str(coll_ITHitMonitor[run_bin]["run_stop"])
            CreateITHist(coll_ITHitMonitor[run_bin]["data"],variable=unbiased_residual, mode="Mean",suffix = suffix, address=plot_address)
            CreateITHist(coll_ITHitMonitor[run_bin]["data"],variable=unbiased_residual, mode="Sigma",suffix = suffix, address=plot_address)
        print "2D plots created, writing histograms to .root file"            
        write_histogram(coll_ITHitMonitor, "Monitor", histogram_address+"ITHitMonitor")
        print "Histograms saved, creating trends"
        create_monitor_trends(coll_ITHitMonitor, "IT", histogram_address+"Trends_ITHitMonitor")
    
    elif (oparation_mode=='2'):
        print "Opening file "+data+"  (it may take several minutes)"
        start = datetime.now()
        with open(data, 'r') as basket:
            coll_TTHitMonitor = pickle.load(basket)
        print "File oppened (took  "+str(datetime.now()-start)+" ) \nCreating 2D plots"
        for run_bin in coll_TTHitMonitor:
            try:
                suffix = coll_TTHitMonitor[run_bin]['comment'].replace(" ","_")
            except:
                suffix = str(coll_TTHitMonitor[run_bin]["run_start"])+"__"+str(coll_TTHitMonitor[run_bin]["run_stop"])
            CreateTTHist(coll_TTHitMonitor[run_bin]["data"],variable=unbiased_residual, mode="Mean",suffix= suffix,address=plot_address)
            CreateTTHist(coll_TTHitMonitor[run_bin]["data"],variable=unbiased_residual, mode="Sigma",suffix=suffix,address=plot_address)
        print "2D plots created, writing histograms to .root file"            
        write_histogram(coll_TTHitMonitor, "Monitor",histogram_address+"TTHitMonitor")
        print "Histograms saved, creating trends"
        create_monitor_trends(coll_TTHitMonitor, "TT",histogram_address+"Trends_TTHitMonitor")
    
    elif (oparation_mode=='3'):
        print "Opening file "+data+"  (it may take several minutes)"
        start = datetime.now()
        with open(data, 'r') as basket:
            coll_TTHitEfficiency = pickle.load(basket)
        print "File oppened (took  "+str(datetime.now()-start)+" ) \nCreating 2D plots"
        for run_bin in coll_TTHitEfficiency:
            try:
                suffix = coll_TTHitEfficiency[run_bin]["comment"]
            except:
                suffix = str(coll_TTHitEfficiency[run_bin]["run_start"])+"__"+str(coll_TTHitEfficiency[run_bin]["run_stop"])
            CreateTTHist(coll_TTHitEfficiency[run_bin]["data"],variable = efficiency, mode="Eff",suffix=suffix,address=plot_address)
        print "2D plots created, writing histograms to .root file"            
        write_histogram(coll_TTHitEfficiency, "Efficiency",histogram_address+"TTHitEfficiency")
        print "Histograms saved, creating trends"
        create_efficiency_trends(coll_TTHitEfficiency, "TT",histogram_address+"Trends_TTHitEfficiency")
    
    elif (oparation_mode=='4'):
        print "Opening file "+data+"  (it may take several minutes)"
        start = datetime.now()
        with open(data, 'r') as basket:
            coll_ITHitEfficiency = pickle.load(basket)
        print "File oppened (took  "+str(datetime.now()-start)+" ) \nCreating 2D plots"
        for run_bin in coll_ITHitEfficiency:
            try:
                suffix = coll_ITHitEfficiency[run_bin]["comment"]
            except:
                suffix = str(coll_ITHitEfficiency[run_bin]["run_start"])+"__"+str(coll_ITHitEfficiency[run_bin]["run_stop"])
            CreateITHist(coll_ITHitEfficiency[run_bin]["data"],variable = efficiency, mode="Eff",suffix=suffix, address=plot_address)
        print "2D plots created, writing histograms to .root file"            
        write_histogram(coll_ITHitEfficiency, "Efficiency",histogram_address+"ITHitEfficiency")
        print "Histograms saved, creating trends"
        create_efficiency_trends(coll_ITHitEfficiency, "IT",histogram_address+"Trends_ITHitEfficiency")
    
    else:
        print "To run scipt, choose the mode you want to run:"
        print "1 - IT Hit Monitor"
        print "2 - TT Hit Monitor"
        print "3 - TT Hit Efficiency"
        print "4 - IT Hit Efficiency"

    return True


if __name__ == "__main__":
    #local_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    if len(sys.argv)==3:
        data = sys.argv[1]
        try:
            PklToHist(data,sys.argv[2])
        except:
            syntax_explanation("PklToHist.py")
    else:
        syntax_explanation("PklToHist.py")
       
