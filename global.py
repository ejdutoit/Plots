class glb:
  def __init__(self,region,classification,index,values):
    self.region = region    
    self.classification = classification    
    self.index = index    
    self.values = values
    
def index_vals(glbs):    
  data = []    
  regions = ["USA","Asia"]    
  for i in range(len(regions)):    
    ind = 0     
    ind_non = 0     
    total = 0         
    for j in range(len(glbs)):      
      if glbs[j].region == regions[i]:        
        temp = glbs[j].values[-1]        
        if glbs[j].index == "Index":          
          ind = ind + temp        
        else:          
          ind_non = ind_non + temp        
        total = total + temp    
    data.append([ind/total, ind_non/total])    
  return data
  
def years_vals(glbs):    
  data = []    
  for y in range(len(glbs[0].values)):        
    ind = 0     
    ind_non = 0     
    total = 0         
    for j in range(len(glbs)):      
      temp = glbs[j].values[y]      
      if glbs[j].index == "Index":        
        ind = ind + temp      
      else:        
        ind_non = ind_non + temp      
      total = total + temp    
    data.append([ind/total,ind_non/total])    
  return data
  
glbs = []
glbs.append(glb("USA","Tech","Index",[11,12]))glbs.append(glb("USA","Tech","Non-Index",[2,3]))
glbs.append(glb("USA","Industry","Index",[15,20]))glbs.append(glb("USA","Industry","Non-Index",[8,4]))
glbs.append(glb("Asia","Tech","Index",[7,9]))glbs.append(glb("Asia","Tech","Non-Index",[1,5]))
glbs.append(glb("Asia","Industry","Index",[16,20]))glbs.append(glb("Asia","Industry","Non-Index",[0,4]))
print(index_vals(glbs))
print(years_vals(glbs))
