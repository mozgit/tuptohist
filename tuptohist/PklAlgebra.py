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
from config import pkl_address
import ROOT as R
from ROOT import gStyle
import parser
gStyle.SetOptStat(False)
#from ROOT import RooFit as RF


def PklAlgebra(dataset_1, dataset_2,formula,  pkl_address=pkl_address):
    text_formula="_"+formula.replace("/","_over_").replace("*","_times_").replace("+","_plus_").replace("-","_minus_")+"_"

    code = parser.expr(formula).compile()

    
    with open(dataset_1, 'r') as basket:
        ds_1 = pickle.load(basket)
    with open(dataset_2, 'r') as basket:
        ds_2 = pickle.load(basket)

    tot_coll={}
    if ds_1.keys()!= ds_2.keys():
        print "ERROR: Different binnings of datasets. Please use .pkls with collections, which have the same time binning"
        return False
    for run_bin in ds_1.keys():
        if ds_1[run_bin]['data'].keys()!=ds_2[run_bin]['data'].keys():
            print "ERROR: Different types of detectors in datasets. Please use .pkls with collections, which describe the same detectors"
            return False
        if ds_1[run_bin]['comment']:
            tot_coll[run_bin]={'run_start':ds_1[run_bin]['run_start'],
                                'run_stop':ds_1[run_bin]['run_stop'],
                                'comment':ds_1[run_bin]['comment'],
                                'data':{}}
        else:
            tot_coll[run_bin]={'run_start':ds_1[run_bin]['run_start'],
                                'run_stop':ds_1[run_bin]['run_stop'],
                                'data':{}}

        for st_id in ds_1[run_bin]['data']:
            if ds_1[run_bin]['data'][st_id].keys()!=ds_2[run_bin]['data'][st_id].keys():
                print "ERROR: Different structure of information in datasets. Please use .pkls which correspond to the same operation mode"
                return False
            tot_coll[run_bin]['data'][st_id]={}
            for val in ds_1[run_bin]['data'][st_id]:
                a = ds_1[run_bin]['data'][st_id][val]
                b = ds_2[run_bin]['data'][st_id][val]
                try:
                    tot_coll[run_bin]['data'][st_id][val]=eval(code)
                    #print "a = "+str(a)+", b = "+str(b)+"; "+formula+" = "+str(eval(code))
                except:
                    print "Failed to calculate formula for "+val+" for the sector "+str(st_id)
                    tot_coll[run_bin]['data'][st_id][val]=0
    with open(pkl_address+text_formula+'with_a_as_'+dataset_1.split('/')[-1].replace(".pkl","")+'_and_b_as_'+dataset_2.split('/')[-1].replace(".pkl","")+'.pkl', 'wb') as basket:
        pickle.dump(tot_coll, basket)                

    return True


if __name__ == "__main__":
    #local_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    if len(sys.argv)==4:
        formula = sys.argv[3]
        ds_1 = sys.argv[1]
        ds_2 = sys.argv[2]
        print "Evaluating formula "+formula
        PklAlgebra(ds_1, ds_2, formula)
    else:
        syntax_explanation("PklAlgebra.py")
       
