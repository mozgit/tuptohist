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
from datetime import datetime
from drawing.Create_Maps import TT_Map as TT_Map_func
from drawing.Create_Maps import IT_Map as IT_Map_func

import ROOT as R
from ROOT import gStyle
gStyle.SetOptStat(False)


def syntax_explanation(script):
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
    return run_schema


#R.TH1F("hist_s","Name",100, -3,3)

def create_monitor_ind(st_name,run_range):
    #Information which should be filled for individual sector for Monitor mode
    #To produce .root files only!
    monitor_ind = {
    "residual":R.TH1F("residualM"+run_range+"_"+st_name,"Residual;[mm];Number of events",100, -0.5,0.5),
    "errMeasure":[],
    "errResidual":[],
    "unbiased_residual":R.TH1F("unbiasedresidualM"+run_range+"_"+st_name,"Residual (rms-unbiased);[mm];Number of events",100, -0.5,0.5)}
    return monitor_ind

def create_efficiency_ind(st_name,run_range):
    #Information which should be filled for individual sector for Efficiency mode
    #To produce .root files only!
    efficiency_ind = {"nbFound":0,
    "nbExpected":0,
    "efficiency":0,
    "err_efficiency":0,
    "residual":R.TH1F("residualE"+run_range+"_"+st_name,"Residual;[mm];Number of events",100, -0.5,0.5),
    "efficiency_hist":R.TH1F("efficiency"+run_range+"_"+st_name,"Efficiency",1, 0.,1.)}
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

def write_histogram(coll, mode, name):
    f = R.TFile(name+"histos.root","recreate")
    for run_bin in coll:
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
            ubresidual_mean.GetXaxis().SetBinLabel(i+1,str(lite_coll[run_bin]["run_start"])+"-"+str(lite_coll[run_bin]["run_stop"]))
            ubresidual_width.SetBinContent(i+1, lite_coll[run_bin]["data"][st_id]["width"])
            ubresidual_width.GetXaxis().SetNdivisions(-414)
            ubresidual_width.GetXaxis().SetBinLabel(i+1,str(lite_coll[run_bin]["run_start"])+"-"+str(lite_coll[run_bin]["run_stop"]))
        ubresidual_mean.Write()
        ubresidual_width.Write()
    f.Close()
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
            efficiency.GetXaxis().SetBinLabel(i+1,str(lite_coll[run_bin]["run_start"])+"-"+str(lite_coll[run_bin]["run_stop"]))
        efficiency.Write()
    f.Close()
    return True

if __name__ == "__main__":
  print "Here are contained supplimentary functions for Tuple to Histogram transformation."
  print "Normally, Tuples are stored as a python dictionaries (see create_coll, create_monitor_ind and create_efficiency_ind)"
  print "Two type of dictioanries is considered: Efficiency-like and Monitor-like"
  print "These dictionaries contains histograms, which a later stored in a .root file (In format which is recognized by interactie ST monitor)"
  print "Basing on time binning, trend histograms are also created. (They are also saved in ST-monitor-friendly .root files)"
  print "ST map plots are created by funcitons from CreateTTHist and CreateITHist files."
