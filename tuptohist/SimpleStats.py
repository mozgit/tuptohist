import sys
import ROOT as R
from ROOT import gStyle
import os
from suppl.Structure import *
from drawing.Create_Maps import TT_Map as TT_Map_func
from drawing.Create_Maps import IT_Map as IT_Map_func
gStyle.SetOptStat(False)
#from ROOT import RooFit as RF


def simple_analysis(data):
    #Make distribution of per-sector parameters wieghted with the nEvents and define mean and rms
    try:
        from config import dead_sectors
    except:
        dead_sectors = []
    TT_Map = TT_Map_func()
    IT_Map = IT_Map_func()

    f_input = R.TFile(data)
    tree_ITHitMonitor = f_input.ITHitMonitor
    t_ITHitMonitor = tree_ITHitMonitor.Get("TrackMonTuple")
    h_ITHitMonitor_u = R.TH2F("h_ITHitMonitor_u","h_ITHitMonitor_u", max(IT_Map.keys())+1, -0.5, max(IT_Map.keys())+0.5, 200, -0.3,0.3)
    h_ITHitMonitor_r = R.TH2F("h_ITHitMonitor_r","h_ITHitMonitor_r", max(IT_Map.keys())+1, -0.5, max(IT_Map.keys())+0.5, 200, -0.3,0.3)
    t_ITHitMonitor.Project("h_ITHitMonitor_u", "hit_residual*hit_errMeasure*hit_errMeasure/hit_errResidual/hit_errResidual:clusterSTchanMapID")
    t_ITHitMonitor.Project("h_ITHitMonitor_r", "hit_residual*hit_errMeasure/hit_errResidual:clusterSTchanMapID")
    it_mean_abswidth=0
    h_it_mean_abswidth = R.TH1F("h_it_mean_abswidth","h_it_mean_abswidth", 100, 0., 0.03)
    it_mean_res=0
    h_it_mean_res = R.TH1F("h_it_mean_res","h_it_mean_res", 100, 0.03, 0.06)
    it_nEntries=0    
    for i in IT_Map.keys():
        if not IT_Map[i] in dead_sectors:            
            #print "Processing "+IT_Map[i]
            h_hist_u = h_ITHitMonitor_u.ProjectionY(IT_Map[i], i+1, i+1)
            h_hist_r = h_ITHitMonitor_r.ProjectionY(IT_Map[i], i+1, i+1)
            it_mean_abswidth    += abs(h_hist_u.GetMean())*h_hist_u.GetEntries()
            h_it_mean_abswidth.Fill(abs(h_hist_u.GetMean()), h_hist_u.GetEntries())
            it_mean_res         += h_hist_r.GetRMS()*h_hist_r.GetEntries()
            h_it_mean_res.Fill(h_hist_r.GetRMS(), h_hist_r.GetEntries())
            it_nEntries         += h_hist_r.GetEntries()
            del h_hist_u
            del h_hist_r
    it_mean_abswidth = float(it_mean_abswidth)/it_nEntries
    it_mean_res = float(it_mean_res)/it_nEntries

    
    tree_TTHitMonitor = f_input.TTHitMonitor
    t_TTHitMonitor = tree_TTHitMonitor.Get("TrackMonTuple")
    h_TTHitMonitor_u = R.TH2F("h_TTHitMonitor_u","h_TTHitMonitor_u", max(TT_Map.keys())+1, -0.5, max(TT_Map.keys())+0.5, 200, -0.3,0.3)
    h_TTHitMonitor_r = R.TH2F("h_TTHitMonitor_r","h_TTHitMonitor_r", max(TT_Map.keys())+1, -0.5, max(TT_Map.keys())+0.5, 200, -0.3,0.3)
    t_TTHitMonitor.Project("h_TTHitMonitor_u", "hit_residual*hit_errMeasure*hit_errMeasure/hit_errResidual/hit_errResidual:clusterSTchanMapID")
    t_TTHitMonitor.Project("h_TTHitMonitor_r", "hit_residual*hit_errMeasure/hit_errResidual:clusterSTchanMapID")
    tt_mean_abswidth=0
    h_tt_mean_abswidth = R.TH1F("h_tt_mean_abswidth","h_tt_mean_abswidth", 100, 0., 0.03)
    tt_mean_res=0
    h_tt_mean_res = R.TH1F("h_tt_mean_res","h_tt_mean_res", 100, 0.03, 0.06)
    tt_nEntries=0    
    for i in TT_Map.keys():
        if not IT_Map[i] in dead_sectors:            
            #print "Processing "+TT_Map[i]
            h_hist_u = h_TTHitMonitor_u.ProjectionY(TT_Map[i], i+1, i+1)
            h_hist_r = h_TTHitMonitor_r.ProjectionY(TT_Map[i], i+1, i+1)
            tt_mean_abswidth    += abs(h_hist_u.GetMean())*h_hist_u.GetEntries()
            h_tt_mean_abswidth.Fill(abs(h_hist_u.GetMean()), h_hist_u.GetEntries())
            tt_mean_res         += h_hist_r.GetRMS()*h_hist_r.GetEntries()
            h_tt_mean_res.Fill(h_hist_r.GetRMS(), h_hist_r.GetEntries())
            tt_nEntries         += h_hist_r.GetEntries()
            del h_hist_u
            del h_hist_r
    tt_mean_abswidth = float(tt_mean_abswidth)/tt_nEntries
    tt_mean_res = float(tt_mean_res)/tt_nEntries

    tree_TTHitEfficiency = f_input.TTHitEfficiency
    t_TTHitEfficiency = tree_TTHitEfficiency.Get("TrackMonTuple")
    h_TTHitEfficiency = R.TH1F("h_TTHitEfficiency","h_TTHitEfficiency",100, 0.,1.1)
    t_TTHitEfficiency.Project("h_TTHitEfficiency","isFound")
    tt_eff = h_TTHitEfficiency.GetMean()
    tot_tt_eff = h_TTHitEfficiency.GetEntries()
    nf_tt_eff = tot_tt_eff*(1-tt_eff)
    f_tt_eff = tot_tt_eff*tt_eff
    err_tt_eff = (f_tt_eff*nf_tt_eff/tot_tt_eff**3)**0.5

    tree_ITHitEfficiency = f_input.ITHitEfficiency
    t_ITHitEfficiency = tree_ITHitEfficiency.Get("TrackMonTuple")
    h_ITHitEfficiency = R.TH1F("h_ITHitEfficiency","h_ITHitEfficiency",100, 0.,1.1)
    t_ITHitEfficiency.Project("h_ITHitEfficiency","isFound")
    it_eff = h_ITHitEfficiency.GetMean()
    tot_it_eff = h_ITHitEfficiency.GetEntries()
    nf_it_eff = tot_it_eff*(1-it_eff)
    f_it_eff = tot_it_eff*it_eff
    err_it_eff = (f_it_eff*nf_it_eff/tot_it_eff**3)**0.5

    print "Uncertainty \"From Hist\" is obtained as RMS of variable distribution weighted with number of events.\
    Each entry correspond to the sector, value is value of the preformance variable, wwight is a number of events."
    #print "(Normal)    Weighted resolution IT: "+str(it_mean_res)
    print "(From Hist) Weighted resolution IT: "+str(h_it_mean_res.GetMean()) +" +/- "+str(h_it_mean_res.GetRMS()) 
    #print "(Normal)    Weighted abs. bias  IT: "+str(it_mean_abswidth)
    print "(From Hist) Weighted abs. bias  IT: "+str(h_it_mean_abswidth.GetMean()) +" +/- "+str(h_it_mean_abswidth.GetRMS()) 
    print "(Normal)    Weighted efficiency IT: "+str(it_eff) + " +/- "+str(err_it_eff)
    #print "(Normal)    Weighted resolution TT: "+str(tt_mean_res)
    print "(From Hist) Weighted resolution TT: "+str(h_tt_mean_res.GetMean()) +" +/- "+str(h_tt_mean_res.GetRMS()) 
    #print "(Normal)    Weighted abs. bias  TT: "+str(tt_mean_abswidth)
    print "(From Hist) Weighted abs. bias  TT: "+str(h_tt_mean_abswidth.GetMean()) +" +/- "+str(h_tt_mean_abswidth.GetRMS()) 
    print "(Normal)    Weighted efficiency TT: "+str(tt_eff) + " +/- "+str(err_tt_eff)


    return True

if __name__ == "__main__":
    if len(sys.argv)==2:
        data = sys.argv[1]
        simple_analysis(data)
    else:
        print "Indicate tuple to analyse"
        #syntax_explanation("SimpleStats.py")

