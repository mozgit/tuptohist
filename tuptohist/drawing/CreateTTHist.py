import pickle
from ROOT import gStyle
from ROOT import TColor
from ROOT import gROOT
import ROOT as R
import statistics
from TTMapping import TTMapping
from TTMapping import TTNumberOfSensors
from TTMapping import PlotTTBoxes
from TTMapping import PlotTTLabels
from Create_Maps import TT_Map as TT_Map_func
from config import TTMeanRange
from config import TTWidthRange
from config import TTEffRange
from config import UsePredefinedRanges
from config import UsePredefinedTitles
from config import TTMeanTitle
from config import TTWidthTitle
from config import TTEffTitle
from config import IncudeMissingSectorsToSummary
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
  - Number ("Value" mode)
  - Mean of the histogram ("Mean" mode)
  - R.M.S. of the histogram ("Sigma" mode)

  st_id is a 3-digit ID of a sector, which is defined in STTrackTuple algorithm. 
  The map between st_id and sector name can be found it Create_Maps.py file (or be obtained with TT_Map_func())
  """
  global TTMeanRange
  global TTWidthRange
  global TTEffRange
  global UsePredefinedRanges
  global UsePredefinedTitles
  global TTMeanTitle
  global TTWidthTitle
  global TTEffTitle
  global IncudeMissingSectorsToSummary
  first_lower = lambda s: s[:1].lower() + s[1:] if s else ''
  
  #Check if requested variable is in collection.
  variable_in_collection = False
  for st_id in data:
    if variable in data[st_id]:
      variable_in_collection = True
      break
  if not variable_in_collection:
    return False

  TT_Map = TT_Map_func()

  stations  = ["a", "b"]
  regions = ["A","B","C"]
  layers = ["X", "U", "V"]
  gROOT.SetStyle("Modern")
  gROOT.ForceStyle()

  gStyle.SetOptStat(0)
  gStyle.SetOptFit(0)
  gStyle.SetPadRightMargin(0.2)
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
  
  if (mode =="Mean") or (variable == "mean"):
    maximum = TTMeanRange[1]
    minimum = TTMeanRange[0]
    if UsePredefinedTitles:
      title = TTMeanTitle
    else:
      title = "Bias distribution, [mm]"
  elif (mode =="Sigma") or (variable == "width"):
    maximum = TTWidthRange[1]
    minimum = TTWidthRange[0]
    if UsePredefinedTitles:
      title = TTWidthTitle
    else:
      title = "Resolution, [mm]"
  elif variable == "efficiency":
    maximum = TTEffRange[1]
    minimum = TTEffRange[0]
    if UsePredefinedTitles:
      title = TTEffTitle
    else:
      title = "Hit efficiency"

  masked_sectors = []  
  vals = []

  hist  = R.TH2D("hist", title, nBinsX, lowX, upX, nBinsY, lowY, upY)
  if not test_mode:
    for st_id in data:
      for i in range (0, m_nSensors[st_id]):
          if mode =="Mean":
            hist.Fill(m_mapping[st_id][0], m_mapping[st_id][1]+i, data[st_id][variable].GetMean())
            if (i==0):
              if IncudeMissingSectorsToSummary:
                vals.append(data[st_id][variable].GetMean())
              else:
                if (data[st_id][variable].GetMean()<maximum) and (data[st_id][variable].GetMean()>minimum):
                  vals.append(data[st_id][variable].GetMean())
            if (i==0) and((maximum<data[st_id][variable].GetMean()) or (minimum>data[st_id][variable].GetMean())):
              masked_sectors.append(TT_Map[st_id])
              print "Atention, hit bias of sector "+TT_Map[st_id]+" is out of hist range. The value is "+str(data[st_id][variable].GetMean())
          elif mode =="Sigma":
            hist.Fill(m_mapping[st_id][0], m_mapping[st_id][1]+i, data[st_id][variable].GetRMS())
            if (i==0):
              if IncudeMissingSectorsToSummary:
                vals.append(data[st_id][variable].GetRMS())
              else:
                if (data[st_id][variable].GetRMS()<maximum) and (data[st_id][variable].GetRMS()>minimum):
                  vals.append(data[st_id][variable].GetRMS())
            if (i==0) and((maximum<data[st_id][variable].GetRMS()) or (minimum>data[st_id][variable].GetRMS())):
              masked_sectors.append(TT_Map[st_id])
              print "Atention, resolution of sector "+TT_Map[st_id]+" is out of hist range. The value is "+str(data[st_id][variable].GetRMS())
          elif mode =="Value":
            hist.Fill(m_mapping[st_id][0], m_mapping[st_id][1]+i, data[st_id][variable])
            if (i==0):
              if IncudeMissingSectorsToSummary:
                vals.append(data[st_id][variable])
              else:
                if (data[st_id][variable]<maximum) and (data[st_id][variable]>minimum):
                  vals.append(data[st_id][variable])
            if (i==0) and((maximum<data[st_id][variable]) or (minimum>data[st_id][variable])):
              masked_sectors.append(TT_Map[st_id])
              if variable == "efficiency":
                try:
                  print "Hit efficiency of sector "+TT_Map[st_id]+" is not shown since it is out of range ($\epsilon = "+str(data[st_id]["efficiency"]) + " \pm "+str(data[st_id]["err_efficiency"])+"$)."
                except:
                  print "Atention, "+variable+" of sector "+TT_Map[st_id]+" is out of hist range. The value is "+str(data[st_id][variable])
              else:
                print "Atention, "+variable+" of sector "+TT_Map[st_id]+" is out of hist range. The value is "+str(data[st_id][variable])
          else:
            print "Please use one of the following modes: Mean, Sigma, Value"
  
  
  c = R.TCanvas("c","c",600,600)

  if UsePredefinedRanges:
    hist.SetMaximum( maximum)
    hist.SetMinimum( minimum)

  hist.Draw("COLZ")
  #if test_mode:
    
  PlotTTBoxes(hist,nBinsX, lowX, upX, nBinsY, lowY, upY, masked_sectors)
  PlotTTLabels(hist)

  gStyle.SetOptStat(1111110)
  gStyle.SetOptFit(1111110)
  gROOT.ForceStyle()

  if not test_mode:
    c.SaveAs(address+variable+"_"+mode+"_TT_"+suffix+".pdf")
    c.SaveAs(address+variable+"_"+mode+"_TT_"+suffix+".C")


  gROOT.ProcessLine(".x lhcbStyle.C")
  #gStyle.SetPadRightMargin(0.1)
  #gStyle.SetPadLeftMargin(0.1)
  gStyle.SetOptStat('erm')  
  gROOT.ForceStyle()

  #lhcbStyle()
 
  try:
    from config import nBins_in_summary
    nBins = nBins_in_summary
  except:
    nBins = 50
    
  
  if (mode =="Mean") or (variable == "mean"):
    hist_summary  = R.TH1D("hist_summary", "TT "+first_lower(title)+"; Bias [mm];Number of sectors", nBins, min(vals), max(vals))
  elif (mode =="Sigma") or (variable == "width"):
    hist_summary  = R.TH1D("hist_summary", "TT "+first_lower(title)+"; Resolution [mm];Number of sectors", nBins, min(vals), max(vals))
  elif variable == "efficiency":
    hist_summary  = R.TH1D("hist_summary", "TT "+first_lower(title)+";Hit detection efficiency;Number of sectors", nBins, min(vals), max(vals))
  else:
    hist_summary  = R.TH1D("hist_summary", title, nBins, min(vals), max(vals))

  #hist_summary.GetYaxis().SetTitleOffset(1.2)
  #hist_summary.GetYaxis().SetLabelSize(0.03)
  #hist_summary.GetXaxis().SetLabelSize(0.03)
  for v in vals:
      hist_summary.Fill(v)

  
  c_s = R.TCanvas("c_s","c_s",800,800)

  hist_summary.Draw()

  R.gPad.Update()

  if variable == "efficiency":
      st = hist_summary.FindObject("stats")
      st.SetX1NDC(0.15)
      st.SetX2NDC(0.35)
      st.SetY1NDC(0.65)
      st.SetY2NDC(0.85)
  elif variable == "mean":
      st = hist_summary.FindObject("stats")
      st.SetX1NDC(0.65)
      st.SetX2NDC(0.85)
      st.SetY1NDC(0.65)
      st.SetY2NDC(0.85)
  elif variable == "width":
      st = hist_summary.FindObject("stats")
      st.SetX1NDC(0.78)
      st.SetX2NDC(0.98)
      st.SetY1NDC(0.65)
      st.SetY2NDC(0.85)


  R.gPad.Update()

  if not test_mode:
    c_s.SaveAs(address+"Summary_"+variable+"_"+mode+"_TT_"+suffix+".pdf")
    c_s.SaveAs(address+"Summary_"+variable+"_"+mode+"_TT_"+suffix+".C")
  print "Mean : "+str(statistics.mean(vals))+" +/- "+str(statistics.stdev(vals))
  print "Median : "+str(statistics.median(vals))
  gROOT.SetStyle("Modern")
  gROOT.ForceStyle()
  return c





if __name__ == "__main__":
  c = CreateTTHist(True, "unbiased_residual","Mean", "suffix","Plots/", True)
