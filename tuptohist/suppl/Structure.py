"""
Here are contained supplimentary functions for Tuple to Histogram and Pkl to Histogram transformation.
Normally, Tuples are stored as a python dictionaries (see create_coll, create_monitor_ind and create_efficiency_ind)
Two type of dictioanries is considered: Efficiency-like and Monitor-like
These dictionaries contains histograms, which a later stored in a .root file (In format which is recognized by interactie ST monitor)
Basing on time binning, trend histograms are also created. (They are also saved in ST-monitor-friendly .root files)
ST map plots are created by funcitons from CreateTTHist and CreateITHist files.
"""

import os
import inspect
from pprint import pprint
from itertools import product
import math
import numpy as n
import sys
from config import binning
from config import residual_limit
from config import perform_window_eff_study
from config import efficiency_windows
from config import residual_nBins

from datetime import datetime
from drawing.Create_Maps import TT_Map as TT_Map_func
from drawing.Create_Maps import IT_Map as IT_Map_func

import ROOT as R
from ROOT import gStyle
gStyle.SetOptStat(False)


def syntax_explanation(script):
    if script == "SingleTrend.py":
        print "Incorrect syntax. Please run with:"
        print "python "+script+" <pkl_data_file> <sector_name>"
        print "Plese use sector names like 'TTaXRegionBSector9'"
    else:
        print "Incorrect syntax. Please run with:"
        print "python "+script+" <data_file> <mode>"
        print "<mode> here:"
        print "1 - IT Hit Monitor"
        print "2 - TT Hit Monitor"
        print "3 - TT Hit Efficiency"
        print "4 - IT Hit Efficiency"
    return True 

def cli_progress_test(i, end_val, start, bar_length=20):
    percent = float(i) / end_val
    hashes = '#' * int(round(percent * bar_length))
    spaces = ' ' * (bar_length - len(hashes))
    sys.stdout.write("\rPercent: [{0}] {1}% ({2}/{3}), {4}".format(hashes + spaces, int(round(percent * 100)),i, end_val, datetime.now()-start))
    sys.stdout.flush()


def run_binning():
    #{<run_start>:{"run_start":<run_start>,
    #           "run_stop":<run_stop>}
    #}    
    global binning
    run_schema = {}
    for pb in binning:
        run_schema[pb["run_start"]]={"run_start":pb["run_start"],"run_stop":pb["run_stop"]}
        try:
            run_schema[pb["run_start"]]["comment"]=pb["comment"]
        except:
            print "Unable to find alias for bin range. Use numbers instead"
            pass
    return run_schema


#R.TH1F("hist_s","Name",100, -3,3)

def create_monitor_ind(st_name,run_range):
    #Information which should be filled for individual sector for Monitor mode
    #To produce .root files only!
    global residual_limit
    global residual_nBins
    monitor_ind = {
    "residual":R.TH1F("residualM"+run_range+"_"+st_name,"Residual;[mm];Number of events",residual_nBins, -residual_limit,residual_limit),
    "errMeasure":[],
    "errResidual":[],
    "unbiased_residual":R.TH1F("unbiasedresidualM"+run_range+"_"+st_name,"Residual (rms-unbiased);[mm];Number of events",residual_nBins, -residual_limit,residual_limit)}
    return monitor_ind

def create_efficiency_ind(st_name,run_range):
    #Information which should be filled for individual sector for Efficiency mode
    #To produce .root files only!
    global residual_limit
    global residual_nBins
    global perform_window_eff_study
    global efficiency_windows
    efficiency_ind = {"nbFound":0,
    "nbExpected":0,
    "efficiency":0,
    "err_efficiency":0,
    "residual":R.TH1F("residualE"+run_range+"_"+st_name,"Residual;[mm];Number of events",residual_nBins, -residual_limit,residual_limit),
    "efficiency_hist":R.TH1F("efficiency"+run_range+"_"+st_name,"Efficiency",1, 0.,1.)}
    if perform_window_eff_study:
        efficiency_ind["window_dependence"] = R.TH1F("wind_dep_"+run_range+"_"+st_name,"Efficiency as a function of search window;[mm];Efficiency",len(efficiency_windows), 0.,1.)
    return efficiency_ind

