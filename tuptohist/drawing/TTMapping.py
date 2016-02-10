import ROOT as R
from Create_Maps import TT_Map as TT_Map_func

def TTMapping(st_id, verbose=False):

  uniqueSector = tt_unique_sector_map(st_id)
  TTlayer = int(str(uniqueSector)[0])
  Region =int(str(uniqueSector)[1])
  Sectorno_1 = uniqueSector-Region*100 - TTlayer*1000 - 1
 
  if (TTlayer == 1):
      XOffSet = -10.
      YOffSet = -9.
  elif (TTlayer == 2):
      XOffSet = 10.
      YOffSet = -9.
  elif (TTlayer == 3):
      XOffSet = -10.
      YOffSet = 9.
  else:
      XOffSet = 10.
      YOffSet = 9.
 
  seq4 = [0,4,3,3]
  seq6 = [0,4,2,1,1,2]
  compute=0
  if (TTlayer < 2.5):
      if(Region == 3):
          x = XOffSet + 7. - Sectorno_1/4
          compute = YOffSet - 7.
          for i in range (0, Sectorno_1%4+1):
              compute += seq4[i]
          y = compute + 0.5
          if verbose: print "Sector No "+str(uniqueSector)+"  x, y:  "+str(x)+" , "+str(y)
          return [x,y]
      elif (Region == 1):
          x = XOffSet - 2. - Sectorno_1/4
          compute = YOffSet - 7.
          for i in range(0,Sectorno_1%4+1):
              compute += seq4[i];
          y = compute + 0.5;
          if verbose: print "Sector No "+str(uniqueSector)+"  x, y:  "+str(x)+" , "+str(y)
          return [x,y]
      else:
          x = XOffSet + 1. - Sectorno_1/6
          compute = YOffSet - 7.
          for i in range(0,Sectorno_1%6+1):
              compute += seq6[i]
          y = compute + 0.5
          if verbose: print "Sector No "+str(uniqueSector)+"  x, y:  "+str(x)+" , "+str(y)
          return [x,y]
  else:
      if (Region == 3):
          x = XOffSet + 8. - Sectorno_1/4
          compute = YOffSet - 7.
          for i in range (0, Sectorno_1%4+1):
              compute += seq4[i]
          y = compute + 0.5
          if verbose: print "Sector No "+str(uniqueSector)+"  x, y:  "+str(x)+" , "+str(y)
          return [x,y]
      elif(Region == 1):
          x = XOffSet - 3. - Sectorno_1/4
          compute = YOffSet - 7.
          for i in range(0, Sectorno_1%4+1):
              compute += seq4[i]
          y = compute + 0.5
          if verbose: print "Sector No "+str(uniqueSector)+"  x, y:  "+str(x)+" , "+str(y)
          return [x,y]
      else:
          if (Sectorno_1 < 4):
            x = XOffSet + 2. - Sectorno_1/4
            compute = YOffSet - 7.
            for i in range(0, Sectorno_1%4+1):
                compute += seq4[i];
            y = compute + 0.5
            if verbose: print "Sector No "+str(uniqueSector)+"  x, y:  "+str(x)+" , "+str(y)
            return [x, y]
          elif (Sectorno_1 > 21):
            Sectorno_1 -= 22
            x = XOffSet - 2. - Sectorno_1/4
            compute = YOffSet - 7.
            for i in range(0, Sectorno_1%4+1):
                compute += seq4[i]
            y = compute + 0.5
            if verbose: print "Sector No "+str(uniqueSector)+"  x, y:  "+str(x)+" , "+str(y)
            return [x,y]
          else:
            Sectorno_1 -= 4
            x = XOffSet + 1. - Sectorno_1/6
            compute = YOffSet - 7.
            for i in range (0, Sectorno_1%6+1):
                compute += seq6[i]
            y = compute + 0.5
            if verbose: print "Sector No "+str(uniqueSector)+"  x, y:  "+str(x)+" , "+str(y)
            return [x,y]


def TTNumberOfSensors(st_id):
  uniqueSector = tt_unique_sector_map(st_id)
  TTlayer = int(str(uniqueSector)[0])
  Region =int(str(uniqueSector)[1])
  Sectorno_1 = uniqueSector-Region*100 - TTlayer*1000 - 1
 
  if(TTlayer < 2.5):
    if(Region == 3):
      if(Sectorno_1%4 == 0 or Sectorno_1%4 == 3):
        return 4
      else:
        return 3
    elif(Region == 1):
      if(Sectorno_1%4 == 0 or Sectorno_1%4 == 3):
        return 4
      else:
        return 3
    else:
      if(Sectorno_1%6 == 0 or Sectorno_1%6 == 5):
        return 4
      elif(Sectorno_1%6 == 1 or Sectorno_1%6 == 4):
        return 2
      else:
        return 1
  else:
    if(Region == 3):
      if(Sectorno_1%4 == 0 or Sectorno_1%4 == 3):
        return 4
      else:
        return 3
    elif(Region == 1):
      if(Sectorno_1%4 == 0 or Sectorno_1%4 == 3):
        return 4
      else:
        return 3
    else:
      if(Sectorno_1 < 4):
        if(Sectorno_1%4 == 0 or Sectorno_1%4 == 3):
          return 4
        else:
          return 3
      elif(Sectorno_1 > 21):
        Sectorno_1 -= 22
        if(Sectorno_1%4 == 0 or Sectorno_1%4 == 3):
          return 4
        else:
          return 3
      else:
        Sectorno_1 -= 4
        if(Sectorno_1%6 == 0 or Sectorno_1%6 == 5):
          return 4
        elif(Sectorno_1%6 == 1 or Sectorno_1%6 == 4):
          return 2
        else:
          return 1
      
    
