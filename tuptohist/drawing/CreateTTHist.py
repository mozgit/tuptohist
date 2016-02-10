import pickle
from ROOT import gStyle
from ROOT import TColor
from ROOT import gROOT
import ROOT as R
from TTMapping import TTMapping
from TTMapping import TTNumberOfSensors
from TTMapping import PlotTTBoxes
from TTMapping import PlotTTLabels
from Create_Maps import TT_Map as TT_Map_func
from config import TTMeanRange
from config import TTWidthRange
from config import TTEffRange
from config import UsePredefinedRanges

from array import array

def CreateTTHist(data, variable,  mode, suffix, address="Plots/", test_mode = False):
  """
  This finction creates map of the TT from given dictionary.
  Dictionary whould have a form:
  data = {<st_id1>:{
                    <variable>:<number or TH1>
                    },
          <st_id2>:{},
          ...}
  depending on mode, the function will create a map according to the:
  - Number ("Eff" mode)
  - Mean of the histogram ("Mean" mode)
  - R.M.S. of the histogram ("Sigma" mode)

  st_id is a 3-digit ID of a sector, which is defined in STTrackTuple algorithm. 
  The map between st_id and sector name can be found it Create_Maps.py file (or be obtained with TT_Map_func())
  """
  global TTMeanRange
  global TTWidthRange
  global TTEffRange
  global UsePredefinedRanges
  
  TT_Map = TT_Map_func()

  stations  = ["a", "b"]
  regions = ["A","B","C"]
  layers = ["X", "U", "V"]


  gStyle.SetOptStat(0)
  gStyle.SetOptFit(0)
  gStyle.SetPadRightMargin(0.25)
  gStyle.SetTitleX(0.5)
  gStyle.SetTitleAlign(23)
  gStyle.SetTitleBorderSize(0)
  gStyle.SetPaintTextFormat("5.0f")
  gStyle.SetStatFormat("5.5f")
  gStyle.SetTitleFontSize(0.07)
  gStyle.SetPadTickY(1)
  gStyle.SetPadTickX(1)
  nColors=52
  MyPalette = [0]*nColors
  stops = [0.00, 0.50, 1.00]
  red = [0.80, 1.00, 0.00]
  green = [0.00, 1.00, 0.00]
  blue = [0.00, 1.00, 0.80]
  s = array('d', stops)
  r   = array('d', red)
  g = array('d', green)
  b  = array('d', blue)
  FI = TColor.CreateGradientColorTable(3, s, r, g, b, nColors);
  for k in range(0, nColors):
    MyPalette[k] = FI+k
  
  
  gStyle.SetNumberContours(nColors)
  gStyle.SetPalette(nColors, array('i',MyPalette))
  gROOT.ForceStyle()
 
  m_mapping={}
  m_nSensors={}

  for st_id in TT_Map:
    m_mapping[st_id]=TTMapping(TT_Map[st_id])
    m_nSensors[st_id] = TTNumberOfSensors(TT_Map[st_id])
 
  nBinsX = 43
  nBinsY = 40
  lowX = -21.5
  upX  =  21.5
  lowY = -20
  upY  =  20
  
  if mode =="Mean":
    maximum = TTMeanRange[1]
    minimum = TTMeanRange[0]
    title = "Bias distribution, [mm]"
  elif mode =="Sigma":
    maximum = TTWidthRange[1]
    minimum = TTWidthRange[0]
    title = "Resolution, [mm]"
  elif mode =="Eff":
    maximum = TTEffRange[1]
    minimum = TTEffRange[0]
    title = "Hit efficiency"
  

  hist  = R.TH2D("hist", title, nBinsX, lowX, upX, nBinsY, lowY, upY)
  if not test_mode:
    for st_id in data:
      for i in range (0, m_nSensors[st_id]):
          if mode =="Mean":
            hist.Fill(m_mapping[st_id][0], m_mapping[st_id][1]+i, data[st_id][variable].GetMean())
          elif mode =="Sigma":
            hist.Fill(m_mapping[st_id][0], m_mapping[st_id][1]+i, data[st_id][variable].GetRMS())
          elif mode =="Eff":
            hist.Fill(m_mapping[st_id][0], m_mapping[st_id][1]+i, data[st_id][variable])
          else:
            print "Please use one of the following modes: Mean, Sigma, Eff"
  
  c = R.TCanvas("c","c",600,600)

  if UsePredefinedRanges:
    hist.SetMaximum( maximum)
    hist.SetMinimum( minimum)

  hist.Draw("COLZ")
  if test_mode:
    PlotTTLabels(hist)
  PlotTTBoxes(hist,nBinsX, lowX, upX, nBinsY, lowY, upY)

  gStyle.SetOptStat(1111110)
  gStyle.SetOptFit(1111110)
  gROOT.ForceStyle()

  if not test_mode:
    c.SaveAs(address+mode+"_TT_"+suffix+".pdf")
    c.SaveAs(address+mode+"_TT_"+suffix+".C")
  return c

if __name__ == "__main__":
  c = CreateTTHist(True, "unbiased_residual","Mean", "suffix","Plots/", True)
