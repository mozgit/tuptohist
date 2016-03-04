import pickle
from ROOT import gStyle
from ROOT import TColor
from ROOT import gROOT
import ROOT as R
import statistics
from ITMapping import ITMapping
from ITMapping import PlotITBoxes
from ITMapping import PlotITLabels
from Create_Maps import IT_Map as IT_Map_func
from config import ITMeanRange
from config import ITWidthRange
from config import ITEffRange
from config import UsePredefinedRanges
from config import UsePredefinedTitles
from config import ITMeanTitle
from config import ITWidthTitle
from config import ITEffTitle
from config import IncudeMissingSectorsToSummary
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
  - Number ("Value" mode)
  - Mean of the histogram ("Mean" mode)
  - R.M.S. of the histogram ("Sigma" mode)

  st_id is a 3-digit ID of a sector, which is defined in STTrackTuple algorithm. 
  The map between st_id and sector name can be found it Create_Maps.py file (or be obtained with IT_Map_func())
  """


  global ITMeanRange
  global ITWidthRange
  global ITEffRange
  global UsePredefinedRanges
  global UsePredefinedTitles
  global ITMeanTitle
  global ITWidthTitle
  global ITEffTitle
  global IncudeMissingSectorsToSummary
  #Check if requested variable is in collection.
  variable_in_collection = False
  for st_id in data:
    if variable in data[st_id]:
      variable_in_collection = True
      break
  if not variable_in_collection:
    return False

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
  
  if (mode =="Mean") or (variable == "mean"):
    maximum = ITMeanRange[1]
    minimum = ITMeanRange[0]
    if UsePredefinedTitles:
      title = ITMeanTitle
    else:
      title = "Bias distribution, [mm]"
  elif (mode =="Sigma") or (variable == "width"):
    maximum = ITWidthRange[1]
    minimum = ITWidthRange[0]
    if UsePredefinedTitles:
      title = ITWidthTitle
    else:
      title = "Resolution, [mm]"
  elif variable == "efficiency":
    maximum = ITEffRange[1]
    minimum = ITEffRange[0]
    if UsePredefinedTitles:
      title = ITEffTitle
    else:
      title = "Hit efficiency"
  
  nBinsX = 25
  nBinsY = 52
  lowX = -12.5
  upX  =  12.5
  lowY = -13
  upY  =  13
  hist = R.TH2D("hist", title, nBinsX, lowX, upX, nBinsY, lowY, upY)
  masked_sectors = []
  vals = []
  if not test_mode:
    for st_id in data:
      if mode =="Mean":
        hist.Fill(m_mapping[st_id][0], m_mapping[st_id][1], data[st_id][variable].GetMean())
        if IncudeMissingSectorsToSummary:
          vals.append(data[st_id][variable].GetMean())        
        else:
          if (data[st_id][variable].GetMean()<maximum) and (data[st_id][variable].GetMean()>minimum):
            vals.append(data[st_id][variable].GetMean())        
        if (maximum<data[st_id][variable].GetMean()) or (minimum>data[st_id][variable].GetMean()):
          masked_sectors.append(IT_Map[st_id])
          print "Atention, hit bias of sector "+IT_Map[st_id]+" is out of hist range. The value is "+str(data[st_id][variable].GetMean())
      elif mode =="Sigma":
        hist.Fill(m_mapping[st_id][0], m_mapping[st_id][1], data[st_id][variable].GetRMS())
        if IncudeMissingSectorsToSummary:
          vals.append(data[st_id][variable].GetRMS())        
        else:
          if (data[st_id][variable].GetRMS()<maximum) and (data[st_id][variable].GetRMS()>minimum):
            vals.append(data[st_id][variable].GetRMS())        
        if (maximum<data[st_id][variable].GetRMS()) or (minimum>data[st_id][variable].GetRMS()):
          masked_sectors.append(IT_Map[st_id])
          print "Atention, resolution of sector "+IT_Map[st_id]+" is out of hist range. The value is "+str(data[st_id][variable].GetRMS())
      elif mode =="Value":
        hist.Fill(m_mapping[st_id][0], m_mapping[st_id][1], data[st_id][variable])
        if IncudeMissingSectorsToSummary:
          vals.append(data[st_id][variable])
        else:
          if (data[st_id][variable]<maximum) and (data[st_id][variable]>minimum):
            vals.append(data[st_id][variable])
        if (maximum<data[st_id][variable]) or (minimum>data[st_id][variable]):
          masked_sectors.append(IT_Map[st_id])
          if variable == "efficiency":
            try:
              print "Hit efficiency of sector "+IT_Map[st_id]+" is not shown since it is out of range ($\epsilon = "+str(data[st_id]["efficiency"]) + " \pm "+str(data[st_id]["err_efficiency"])+"$)."
            except:
              print "Atention, "+variable+" of sector "+IT_Map[st_id]+" is out of hist range. The value is "+str(data[st_id][variable])
          else:
            print "Atention, "+variable+" of sector "+IT_Map[st_id]+" is out of hist range. The value is "+str(data[st_id][variable])
      else:
        print "Please use one of the following modes: Mean, Sigma, Value"
  
  c = R.TCanvas("c","c",600,600)

  if UsePredefinedRanges:
    hist.SetMaximum( maximum)
    hist.SetMinimum( minimum)
  hist.Draw("COLZ")

  #if test_mode:
  
  PlotITBoxes(hist, nBinsX, lowX, upX, nBinsY, lowY, upY, masked_sectors)
  PlotITLabels(hist)

  gStyle.SetOptStat(1111110)
  gStyle.SetOptFit(1111110)
  gROOT.ForceStyle()
  if not test_mode:
    c.SaveAs(address+variable+"_"+mode+"_IT_"+suffix+".pdf")
    c.SaveAs(address+variable+"_"+mode+"_IT_"+suffix+".C")

  gStyle.SetOptStat('erm')  
  gROOT.ForceStyle()
  first_lower = lambda s: s[:1].lower() + s[1:] if s else ''
  hist_summary  = R.TH1D("hist_summary", "Summary of "+first_lower(title), 100, min(vals), max(vals))
  for v in vals:
      hist_summary.Fill(v)

  c_s = R.TCanvas("c_s","c_s",600,600)
  hist_summary.Draw()
  if not test_mode:
    c_s.SaveAs(address+"Summary_"+variable+"_"+mode+"_IT_"+suffix+".pdf")
    c_s.SaveAs(address+"Summary_"+variable+"_"+mode+"_IT_"+suffix+".C")
  print "Mean : "+str(statistics.mean(vals))
  print "Median : "+str(statistics.median(vals))

  return c
 
if __name__ == "__main__":
  c = CreateITHist(True, "Mean", "suffix","Plots/",True)