def create_monitor_lite(monitor_ind):
    #Information which should be filled for individual sector for Monitor mode
    #To produce .pkls and build trends.
    monitor_lite = {
    "mean":monitor_ind["unbiased_residual"].GetMean(),
    "width":monitor_ind["unbiased_residual"].GetRMS()}
    return monitor_lite

def create_efficiency_lite(efficiency_ind):
    #Information which should be filled for individual sector for Efficiency mode
    #To produce .pkls and build trends.
    efficiency_lite = {
    "efficiency":efficiency_ind["efficiency"],
    "err_efficiency":efficiency_ind["err_efficiency"],}
    return efficiency_lite


def create_coll(det="IT", mode="Monitor"):
    #To be used for creation of histograms
    #{<run_start>:{
    #            "run_start":<run_start>,
    #            "run_stop" :<run_stop>,
    #            "data"     :{
    #                        <st_ID1>:{},
    #                        <st_ID2>:{},
    #                        <st_ID3>:{}...
    #}             }          } 
    coll = run_binning()
    if det == "IT":
        ST_Map = IT_Map_func()
    else:
        ST_Map = TT_Map_func()
    for run_bin in coll:
        try:
            run_range=coll[run_bin]["comment"]
        except:
            run_range="::::"+str(coll[run_bin]["run_start"])+"::"+str(coll[run_bin]["run_stop"])+"::::"
        coll[run_bin]["data"]={}
        for st_id in ST_Map:
            if mode == "Monitor":
                coll[run_bin]["data"][st_id]=create_monitor_ind(ST_Map[st_id],run_range)
            else:
                coll[run_bin]["data"][st_id]=create_efficiency_ind(ST_Map[st_id],run_range)
    return coll

def make_coll_lite(coll, det="IT", mode="Monitor"):
    #To be stored in .pkl, to create trends
    #{<run_start>:{
    #            "run_start":<run_start>,
    #            "run_stop" :<run_stop>,
    #            "data"     :{
    #                        <st_ID1>:{},
    #                        <st_ID2>:{},
    #                        <st_ID3>:{}...
    #}             }          } 
    lite_coll = run_binning()
    if det == "IT":
        ST_Map = IT_Map_func()
    else:
        ST_Map = TT_Map_func()
    for run_bin in coll:
        try:
            run_range=coll[run_bin]["comment"]
        except:
            run_range="::::"+str(coll[run_bin]["run_start"])+"::"+str(coll[run_bin]["run_stop"])+"::::"
        lite_coll[run_bin]["data"]={}
        for st_id in ST_Map:
            if mode == "Monitor":
                lite_coll[run_bin]["data"][st_id]=create_monitor_lite(coll[run_bin]["data"][st_id])
            else:
                lite_coll[run_bin]["data"][st_id]=create_efficiency_lite(coll[run_bin]["data"][st_id])
    return lite_coll

def find_efficiency(coll):
    for run_bin in coll:
        for st_ID in coll[run_bin]["data"]:
            nbf = coll[run_bin]["data"][st_ID]["nbFound"]
            nbe = coll[run_bin]["data"][st_ID]["nbExpected"]
            if nbe == 0:
                coll[run_bin]["data"][st_ID]["efficiency"]= 0
                coll[run_bin]["data"][st_ID]["err_efficiency"] = 0
                coll[run_bin]["data"][st_ID]["efficiency_hist"].SetBinContent(1, 0)
                coll[run_bin]["data"][st_ID]["efficiency_hist"].SetBinError(1, 0)
                continue
            coll[run_bin]["data"][st_ID]["efficiency"]=nbf/nbe
            coll[run_bin]["data"][st_ID]["err_efficiency"] = nbf**0.5*(nbe-nbf)**0.5*nbe**(-1.5)
            coll[run_bin]["data"][st_ID]["efficiency_hist"].SetBinContent(1, coll[run_bin]["data"][st_ID]["efficiency"])
            coll[run_bin]["data"][st_ID]["efficiency_hist"].SetBinError(1, coll[run_bin]["data"][st_ID]["err_efficiency"])
    return coll