def PlotTTBoxes(hist, nBinsX, lowX, upX, nBinsY, lowY, upY):
  box = R.TBox()
  box.SetFillColor(R.kWhite)
  box.SetFillStyle(0)
  box.SetLineStyle(3)
  box.SetLineColor(R.kBlack)
  #box.SetLineWidth(box.GetLineWidth()/10.)
 
  boxempty = R.TBox()
  boxempty.SetFillColor(14)
  boxempty.SetFillStyle(3254)
  boxempty.SetLineStyle(3)
  boxempty.SetLineColor(14)
  #boxempty.SetLineWidth(boxempty.GetLineWidth()/100.)

  boxwhite = R.TBox()
  boxwhite.SetFillColor(R.kWhite)
  boxwhite.SetFillStyle(1001)
  boxwhite.SetLineStyle(1)
  boxwhite.SetLineColor(R.kWhite)  
 
  #with open('TT_Map.pkl', 'r') as basket:
  #  TT_Map = pickle.load(basket)
  TT_Map = TT_Map_func()

  x_white = float(upX-lowX)/nBinsX
  y_white = float(upY-lowY)/nBinsY

  active_sectors = []
  for st_id in TT_Map.values():
    for i in range(0, TTNumberOfSensors(st_id)):
      active_sectors.append([TTMapping(st_id)[0],TTMapping(st_id)[1]+i])
  for i in range(0, nBinsX):
    for j in range(0, nBinsY):
      if [lowX+x_white*i+0.5, lowY+y_white*j+0.5] not in active_sectors:
        boxwhite.DrawBox(lowX+x_white*i, lowY+y_white*j, lowX+x_white*(i+1), lowY+y_white*(j+1))


  for st_id in TT_Map.values():
    box.DrawBox(TTMapping(st_id)[0]-0.5,TTMapping(st_id)[1]-0.5, TTMapping(st_id)[0]+0.5,TTMapping(st_id)[1]+0.5+TTNumberOfSensors(st_id)-1.)
    if(hist.GetBinContent( hist.GetXaxis().FindBin(TTMapping(st_id)[0]), hist.GetYaxis().FindBin(TTMapping(st_id)[1]) )==0):
      boxwhite.DrawBox(TTMapping(st_id)[0]-0.5,TTMapping(st_id)[1]-0.5, TTMapping(st_id)[0]+0.5,TTMapping(st_id)[1]+0.5+TTNumberOfSensors(st_id)-1.)
      boxempty.DrawBox(TTMapping(st_id)[0]-0.5,TTMapping(st_id)[1]-0.5, TTMapping(st_id)[0]+0.5,TTMapping(st_id)[1]+0.5+TTNumberOfSensors(st_id)-1.)

def PlotTTLabels(hist): 
  hist.GetXaxis().SetTickLength(0)
  hist.GetYaxis().SetTickLength(0)
  hist.GetXaxis().SetLabelColor(R.kWhite)
  hist.GetYaxis().SetLabelColor(R.kWhite)
 
  tta =R.TText()
  tta.DrawText(-0.75, -9.8, "TTa")
 
  ttb = R.TText()
  ttb.DrawText(-0.75, 8., "TTb")
 
  ttaX = R.TText()
  ttaX.DrawText(-19.8, -9., "X")
 
  ttaU = R.TText()
  ttaU.DrawText(19.3, -9., "U")
 
  ttbV = R.TText()
  ttbV.DrawText(-19.8, 8., "V")
 
  ttbX = R.TText()
  ttbX.DrawText(19.3, 8., "X")
 
  ttA = R.TText()
  ttA.SetTextSize(0.07)
  ttA.DrawText(-20.8, -0.5, "A")
 
  ttC = R.TText()
  ttC.SetTextSize(0.07)
  ttC.DrawText(19.8, -0.5, "C")
 
  XArrow = R.TArrow()
  XArrow.DrawArrow(0.,-18.,-8.5,-18.,0.005,"|-|>")
 
  X =R.TText()
  X.SetTextSize(0.04)
  X.DrawText(-9.1, -19., "X")
 
  #with open('TT_Map.pkl', 'r') as basket:
  #  TT_Map = pickle.load(basket)
  TT_Map = TT_Map_func()
  for st_id in TT_Map:    
    tt = R.TText()
    tt.SetTextSize(0.015)
    tt.SetTextAngle(90)
    tt.DrawText(TTMapping(TT_Map[st_id])[0]-0.25, TTMapping(TT_Map[st_id])[1]+0.45*(TTNumberOfSensors(TT_Map[st_id])-1), str(st_id))
  return True 

def tt_unique_sector_map(sector):
    m_sector   = sector
    m_station  = sector[2]
    m_layer    = sector[3]
    m_region   = sector[10]
    m_sectorID = int(sector.split("Sector")[1])


    m_uniqueSector = 0
    if( m_station=="a" and m_layer=="X"): m_uniqueSector += 1000
    elif( m_station=="a" and (m_layer=="U" or m_layer=="V") ): m_uniqueSector += 2000
    elif( m_station=="b" and (m_layer=="U" or m_layer=="V") ): m_uniqueSector += 3000
    elif( m_station=="b" and  m_layer=="X" ): m_uniqueSector += 4000
 
    if( m_region=="A" ): m_uniqueSector += 100
    elif( m_region=="B" ): m_uniqueSector += 200
    elif( m_region=="C" ): m_uniqueSector += 300

    m_uniqueSector += m_sectorID

    return m_uniqueSector
