# Function that reads burl1 data
# This function takes the file name and the column of wind direction, wind speed and pressure and returns the wind direction in oceanographic convention
#Samira Ardani, 2013

def HW1_function(fname,dir_col,speed_col,pressure_col):
# script to read burl1 data
#Samira Ardani, 2013

    import numpy as np
    import math 
    from datetime import datetime
    import matplotlib.pyplot as plt
    f = open(fname)
    #results =[]
    #wind = []
    wind_dir = []
    wind_speed = []
    pressure = []
    dates = []
    for line in f.readlines()[2:]:
        print line
    
    
        data = line.split()
        wind_dir.append( float(data[dir_col]) )
        wind_speed.append ( float(data[speed_col]))
        pressure.append ( float(data[pressure_col]))
    
        year   = int(data[0])
        month  = int(data[1])
        day    = int(data[2])
        hour   = int(data[3])     
        minute = int(data[4])
        dates.append(datetime(year,month, day, hour, minute))
    
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
    
    
    # Plotting the results
        
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
    
    return dates, direc_o, sp_h, sp_v, pressure  
    
#dates = np.array(dates)
    
#wspeed=np.array(wspeed)   
    
#print 'mean pressure=', wspeed. mean()
#print 'min pressure=', wspeed. min()

 



    

    
   


 


