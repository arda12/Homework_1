# Class that reads burl1 data
# This Class takes the function name 
#Samira Ardani, 2013
import numpy as np
import math 
from datetime import datetime
#import matplotlib.pyplot as plt

class HW1_class():
    def __init__(self,filename):
        f = open(filename)
    #results =[]
     #   wind = []
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
        print  dates
        pressure = np.array(pressure)          
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
#print direc        

#    np.isnan(d)
        prs =[]
        for p in pressure:
  
            if p == 9999.:
                p = np.nan
            print p
            prs.append(p) 
        prs = np.array(prs) 
        print prs
# convert meteorologycal convension to northward eastward:
# direc_m: meteorological direction
# direc_o: oceanographycal direction

        direc_o =[]
        for direc_m in direc:
    
            if direc_m>180:
                direc_o.append( direc_m -180)
            else:
                direc_o.append(direc_m +180)
        print direc_o

        direc_o = np.array(direc_o)
    
        sp   =[]
    #sp_v =[]
    #sp_h =[]   
     
        for sp_line in speed:
            sp.append(sp_line)
    
        sp = np.array(sp)
        sp_h= -sp*(np.sin((direc_o*math.pi)/180))
        sp_v= -sp*(np.cos((direc_o*math.pi)/180)) 

        print sp_v
        print sp_h
        
       # self = 'burl1_2012.dat'
        
        self.sp_v = sp_v
        self.sp_h = sp_h
        self.prs = prs
        self.direc_o = direc_o
        self.dates = dates 
       
# Then we type this in the interactive window:      
# foo = HW1_class('burl1_2012.dat')
# foo. ...       
        
