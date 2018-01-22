class lcl:
  def __init__(self,region,classification,category,style,alt,values):
    self.region = region
    self.classification = classification
    self.category = category
    self.style = style
    self.alt = alt
    self.values = values
    
def aum_strategy(lcls):
  data = []
  for y in range(len(lcls[0].values)):
    ma = 0
    alt = 0
    cap = 0
    for j in range(len(lcls)):
      temp = lcls[j].values[y]
        if lcls[j].classification == "Equity":
          if lcls[j].alt == "Y":
            alt = alt + temp
          else:
            cap = cap + temp
        elif lcls[j].classification == "Multi Asset":
          if lcls[j].alt == "Y":
            alt = alt + temp
          else:
            ma = ma + temp
      data.append([ma,alt,cap])
    return data
    
def aum_vehicle(lcls):
  data = []
  for y in range(len(lcls[0].values)):
    unit = 0
    etf = 0
    for j in range(len(lcls)):
      temp = lcls[j].values[y]
      if lcls[j].style == "ETF":
        etf = etf + temp
      elif lcls[j].style == "Unit Trust":
        unit = unit + temp
    data.append([unit,etf])
  return data

def num_funds(lcls):
  data = []
  for y in range(len(lcls[0].values)):
    trad = 0
    rule = 0
    for j in range(len(lcls)):
      if lcls[j].classification == "Equity" or lcls[j].classification == "Multi Asset":
        if lcls[j].style == "Traditional":
          trad += 1
        elif lcls[j].style == "ETF" or lcls[j].style == "Unit Trust":
          rule += 1
    data.append([trad,rule])
  return data

def num_rules(lcls):
  data = []
  for y in range(len(lcls[0].values)):
    cap = 0 
    alt = 0
    ma = 0 
    for j in range(len(lcls)): 
      if lcls[j].style == "ETF" or lcls[j].style == "Unit Trust":   
        if lcls[j].classification == "Equity":  
          if lcls[j].alt == "Y":    
            alt += 1     
          else:    
            cap += 1  
        elif lcls[j].classification == "Multi Asset":   
          if lcls[j].alt == "Y":    
            alt += 1   
          else:   
            ma += 1   
      data.append([cap,alt,ma]) 
   return data

def aum_categories(lcls):
  data = []
  for y in range(len(lcls[0].values)):   
    equity = 0   
    foreign = 0
    multi = 0 
    real = 0 
    interest = 0  
    for j in range(len(lcls)):
      if lcls[j].region == "South Africa":   
        if lcls[j].classification == "Equity":  
          equity += 1    
        elif lcls[j].classification == "Multi Asset":  
          multi += 1   
        elif lcls[j].classification == "Real Estate": 
          real += 1 
        elif lcls[j].classification == "Interest Bearing": 
          interest += 1    
      elif lcls[j].region == "Global": 
        if lcls[j].classification == "Equity":   
          foregin += 1 
    data.append([equity,foreign,multi,real,interest])
  return data    

lcls = []
lcls.append(lcl("South Africa","Equity","General","Traditional","N",[10,12]))
lcls.append(lcl("South Africa","Equity","Large Cap","ETF","Y",[3, 8]))
lcls.append(lcl("South Africa","Multi Asset","High Equity","Unit Trust","N",[4, 5]))
lcls.append(lcl("South Africa","Multi Asset","High Equity","Traditional","N",[5, 8]))
print(aum_strategy(lcls))
print(aum_vehicle(lcls))
print(num_funds(lcls))
print(num_rules(lcls))
print(aum_categories(lcls))