def bins_from_window(window):
    global residual_limit
    global residual_nBins
    bin_width = 2.*float(residual_limit)/float(residual_nBins)
    bin_low = residual_nBins/2 - int(window/bin_width)
    bin_hi = residual_nBins-bin_low+1
    return [bin_low, bin_hi]


def window_eff_study(coll):
    global efficiency_windows
    for run_bin in coll:
        for st_ID in coll[run_bin]["data"]:
            nbe = coll[run_bin]["data"][st_ID]["nbExpected"]
            if nbe == 0:
                continue            
            coll[run_bin]["data"][st_ID]["window_dependence"].GetXaxis().SetNdivisions(-414)
            for i, window in enumerate(sorted(efficiency_windows)):
                nbf = coll[run_bin]["data"][st_ID]["residual"].Integral(bins_from_window(window)[0], bins_from_window(window)[1])
                coll[run_bin]["data"][st_ID]["window_dependence"].SetBinContent(i+1, nbf/nbe)
                if nbf!=0:
                    coll[run_bin]["data"][st_ID]["window_dependence"].SetBinError(i+1, nbf**0.5*(nbe-nbf)**0.5*nbe**(-1.5))
                else:
                    coll[run_bin]["data"][st_ID]["window_dependence"].SetBinError(i+1, 0)
                coll[run_bin]["data"][st_ID]["window_dependence"].GetXaxis().SetBinLabel(i+1,str(window))
    return coll

def write_histogram(coll, mode, name):
    f = R.TFile(name+"histos.root","recreate")
    for run_bin in coll:
        try:
            cdtof = f.mkdir(coll[run_bin]["comment"])
        except:
            cdtof = f.mkdir(str(coll[run_bin]["run_start"])+"-"+str(coll[run_bin]["run_stop"]))
        cdtof.cd()
        for st_id in coll[run_bin]["data"]:
            if mode == "Monitor":
                #coll[run_bin]["data"][st_id]["residual"].Write()            
                coll[run_bin]["data"][st_id]["unbiased_residual"].Write()
            else:
                #coll[run_bin]["data"][st_id]["residual"].Write()            
                coll[run_bin]["data"][st_id]["efficiency_hist"].Write()
    f.Close()
    return True

def write_window_eff_study(coll, mode, name):
    f = R.TFile(name+"histos.root","recreate")
    for run_bin in coll:
        try:
            cdtof = f.mkdir(coll[run_bin]["comment"])
        except:
            cdtof = f.mkdir(str(coll[run_bin]["run_start"])+"-"+str(coll[run_bin]["run_stop"]))
        cdtof.cd()
        for st_id in coll[run_bin]["data"]:
            coll[run_bin]["data"][st_id]["window_dependence"].Write()
    f.Close()
    return True

