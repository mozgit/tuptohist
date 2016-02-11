import pickle
from ROOT import gStyle
from ROOT import TColor
from ROOT import gROOT
import ROOT as R
from ITMapping import ITMapping
from ITMapping import PlotITBoxes
from ITMapping import PlotITLabels
from Create_Maps import IT_Map as IT_Map_func
from config import ITMeanRange
from config import ITWidthRange
from config import ITEffRange
from config import UsePredefinedRanges

from array import array


def CreateITHist(data,variable, mode, suffix, address="Plots/", test_mode=False):
  """
  This finction creates map of the IT from given dictionary.
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
  The map between st_id and sector name can be found it Create_Maps.py file (or be obtained with IT_Map_func())
  """


  global ITMeanRange
  global ITWidthRange
  global ITEffRange
  global UsePredefinedRanges

 
  stats = ["1","2","3"]
  boxes = ["ASide","CSide","Top","Bottom"]
  layers = ["X1", "U", "V", "X2"]
  sectors = ["1","2","3","4","5","6","7"]

  IT_Map = IT_Map_func()

  gStyle.SetOptStat(0)
  gStyle.SetOptFit(0)
  gStyle.SetPadRightMargin(0.2)
  gStyle.SetTitleX(0.5)
  gStyle.SetTitleAlign(23)
  gStyle.SetTitleBorderSize(0)
  gStyle.SetPaintTextFormat("5.1f")
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

  for st_id in IT_Map:
    m_mapping[st_id]=ITMapping(IT_Map[st_id])

  if mode =="Mean":
    maximum = ITMeanRange[1]
    minimum = ITMeanRange[0]
    title = "Bias distribution, [mm]"
  elif mode =="Sigma":
    maximum = ITWidthRange[1]
    minimum = ITWidthRange[0]
    title = "Resolution, [mm]"
  elif mode =="Eff":
    maximum = ITEffRange[1]
    minimum = ITEffRange[0]
    title = "Hit efficiency"

  nBinsX = 25
  nBinsY = 52
  lowX = -12.5
  upX  =  12.5
  lowY = -13
  upY  =  13
  hist = R.TH2D("hist", title, nBinsX, lowX, upX, nBinsY, lowY, upY)
  if not test_mode:
    for st_id in data:
      if mode =="Mean":
        hist.Fill(m_mapping[st_id][0], m_mapping[st_id][1], data[st_id][variable].GetMean())
        if (maximum<data[st_id][variable].GetMean()) or (minimum>data[st_id][variable].GetMean()):
          print "Atention, hit bias of sector "+IT_Map[st_id]+" is out of hist range. The value is "+str(data[st_id][variable].GetMean())
      elif mode =="Sigma":
        hist.Fill(m_mapping[st_id][0], m_mapping[st_id][1], data[st_id][variable].GetRMS())
        if (maximum<data[st_id][variable].GetRMS()) or (minimum>data[st_id][variable].GetRMS()):
          print "Atention, resolution of sector "+IT_Map[st_id]+" is out of hist range. The value is "+str(data[st_id][variable].GetRMS())
      elif mode =="Eff":
        hist.Fill(m_mapping[st_id][0], m_mapping[st_id][1], data[st_id][variable])
        if (maximum<data[st_id][variable]) or (minimum>data[st_id][variable]):
          print "Atention, hit efficiency of sector "+IT_Map[st_id]+" is out of hist range. The value is "+str(data[st_id][variable])
      else:
        print "Please use one of the following modes: Mean, Sigma, Eff"
  
  c = R.TCanvas("c","c",600,600)

  if UsePredefinedRanges:
    hist.SetMaximum( maximum)
    hist.SetMinimum( minimum)
  hist.Draw("COLZ")

  #if test_mode:
  
  PlotITBoxes(hist, nBinsX, lowX, upX, nBinsY, lowY, upY)
  PlotITLabels(hist)

  gStyle.SetOptStat(1111110)
  gStyle.SetOptFit(1111110)
  gROOT.ForceStyle()
  if not test_mode:
    c.SaveAs(address+mode+"_IT_"+suffix+".pdf")
    c.SaveAs(address+mode+"_IT_"+suffix+".C")
  return c
 
if __name__ == "__main__":
  c = CreateITHist(True, "Mean", "suffix","Plots/",True)

