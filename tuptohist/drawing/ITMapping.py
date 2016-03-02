import ROOT as R
from Create_Maps import IT_Map as IT_Map_func

def ITMapping(st_id):
    uniqueSector = it_unique_sector_map(st_id)
    Itno = int(str(uniqueSector)[0])
    Boxno = int(str(uniqueSector)[1])
    Layerno = int(str(uniqueSector)[2])
    Sectorno = int(str(uniqueSector)[3])

    if(Boxno == 1):
        x = -3. - Sectorno
        y = (16.*(Itno-1.)+7.+Layerno)/2. -13. + 0.25
        return [x,y]
    elif(Boxno == 2):
        x = 11. - Sectorno
        y = (16.*(Itno-1.)+7.+Layerno)/2. -13. + 0.25
        return [x,y]
    elif(Boxno == 3):
        x = 4. - Sectorno
        y = (16.*(Itno-1.)+11.+Layerno)/2. -13. + 0.25
        return [x,y]
    else:
        x = 4. - Sectorno
        y = (16.*(Itno-1.)+3.+Layerno)/2. -13. + 0.25
        return[x,y]


def PlotITBoxes(hist, nBinsX, lowX, upX, nBinsY, lowY, upY, masked_sectors):
  box = R.TBox()
  box.SetFillColor(R.kBlack)
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

  #with open('IT_Map.pkl', 'r') as basket:
  #  IT_Map = pickle.load(basket)
  IT_Map = IT_Map_func()

  x_white = float(upX-lowX)/nBinsX
  y_white = float(upY-lowY)/nBinsY

  active_sectors = []
  for st_id in IT_Map.values():
    active_sectors.append(ITMapping(st_id))
  for i in range(0, nBinsX):
    for j in range(0, nBinsY):
      if [lowX+x_white*i+0.5, lowY+y_white*j+0.25] not in active_sectors:
        boxwhite.DrawBox(lowX+x_white*i, lowY+y_white*j, lowX+x_white*(i+1), lowY+y_white*(j+1))

  for st_id in IT_Map.values():
    box.DrawBox(ITMapping(st_id)[0]-0.5,ITMapping(st_id)[1]-0.25, ITMapping(st_id)[0]+0.5,ITMapping(st_id)[1]+0.25)
    #if(hist.GetBinContent( hist.GetXaxis().FindBin(ITMapping(st_id)[0]), hist.GetYaxis().FindBin(ITMapping(st_id)[1]) )==0):
      #boxwhite.DrawBox(ITMapping(st_id)[0]-0.5,ITMapping(st_id)[1]-0.25, ITMapping(st_id)[0]+0.5,ITMapping(st_id)[1]+0.25)
      #boxempty.DrawBox(ITMapping(st_id)[0]-0.5,ITMapping(st_id)[1]-0.25, ITMapping(st_id)[0]+0.5,ITMapping(st_id)[1]+0.25)
    if st_id in masked_sectors:
      boxwhite.DrawBox(ITMapping(st_id)[0]-0.5,ITMapping(st_id)[1]-0.25, ITMapping(st_id)[0]+0.5,ITMapping(st_id)[1]+0.25)
      boxempty.DrawBox(ITMapping(st_id)[0]-0.5,ITMapping(st_id)[1]-0.25, ITMapping(st_id)[0]+0.5,ITMapping(st_id)[1]+0.25)


  return True
 
def PlotITLabels(hist):
  hist.GetXaxis().SetTickLength(0)
  hist.GetYaxis().SetTickLength(0)
  hist.GetXaxis().SetLabelColor(R.kBlack)
  hist.GetYaxis().SetLabelColor(R.kBlack)
  it1 = R.TText()
  it1.DrawText(-1., -8.5, "IT1")
  it2 = R.TText()
  it2.DrawText(-1., -0.5, "IT2")
  it3 = R.TText()
  it3.DrawText(-1., 7.5, "IT3")
  itA = R.TText()
  itA.SetTextSize(0.05)
  itA.DrawText(-12, -0.5, "A")
  itC = R.TText()
  itC.SetTextSize(0.05)
  itC.DrawText(11.5, -0.5, "C")
  XArrow = R.TArrow()
  XArrow.DrawArrow(3.,-12.,-3.,-12.,0.005,"|-|>")
  X = R.TText()
  X.SetTextSize(0.04)
  X.DrawText(-4, -12.5, "X")
 
  set1=[[10.7,-9],[10.7,-1],[10.7, 7]]
  for s in set1:
    x = s[0]
    y = s[1]
    itX1 = R.TText()
    itX1.SetTextSize(0.02)
    itX1.DrawText(x, y, "X1")
    itU = R.TText()
    itU.SetTextSize(0.02)
    itU.DrawText(x, y+0.5, "U")
    itV = R.TText()
    itV.SetTextSize(0.02)
    itV.DrawText(x, y+1.0, "V")
    itX2 = R.TText()
    itX2.SetTextSize(0.02)
    itX2.DrawText(x, y+1.5, "X2")
  set2 = [[10,  1.2],[ 3, 11.2],[ 3,-11.65],[-4,  1.2]] 
  for s in set2:
    x = s[0]
    y = s[1]
    itno1 = R.TText()
    itno1.SetTextSize(0.02)
    itno1.DrawText(x, y, "1")
    itno2 = R.TText()
    itno2.SetTextSize(0.02)
    itno2.DrawText(x-1, y, "2")
    itno3 = R.TText()
    itno3.SetTextSize(0.02)
    itno3.DrawText(x-2, y, "3")
    itno4 = R.TText()
    itno4.SetTextSize(0.02)
    itno4.DrawText(x-3, y, "4")
    itno5 = R.TText()
    itno5.SetTextSize(0.02)
    itno5.DrawText(x-4, y, "5")
    itno6 = R.TText()
    itno6.SetTextSize(0.02)
    itno6.DrawText(x-5, y, "6")
    itno7 = R.TText()
    itno7.SetTextSize(0.02)
    itno7.DrawText(x-6, y, "7")
  return True

 
def it_unique_sector_map(sector):
  m_sector = sector
  m_stationID= int(sector[2])
  m_sectorID = int(sector.split("Sector")[1])
 
  if "ASide" in sector: m_box = "ASide"
  if "CSide" in sector: m_box = "CSide"
  if "Top" in sector: m_box = "Top"
  if "Bottom" in sector: m_box = "Bottom"
 

  if "X1" in sector: m_layer = "X1"
  if "X2" in sector: m_layer = "X2"
  if "U" in sector: m_layer = "U"
  if "V" in sector: m_layer = "V"
 
  m_uniqueSector = 0
  if( m_stationID==1 ): m_uniqueSector += 1000
  elif( m_stationID==2 ): m_uniqueSector += 2000
  elif( m_stationID==3 ): m_uniqueSector += 3000
 
  if  "ASide" in sector : m_uniqueSector += 100
  elif  "CSide" in sector : m_uniqueSector += 200
  elif  "Top" in sector : m_uniqueSector += 300
  elif  "Bottom" in sector : m_uniqueSector += 400
 

  if  "X1" in sector: m_uniqueSector += 10
  elif  "U" in sector: m_uniqueSector += 20
  elif  "V" in sector: m_uniqueSector += 30
  elif  "X2" in sector: m_uniqueSector += 40
 
  m_uniqueSector += m_sectorID
 
  return m_uniqueSector