def create_monitor_trends(lite_coll, det, name):
    f = R.TFile(name+"histos.root","recreate")
    f.cd()
    if det == "IT":
        ST_Map = IT_Map_func()
    else:
        ST_Map = TT_Map_func()
    for st_id in ST_Map:
        ubresidual_mean = R.TH1F("bias:trend:RMSNB:M_"+ST_Map[st_id],"Changes of hit residual mean (rms-unbiased);;Bias, [mm]",len(lite_coll),0,1)
        ubresidual_width = R.TH1F("width:trend:RMSNB:M_"+ST_Map[st_id],"Changes of hit residual width rms-unbiased;;Resolution, [mm]",len(lite_coll),0,1)
        for i, run_bin in enumerate(sorted(lite_coll.keys())):
            ubresidual_mean.SetBinContent(i+1, lite_coll[run_bin]["data"][st_id]["mean"])
            ubresidual_mean.SetBinError(i+1, lite_coll[run_bin]["data"][st_id]["width"])
            ubresidual_mean.GetXaxis().SetNdivisions(-414)
            try:
                ubresidual_mean.GetXaxis().SetBinLabel(i+1,lite_coll[run_bin]["comment"])
            except:
                ubresidual_mean.GetXaxis().SetBinLabel(i+1,str(lite_coll[run_bin]["run_start"])+"-"+str(lite_coll[run_bin]["run_stop"]))
            ubresidual_width.SetBinContent(i+1, lite_coll[run_bin]["data"][st_id]["width"])
            ubresidual_width.GetXaxis().SetNdivisions(-414)
            try:
                ubresidual_width.GetXaxis().SetBinLabel(i+1,lite_coll[run_bin]["comment"])
            except:
                ubresidual_width.GetXaxis().SetBinLabel(i+1,str(lite_coll[run_bin]["run_start"])+"-"+str(lite_coll[run_bin]["run_stop"]))
        ubresidual_mean.Write()
        ubresidual_width.Write()
    f.Close()
    print "Residual trends created at "+name+"histos.root"
    return True

def create_single_monitor_trend(lite_coll, sector, plot_address):
    setcor_is_found = False
    if "IT" in sector:
        ST_Map = IT_Map_func()
    else:
        ST_Map = TT_Map_func()
    for i in ST_Map:
        if ST_Map[i]==sector:
            st_id = i
            break
    if not st_id:
        print "Wrong sector. Plese use sector names like 'TTaXRegionBSector9'"
        return False
    ubresidual_mean = R.TH1F(sector,"Changes of hit residual mean (rms-unbiased) of "+sector+";;Bias, [mm]",len(lite_coll),0,1)
    ubresidual_width = R.TH1F(sector,"Changes of hit residual width rms-unbiased of "+sector+";;Resolution, [mm]",len(lite_coll),0,1)
    for i, run_bin in enumerate(sorted(lite_coll.keys())):
        if st_id in lite_coll[run_bin]["data"]:
            setcor_is_found = True
            ubresidual_mean.SetBinContent(i+1, lite_coll[run_bin]["data"][st_id]["mean"])
            ubresidual_mean.SetBinError(i+1, lite_coll[run_bin]["data"][st_id]["width"])
            ubresidual_mean.GetXaxis().SetNdivisions(-414)
            try:
                ubresidual_mean.GetXaxis().SetBinLabel(i+1,lite_coll[run_bin]["comment"])
            except:
                ubresidual_mean.GetXaxis().SetBinLabel(i+1,str(lite_coll[run_bin]["run_start"])+"-"+str(lite_coll[run_bin]["run_stop"]))
            ubresidual_width.SetBinContent(i+1, lite_coll[run_bin]["data"][st_id]["width"])
            ubresidual_width.GetXaxis().SetNdivisions(-414)
            try:
                ubresidual_width.GetXaxis().SetBinLabel(i+1,lite_coll[run_bin]["comment"])
            except:
                ubresidual_width.GetXaxis().SetBinLabel(i+1,str(lite_coll[run_bin]["run_start"])+"-"+str(lite_coll[run_bin]["run_stop"]))
    if not setcor_is_found:
        print "Trends are empty, please check that you use correct dataset for chosen sector"
        return False
    c1 = R.TCanvas("c1","c1",600,600)
    ubresidual_mean.Draw()
    c1.SaveAs(plot_address+"/Trend_Mean_Sector_"+sector+".pdf")
    c1.SaveAs(plot_address+"/Trend_Mean_Sector_"+sector+".C")
    c2 = R.TCanvas("c2","c2",600,600)
    ubresidual_width.Draw()
    c2.SaveAs(plot_address+"/Trend_Width_Sector_"+sector+".pdf")
    c2.SaveAs(plot_address+"/Trend_Width_Sector_"+sector+".C")
    return True


