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
from drawing.Create_Maps import *
from config import binning
from config import histogram_address
from config import plot_address
import ROOT as R
from ROOT import gStyle
gStyle.SetOptStat(False)
#from ROOT import RooFit as RF


def PklToHist(data, operation_mode, histogram_address=histogram_address, plot_address=plot_address, dump_summary = False):
    if (operation_mode=='1'):
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
            CreateITHist(coll_ITHitMonitor[run_bin]["data"],variable="mean", mode="Value",suffix = suffix, address=plot_address)
            CreateITHist(coll_ITHitMonitor[run_bin]["data"],variable="width", mode="Value",suffix = suffix, address=plot_address)
        print "2D plots created"#, writing histograms to .root file"            
        #write_histogram(coll_ITHitMonitor, "Monitor", histogram_address+"ITHitMonitor")
        print "Creating trends"
        create_monitor_trends(coll_ITHitMonitor, "IT", histogram_address+"Trends_ITHitMonitor")
        if dump_summary:
            ITResolution = []
            IT_Map_dict = IT_Map()
            IT_ids_Map_dict = IT_ids_Map()
            for st_id in coll_ITHitMonitor[0]['data']:
                ITResolution.append({'name':IT_Map_dict[st_id],'id':IT_ids_Map_dict[st_id],'resolution':coll_ITHitMonitor[0]['data'][st_id]['width'], 'mean':coll_ITHitMonitor[0]['data'][st_id]['mean'], 'err_width:':coll_ITHitMonitor[0]['data'][st_id]['err_width']})
            with open('Resolution_Map_IT.pkl', 'wb') as basket:
                pickle.dump(ITResolution, basket)        

    
    elif (operation_mode=='2'):
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
            CreateTTHist(coll_TTHitMonitor[run_bin]["data"],variable="mean", mode="Value",suffix= suffix,address=plot_address)
            CreateTTHist(coll_TTHitMonitor[run_bin]["data"],variable="width", mode="Value",suffix=suffix,address=plot_address)
        print "2D plots created"#, writing histograms to .root file"            
        #write_histogram(coll_TTHitMonitor, "Monitor",histogram_address+"TTHitMonitor")
        print "Creating trends"
        create_monitor_trends(coll_TTHitMonitor, "TT",histogram_address+"Trends_TTHitMonitor")
        if dump_summary:
            TTResolution = []
            TT_Map_dict = TT_Map()
            TT_ids_Map_dict = TT_ids_Map()
            for st_id in coll_TTHitMonitor[0]['data']:
                TTResolution.append({'name':TT_Map_dict[st_id],'id':TT_ids_Map_dict[st_id],'resolution':coll_TTHitMonitor[0]['data'][st_id]['width'], 'mean':coll_TTHitMonitor[0]['data'][st_id]['mean'], 'err_width:':coll_TTHitMonitor[0]['data'][st_id]['err_width']})
            with open('Resolution_Map_TT.pkl', 'wb') as basket:
                pickle.dump(TTResolution, basket)  
    
    elif (operation_mode=='3'):
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
            CreateTTHist(coll_TTHitEfficiency[run_bin]["data"],variable = "efficiency", mode="Value",suffix=suffix,address=plot_address)
        print "2D plots created"#, writing histograms to .root file"            
        #write_histogram(coll_TTHitEfficiency, "Efficiency",histogram_address+"TTHitEfficiency")
        print "Creating trends"
        create_efficiency_trends(coll_TTHitEfficiency, "TT",histogram_address+"Trends_TTHitEfficiency")
        if dump_summary:
            TTEfficiency = []
            TT_Map_dict = TT_Map()
            TT_ids_Map_dict = TT_ids_Map()
            for st_id in coll_TTHitEfficiency[0]['data']:
                TTEfficiency.append({'name':TT_Map_dict[st_id],'id':TT_ids_Map_dict[st_id],'efficiency':coll_TTHitEfficiency[0]['data'][st_id]['efficiency'], 'err_efficiency':coll_TTHitEfficiency[0]['data'][st_id]['err_efficiency']})
            with open('Efficiency_Map_TT.pkl', 'wb') as basket:
                pickle.dump(TTEfficiency, basket)  

    
    elif (operation_mode=='4'):
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
            CreateITHist(coll_ITHitEfficiency[run_bin]["data"],variable = "efficiency", mode="Value",suffix=suffix, address=plot_address)
        print "2D plots created"#, writing histograms to .root file"            
        #write_histogram(coll_ITHitEfficiency, "Efficiency",histogram_address+"ITHitEfficiency")
        print "Creating trends"
        create_efficiency_trends(coll_ITHitEfficiency, "IT",histogram_address+"Trends_ITHitEfficiency")
        if dump_summary:
            ITEfficiency = []
            IT_Map_dict = IT_Map()
            IT_ids_Map_dict = IT_ids_Map()
            for st_id in coll_ITHitEfficiency[0]['data']:
                ITEfficiency.append({'name':IT_Map_dict[st_id],'id':IT_ids_Map_dict[st_id],'efficiency':coll_ITHitEfficiency[0]['data'][st_id]['efficiency'], 'err_efficiency':coll_ITHitEfficiency[0]['data'][st_id]['err_efficiency']})
            with open('Efficiency_Map_IT.pkl', 'wb') as basket:
                pickle.dump(ITEfficiency, basket)  

    
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
        PklToHist(data,sys.argv[2])
    if len(sys.argv)==4:
        data = sys.argv[1]
        PklToHist(data = data, operation_mode = sys.argv[2], dump_summary = True)
    else:
        syntax_explanation("PklToHist.py")
       
