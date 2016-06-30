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
from drawing.Create_Maps import TT_Map as TT_Map_func
from drawing.Create_Maps import IT_Map as IT_Map_func
from config import binning
from config import bin_name
from config import perform_window_eff_study
from config import Number_Of_Events
from config import histogram_address
from config import plot_address
from config import pkl_address
import ROOT as R
from ROOT import gStyle
gStyle.SetOptStat(False)
#from ROOT import RooFit as RF

binning
bin_name

def TupToHist(data, oparation_mode, Number_Of_Events=Number_Of_Events, pkl_address=pkl_address, histogram_address=histogram_address, plot_address=plot_address):
    global perform_window_eff_study

    IT_Map=IT_Map_func()
    TT_Map=TT_Map_func()
    f_input = R.TFile(data)
    start = datetime.now()
    
    if (oparation_mode=='1'):
        tree_ITHitMonitor = f_input.ITHitMonitor
        t_ITHitMonitor = tree_ITHitMonitor.Get("TrackMonTuple")
        coll_ITHitMonitor = create_coll(det = "IT", mode = "Monitor")
        print "IT Monitor"
        for i, s in enumerate(t_ITHitMonitor):
            if i%100==0:
                cli_progress_test(i, t_ITHitMonitor.GetEntries(), start)
            if Number_Of_Events>0:
                if i>Number_Of_Events: continue
            for hit in range(0,s.len):
                for run_bin in coll_ITHitMonitor:
                    if ((s.RunNumber>=coll_ITHitMonitor[run_bin]["run_start"]) and (s.RunNumber<=coll_ITHitMonitor[run_bin]["run_stop"])):
                        coll_ITHitMonitor[run_bin]["data"][s.clusterSTchanMapID[hit]]["residual"].Fill(s.hit_residual[hit])
                        coll_ITHitMonitor[run_bin]["data"][s.clusterSTchanMapID[hit]]["errMeasure"].append(s.hit_errMeasure[hit])
                        coll_ITHitMonitor[run_bin]["data"][s.clusterSTchanMapID[hit]]["errResidual"].append(s.hit_errResidual[hit])
                        coll_ITHitMonitor[run_bin]["data"][s.clusterSTchanMapID[hit]]["unbiased_residual"].Fill(s.hit_residual[hit]*(abs(s.hit_errMeasure[hit]/s.hit_errResidual[hit])**2))
                        coll_ITHitMonitor[run_bin]["data"][s.clusterSTchanMapID[hit]]["rms_unbiased_residual"].Fill(s.hit_residual[hit]*abs(s.hit_errMeasure[hit]/s.hit_errResidual[hit]))
        write_histogram(coll_ITHitMonitor, "Monitor", histogram_address+"ITHitMonitor"+"__"+bin_name+"_")                        
        coll_ITHitMonitor = make_coll_lite(coll = coll_ITHitMonitor, det = "IT", mode = "Monitor")
        for run_bin in coll_ITHitMonitor:
            try:
                suffix =coll_ITHitMonitor[run_bin]["comment"].replace(" ","_")
            except:
                suffix =str(coll_ITHitMonitor[run_bin]["run_start"])+"__"+str(coll_ITHitMonitor[run_bin]["run_stop"])
            CreateITHist(coll_ITHitMonitor[run_bin]["data"], variable = "mean", mode="Value",suffix = suffix, address=plot_address)
            CreateITHist(coll_ITHitMonitor[run_bin]["data"], variable = "width", mode="Value",suffix = suffix, address=plot_address)
        with open(pkl_address+'ITHitMonitor_'+bin_name+'.pkl', 'wb') as basket:
            pickle.dump(coll_ITHitMonitor, basket)
        create_monitor_trends(coll_ITHitMonitor, "IT", histogram_address+"Trends_ITHitMonitor"+"__"+bin_name+"_")
    
    elif (oparation_mode=='2'):
        tree_TTHitMonitor = f_input.TTHitMonitor
        t_TTHitMonitor = tree_TTHitMonitor.Get("TrackMonTuple")
        coll_TTHitMonitor = create_coll(det = "TT", mode = "Monitor")
        print "TT Monitor"
        for i, s in enumerate(t_TTHitMonitor):
            if i%100==0:
                cli_progress_test(i, t_TTHitMonitor.GetEntries(), start)
            if Number_Of_Events>0:
                if i>Number_Of_Events: continue
            for hit in range(0,s.len):
                for run_bin in coll_TTHitMonitor:
                    if ((s.RunNumber>=coll_TTHitMonitor[run_bin]["run_start"]) and (s.RunNumber<=coll_TTHitMonitor[run_bin]["run_stop"])):
                        coll_TTHitMonitor[run_bin]["data"][s.clusterSTchanMapID[hit]]["residual"].Fill(s.hit_residual[hit])
                        coll_TTHitMonitor[run_bin]["data"][s.clusterSTchanMapID[hit]]["errMeasure"].append(s.hit_errMeasure[hit])
                        coll_TTHitMonitor[run_bin]["data"][s.clusterSTchanMapID[hit]]["errResidual"].append(s.hit_errResidual[hit])
                        coll_TTHitMonitor[run_bin]["data"][s.clusterSTchanMapID[hit]]["unbiased_residual"].Fill(s.hit_residual[hit]*(abs(s.hit_errMeasure[hit]/s.hit_errResidual[hit])**2))
                        coll_TTHitMonitor[run_bin]["data"][s.clusterSTchanMapID[hit]]["rms_unbiased_residual"].Fill(s.hit_residual[hit]*abs(s.hit_errMeasure[hit]/s.hit_errResidual[hit]))
        write_histogram(coll_TTHitMonitor, "Monitor",histogram_address+"TTHitMonitor"+"__"+bin_name+"_")                        
        coll_TTHitMonitor = make_coll_lite(coll = coll_TTHitMonitor, det = "TT", mode = "Monitor")
        for run_bin in coll_TTHitMonitor:
            try:
                suffix = coll_TTHitMonitor[run_bin]['comment'].replace(" ","_")
            except:
                suffix = str(coll_TTHitMonitor[run_bin]["run_start"])+"__"+str(coll_TTHitMonitor[run_bin]["run_stop"])
            CreateTTHist(coll_TTHitMonitor[run_bin]["data"],variable = "mean", mode="Value",suffix= suffix,address=plot_address)
            CreateTTHist(coll_TTHitMonitor[run_bin]["data"],variable = "width", mode="Value",suffix=suffix,address=plot_address)           
        with open(pkl_address+'TTHitMonitor_'+bin_name+'.pkl', 'wb') as basket:
            pickle.dump(coll_TTHitMonitor, basket)        
        create_monitor_trends(coll_TTHitMonitor, "TT",histogram_address+"Trends_TTHitMonitor"+"__"+bin_name+"_")
    
    elif (oparation_mode=='3'):
        tree_TTHitEfficiency = f_input.TTHitEfficiency
        t_TTHitEfficiency = tree_TTHitEfficiency.Get("TrackMonTuple")
        coll_TTHitEfficiency = create_coll(det = "TT", mode = "Efficiency")
        print "TT Efficiency"
        for i, s in enumerate(t_TTHitEfficiency):
            if i%100==0:
                cli_progress_test(i, t_TTHitEfficiency.GetEntries(), start)    
            if Number_Of_Events>0:
                if i>Number_Of_Events: continue                
            for hit in range(0,s.len):
                for run_bin in coll_TTHitEfficiency:
                    if ((s.RunNumber>=coll_TTHitEfficiency[run_bin]["run_start"]) and (s.RunNumber<=coll_TTHitEfficiency[run_bin]["run_stop"])):
                        if s.isFound[hit]:
                            coll_TTHitEfficiency[run_bin]["data"][s.clusterSTchanMapID[hit]]["residual"].Fill(s.hit_residual[hit])
                        coll_TTHitEfficiency[run_bin]["data"][s.clusterSTchanMapID[hit]]["nbFound"]+=s.isFound[hit]
                        coll_TTHitEfficiency[run_bin]["data"][s.clusterSTchanMapID[hit]]["nbExpected"]+=s.isExpected[hit]
        coll_TTHitEfficiency = find_efficiency(coll_TTHitEfficiency)
        if perform_window_eff_study:
            coll_TTHitEfficiency = window_eff_study(coll_TTHitEfficiency)
            write_window_eff_study(coll_TTHitEfficiency, "Efficiency", histogram_address+"TTHitEfficiency"+"_"+bin_name+"_efficiency_study_")
        write_histogram(coll_TTHitEfficiency, "Efficiency",histogram_address+"TTHitEfficiency"+"__"+bin_name+"_")        
        coll_TTHitEfficiency = make_coll_lite(coll = coll_TTHitEfficiency, det = "TT", mode = "Efficiency")
        for run_bin in coll_TTHitEfficiency:
            try:
                suffix = coll_TTHitEfficiency[run_bin]["comment"]
            except:
                suffix = str(coll_TTHitEfficiency[run_bin]["run_start"])+"__"+str(coll_TTHitEfficiency[run_bin]["run_stop"])
            CreateTTHist(coll_TTHitEfficiency[run_bin]["data"],variable="efficiency", mode="Value",suffix=suffix,address=plot_address)
        with open(pkl_address+'TTHitEfficiency_'+bin_name+'.pkl', 'wb') as basket:
            pickle.dump(coll_TTHitEfficiency, basket)        
        create_efficiency_trends(coll_TTHitEfficiency, "TT",histogram_address+"Trends_TTHitEfficiency"+"__"+bin_name+"_")
    
    elif (oparation_mode=='4'):
        tree_ITHitEfficiency = f_input.ITHitEfficiency
        t_ITHitEfficiency = tree_ITHitEfficiency.Get("TrackMonTuple")
        coll_ITHitEfficiency = create_coll(det = "IT", mode = "Efficiency")    
        print "IT Efficiency"
        for i, s in enumerate(t_ITHitEfficiency):
            if i%100==0:
                cli_progress_test(i, t_ITHitEfficiency.GetEntries(), start)    
            if Number_Of_Events>0:
                if i>Number_Of_Events: continue                
            for hit in range(0,s.len):
                for run_bin in coll_ITHitEfficiency:
                    if ((s.RunNumber>=coll_ITHitEfficiency[run_bin]["run_start"]) and (s.RunNumber<=coll_ITHitEfficiency[run_bin]["run_stop"])):
                        if s.isFound[hit]:
                            coll_ITHitEfficiency[run_bin]["data"][s.clusterSTchanMapID[hit]]["residual"].Fill(s.hit_residual[hit])
                        coll_ITHitEfficiency[run_bin]["data"][s.clusterSTchanMapID[hit]]["nbFound"]+=s.isFound[hit]
                        coll_ITHitEfficiency[run_bin]["data"][s.clusterSTchanMapID[hit]]["nbExpected"]+=s.isExpected[hit]
        coll_ITHitEfficiency = find_efficiency(coll_ITHitEfficiency)
        if perform_window_eff_study:
            coll_ITHitEfficiency = window_eff_study(coll_ITHitEfficiency)
            write_window_eff_study(coll_ITHitEfficiency, "Efficiency", histogram_address+"ITHitEfficiency"+"_"+bin_name+"_efficiency_study_")
        write_histogram(coll_ITHitEfficiency, "Efficiency",histogram_address+"ITHitEfficiency"+"__"+bin_name+"_")        
        coll_ITHitEfficiency = make_coll_lite(coll = coll_ITHitEfficiency, det = "IT", mode = "Efficiency")    
        for run_bin in coll_ITHitEfficiency:
            try:
                suffix = coll_ITHitEfficiency[run_bin]["comment"]
            except:
                suffix = str(coll_ITHitEfficiency[run_bin]["run_start"])+"__"+str(coll_ITHitEfficiency[run_bin]["run_stop"])
            CreateITHist(coll_ITHitEfficiency[run_bin]["data"],variable="efficiency", mode="Value",suffix=suffix, address=plot_address)
        with open(pkl_address+'ITHitEfficiency_'+bin_name+'.pkl', 'wb') as basket:
            pickle.dump(coll_ITHitEfficiency, basket)                
        create_efficiency_trends(coll_ITHitEfficiency, "IT",histogram_address+"Trends_ITHitEfficiency"+"__"+bin_name+"_")
    
    else:
        syntax_explanation("TupToHist.py")

    return True

if __name__ == "__main__":
    if len(sys.argv)==3:
        data = sys.argv[1]
        TupToHist(data,sys.argv[2])
    else:
        syntax_explanation("TupToHist.py")

