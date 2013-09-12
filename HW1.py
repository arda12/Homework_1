# script to read burl1 data
#Samira Ardani, 2013

import numpy as np
import math 
from datetime import datetime
import matplotlib.pyplot as plt

f = open('burl1_2012.dat')

#wind = []
wind_dir = []
wind_speed = []
pressure = []
dates = []

for line in f.readlines()[2:]:
    print line
    
    
    data = line.split()
    wind_dir.append( float(data[5]) )
    wind_speed.append ( float(data[6]))
    pressure.append ( float(data[12]))
    
    year   = int(data[0])
    month  = int(data[1])
    day    = int(data[2])
    hour   = int(data[3])     
    minute = int(data[4])
    dates.append(datetime(year,month, day, hour, minute))
#print dates    
            
direction = np.array(wind_dir)
speed = np.array(wind_speed) 
#print direction

# Replace all 999 with NaN:
direc =[]
for d in direction:
  
    if d == 999.:
        d = np.nan
    print d
    direc.append(d)
    
prs =[]
for p in pressure:
  
    if p == 9999.:
        p = np.nan
    print p
    prs.append(p) 
prs = np.array(prs) 

print prs             
#print direc        

#    np.isnan(d)

# convert meteorologycal convension to northward eastward:
# direc_m: meteorological direction
# direc_o: oceanographycal direction

direc_o =[]
for direc_m in direc:
    
    if direc_m>180:
        direc_o.append( direc_m -180)
    else:
        direc_o.append(direc_m +180)
#print direc_o

direc_o = np.array(direc_o)
#print direc_o
        
sp   =[]
        
#sp_v =[]
#sp_h =[]   
     
for sp_line in speed:
    sp.append(sp_line)
    
sp = np.array(sp)
sp_h= -sp*(np.sin((direc_o*math.pi)/180))
sp_v= -sp*(np.cos((direc_o*math.pi)/180)) 

print 'dates:'
print  dates
print 'pressures:'
print prs
print 'Oceanographic direction:'
print direc_o
print 'Vertical velocity:'
print sp_v
print 'Horizontal velocity:'
print sp_h

    
plt.figure()
plt.plot(direc_o) 
plt.ylabel('direction, deg')
plt.show()
     
plt.figure()
plt.plot(sp_v) 
plt.ylabel('Vertical wind speed, m/s')
plt.show()

plt.figure()
plt.plot(sp_h) 
plt.ylabel('Horizontal wind speed, m/s')
plt.show()

plt.figure()
plt.plot(prs) 
plt.ylabel('pressure')
plt.show()          
#sp_v = np.array(sp_v)
#sp_h = np.array(sp_h)

      


 


