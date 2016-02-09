import pickle
from ROOT import gStyle
from ROOT import TColor
from ROOT import gROOT
import ROOT as R
from ITMapping import ITMapping
from ITMapping import PlotITBoxes
from ITMapping import PlotITLabels
from Create_Maps import IT_Map as IT_Map_func


from array import array

def CreateITHist(data, mode, suffix, address="Plots/", test_mode=False):
 
  stats = ["1","2","3"]
  boxes = ["ASide","CSide","Top","Bottom"]
  layers = ["X1", "U", "V", "X2"]
  sectors = ["1","2","3","4","5","6","7"]

  IT_Map = IT_Map_func()

  gStyle.SetOptStat(0)
  gStyle.SetOptFit(0)
  gStyle.SetPadRightMargin(0.25)
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
    maximum = 0.1
    minimum = -0.1
    title = "Bias distribution, [mm]"
  elif mode =="Sigma":
    maximum = 0.1
    minimum = 0
    title = "Resolution, [mm]"
  elif mode =="Eff":
    maximum = 1.05
    minimum = 0.8
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
        hist.Fill(m_mapping[st_id][0], m_mapping[st_id][1], data[st_id]["unbiased_residual"].GetMean())
      elif mode =="Sigma":
        hist.Fill(m_mapping[st_id][0], m_mapping[st_id][1], data[st_id]["unbiased_residual"].GetRMS())
      elif mode =="Eff":
        hist.Fill(m_mapping[st_id][0], m_mapping[st_id][1], data[st_id]["efficiency"])
      else:
        print "Please use one of the following modes: Mean, Sigma, Eff"
  
  c = R.TCanvas("c","c",600,600)
  #hist.SetMaximum( maximum)
  #hist.SetMinimum( minimum)
  hist.Draw("COLZ")
  if test_mode:
    PlotITLabels(hist)
  PlotITBoxes(hist)

  gStyle.SetOptStat(1111110)
  gStyle.SetOptFit(1111110)
  gROOT.ForceStyle()
  if not test_mode:
    c.SaveAs(address+mode+"_IT_"+suffix+".pdf")
  return c
 
if __name__ == "__main__":
  c = CreateITHist(True, "Mean", "suffix","Plots/",True)

