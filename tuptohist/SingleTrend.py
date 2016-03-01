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
from config import binning
from config import histogram_address
from config import plot_address
import ROOT as R
from ROOT import gStyle
gStyle.SetOptStat(False)
#from ROOT import RooFit as RF


def SingleTrend(data, sector, histogram_address=histogram_address, plot_address=plot_address):
    with open(data, 'r') as basket:
        coll = pickle.load(basket)
    for run in coll:
        if "mean" in coll[run]["data"]:
            create_single_monitor_trend(coll, sector, plot_address)
        else:
            create_single_efficiency_trend(coll, sector, plot_address)
        break
    return True

if __name__ == "__main__":
    #local_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    if len(sys.argv)==3:
        data = sys.argv[1]
        SingleTrend(data,sys.argv[2])
    else:
        syntax_explanation("SingleTrend.py")
       