def create_efficiency_trends(lite_coll, det, name):
    f = R.TFile(name+"histos.root","recreate")
    if det == "IT":
        ST_Map = IT_Map_func()
    else:
        ST_Map = TT_Map_func()
    for st_id in ST_Map:
        efficiency = R.TH1F("eff:trend_"+ST_Map[st_id],"Changes of hit efficiency;;Efficiency",len(lite_coll),0,1)
        for i, run_bin in enumerate(sorted(lite_coll.keys())):
            efficiency.SetBinContent(i+1, lite_coll[run_bin]["data"][st_id]["efficiency"])
            efficiency.SetBinError(i+1, lite_coll[run_bin]["data"][st_id]["err_efficiency"])
            efficiency.GetXaxis().SetNdivisions(-414)
            try:
                efficiency.GetXaxis().SetBinLabel(i+1,lite_coll[run_bin]["comment"])
            except:            
                efficiency.GetXaxis().SetBinLabel(i+1,str(lite_coll[run_bin]["run_start"])+"-"+str(lite_coll[run_bin]["run_stop"]))
        efficiency.Write()
    f.Close()
    print "Efficiency trends created at "+name+"histos.root"
    return True

def create_single_efficiency_trend(lite_coll, sector, plot_address):
    setcor_is_found = False
    if "IT" in sector:
        ST_Map = IT_Map_func()
    else:
        ST_Map = TT_Map_func()
    for i in ST_Map:
        if ST_Map[i]==sector:
            st_id = i
            break
    if not st_id:
        print "Wrong sector. Plese use sector names like 'TTaXRegionBSector9'"
        return False
    efficiency = R.TH1F(sector,"Changes of hit efficiency of "+sector+";;Efficiency",len(lite_coll),0,1)
    for i, run_bin in enumerate(sorted(lite_coll.keys())):
        if st_id in lite_coll[run_bin]["data"]:
            setcor_is_found = True
            efficiency.SetBinContent(i+1, lite_coll[run_bin]["data"][st_id]["efficiency"])
            efficiency.SetBinError(i+1, lite_coll[run_bin]["data"][st_id]["err_efficiency"])
            efficiency.GetXaxis().SetNdivisions(-414)
            try:
                efficiency.GetXaxis().SetBinLabel(i+1,lite_coll[run_bin]["comment"])
            except:            
                efficiency.GetXaxis().SetBinLabel(i+1,str(lite_coll[run_bin]["run_start"])+"-"+str(lite_coll[run_bin]["run_stop"]))
    if not setcor_is_found:
        print "Trends are empty, please check that you use correct dataset for chosen sector"
        return False
    c1 = R.TCanvas("c1","c1",600,600)
    efficiency.Draw()
    c1.SaveAs(plot_address+"/Trend_Efficiency_Sector_"+sector+".pdf")
    c1.SaveAs(plot_address+"/Trend_Efficiency_Sector_"+sector+".C")
    return True


if __name__ == "__main__":
  print "Here are contained supplimentary functions for Tuple to Histogram transformation."
  print "Normally, Tuples are stored as a python dictionaries (see create_coll, create_monitor_ind and create_efficiency_ind)"
  print "Two type of dictioanries is considered: Efficiency-like and Monitor-like"
  print "These dictionaries contains histograms, which a later stored in a .root file (In format which is recognized by interactie ST monitor)"
  print "Basing on time binning, trend histograms are also created. (They are also saved in ST-monitor-friendly .root files)"
  print "ST map plots are created by funcitons from CreateTTHist and CreateITHist files."
