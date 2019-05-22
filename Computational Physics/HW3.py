import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def Euler(Jupiter_scale):

    AU =  149597870700 #m
    G = 1.9825455765 * (10**-29) # AU^3 * kg^{-1} * yr^{-2}
    del_t = 0.01

    # Initial Earth parameters
    init_Earth_x = 1 #AU
    init_Earth_y = 0 #AU
    mass_Earth = 5.97237 * (10**24) #kg
    init_Earth_vx = 0 # AU/year
    init_Earth_vy = -29.78*0.210805 #AU/year

    # Initial Jupiter parameters
    init_Jupiter_x = 0 #AU
    init_Jupiter_y = 5.2 #AU
    mass_Jupiter = Jupiter_scale*1.8982 * (10**27) #kg
    init_Jupiter_vx = (13.07*0.210805) #AU/year
    init_Jupiter_vy = 0 #AU/year

    # Initial Sun parameters
    init_Sun_x = 0 #AU
    init_Sun_y = 0 #AU
    mass_Sun = 1.98855 * (10**30) #kg
    init_Sun_vx =  -(mass_Jupiter*init_Jupiter_vx)/mass_Sun #AU/year
    init_Sun_vy = -(mass_Earth*init_Earth_vy)/mass_Sun #AU/year

    # Test
    if Jupiter_scale > 1:
        semi = (G*(mass_Sun + mass_Jupiter))*(11.86/(2*np.pi))**2
        semi = semi**(1/3)
        vel = (2*np.pi*semi) / 11.86

        init_Jupiter_vx = vel
        init_Jupiter_y = semi

        init_Sun_vx =  -(mass_Jupiter*init_Jupiter_vx)/mass_Sun #AU/year
        init_Sun_vy = -(mass_Earth*init_Earth_vy)/mass_Sun #AU/year

    # Distances
    R_Sun_Earth = np.sqrt((init_Earth_x - init_Sun_x)**2 + (init_Earth_y - init_Sun_y)**2)
    R_Sun_Jupiter = np.sqrt((init_Jupiter_x - init_Sun_x)**2 + (init_Jupiter_y - init_Sun_y)**2)
    R_Earth_Jupiter = np.sqrt((init_Jupiter_x - init_Earth_x)**2 + (init_Jupiter_y - init_Earth_y)**2)

    # New velocities
    vx_Earth = init_Earth_vx - del_t * (G * mass_Sun * init_Earth_x) / (R_Sun_Earth**3) - del_t * (G * mass_Jupiter * (init_Earth_x - init_Jupiter_x)) / (R_Earth_Jupiter**3)
    vy_Earth = init_Earth_vy - del_t * (G * mass_Sun * init_Earth_y) / (R_Sun_Earth**3) - del_t * (G * mass_Jupiter * (init_Earth_y - init_Jupiter_y)) / (R_Earth_Jupiter**3)

    vx_Jupiter = init_Jupiter_vx - del_t * (G * mass_Sun * init_Jupiter_x) / (R_Sun_Jupiter**3) - del_t * (G * mass_Earth * (init_Jupiter_x - init_Earth_x)) / (R_Earth_Jupiter**3)
    vy_Jupiter = init_Jupiter_vy - del_t * (G * mass_Sun * init_Jupiter_y) / (R_Sun_Jupiter**3) - del_t * (G * mass_Earth * (init_Jupiter_y - init_Earth_y)) / (R_Earth_Jupiter**3)

    vx_Sun = init_Sun_vx - del_t * (G * mass_Earth * (init_Sun_x - init_Earth_x)) / (R_Sun_Earth**3) - del_t * (G * mass_Jupiter * (init_Sun_x - init_Jupiter_x)) / (R_Sun_Jupiter**3)
    vy_Sun = init_Sun_vy - del_t * (G * mass_Earth * (init_Sun_y - init_Earth_y)) / (R_Sun_Earth**3) - del_t * (G * mass_Jupiter * (init_Sun_y - init_Jupiter_y)) / (R_Sun_Jupiter**3)

    # New positions
    x_Earth = init_Earth_x + vx_Earth * del_t
    y_Earth = init_Earth_y + vy_Earth * del_t

    x_Jupiter = init_Jupiter_x + vx_Jupiter * del_t
    y_Jupiter = init_Jupiter_y + vy_Jupiter * del_t

    x_Sun = init_Sun_x + vx_Sun * del_t
    y_Sun = init_Sun_y + vy_Sun * del_t

    Earth_values = [init_Earth_x, init_Earth_y, init_Earth_vx, init_Earth_vy, x_Earth, y_Earth, vx_Earth, vy_Earth]
    Jupiter_values = [init_Jupiter_x, init_Jupiter_y, init_Jupiter_vx, init_Jupiter_vy, x_Jupiter, y_Jupiter, vx_Jupiter, vy_Jupiter]
    Sun_values = [init_Sun_x, init_Sun_y, init_Sun_vx, init_Sun_vy, x_Sun, y_Sun, vx_Sun, vy_Sun]

    # Return values
    return(Earth_values,Jupiter_values,Sun_values)

def Pos_Update(x1,y1,vx1,vy1,ax1,ay1,del_t):

    x2 = (x1 + vx1 * del_t) + (0.5 * ax1 * (del_t**2))
    y2 = (y1 + vy1 * del_t) + (0.5 * ay1 * (del_t**2))

    return(x2,y2)

def Accel_Update(Earth_x2,Earth_y2,Jupiter_x2,Jupiter_y2,Sun_x2,Sun_y2,Jupiter_scale):

    mass_Earth = 5.97237 * (10**24)
    mass_Jupiter = Jupiter_scale*1.8982 * (10**27)
    mass_Sun = 1.98855 * (10**30)
    G = 1.9825455765 * (10**-29) # AU^3 * kg^{-1} * yr^{-2}

    # Calculate Distances
    R_Sun_Earth = np.sqrt((Earth_x2 - Sun_x2)**2 + (Earth_y2 - Sun_y2)**2)
    R_Sun_Jupiter = np.sqrt((Jupiter_x2 - Sun_x2)**2 + (Jupiter_y2 - Sun_y2)**2)
    R_Earth_Jupiter = np.sqrt((Jupiter_x2 - Earth_x2)**2 + (Jupiter_y2 - Earth_y2)**2)

    # Acceleration update 
    Earth_ax2 = -(4*np.pi**2 * (Earth_x2 - Sun_x2)) / (R_Sun_Earth**3) - (4*np.pi**2 * (mass_Jupiter / mass_Sun) * (Earth_x2 - Jupiter_x2)) / (R_Earth_Jupiter**3)
    Earth_ay2 = -(4*np.pi**2 * (Earth_y2 - Sun_y2)) / (R_Sun_Earth**3) - (4*np.pi**2 * (mass_Jupiter / mass_Sun) * (Earth_y2 - Jupiter_y2)) / (R_Earth_Jupiter**3)

    Jupiter_ax2 = -(4*np.pi**2 * (Jupiter_x2 - Sun_x2)) / (R_Sun_Jupiter**3) - (4*np.pi**2 * (mass_Earth/mass_Sun) * (Jupiter_x2 - Earth_x2)) / (R_Earth_Jupiter**3)
    Jupiter_ay2 = -(4*np.pi**2 * (Jupiter_y2 - Sun_y2)) / (R_Sun_Jupiter**3) - (4*np.pi**2 * (mass_Earth/mass_Sun) * (Jupiter_y2 - Earth_y2)) / (R_Earth_Jupiter**3)

    Sun_ax2 = -(G * mass_Earth * (Sun_x2 - Earth_x2)) / (R_Sun_Earth**3) - (G * mass_Jupiter * (Sun_x2 - Jupiter_x2)) / (R_Sun_Jupiter**3)
    Sun_ay2 = -(G * mass_Earth * (Sun_y2 - Earth_y2)) / (R_Sun_Earth**3) - (G * mass_Jupiter * (Sun_y2 - Jupiter_y2)) / (R_Sun_Jupiter**3)

    return(Earth_ax2,Earth_ay2,Jupiter_ax2,Jupiter_ay2,Sun_ax2,Sun_ay2)

def Vel_Update(vx1,vy1,ax1,ay1,ax2,ay2,del_t):

    vx2 = vx1 + 0.5 * (ax1 + ax2) * del_t
    vy2 = vy1 + 0.5 * (ay1 + ay2) * del_t

    return(vx2,vy2)

def Velocity_Verlet(Earth,Jupiter,Sun,Jupiter_scale):

    # Initial conditions
    mass_Earth = 5.97237 * (10**24) #kg
    Earth_x0 = Earth[0]
    Earth_y0 = Earth[1]
    Earth_vx0 = Earth[2]
    Earth_vy0 = Earth[3]
    Earth_x1 = Earth[4]
    Earth_y1 = Earth[5]
    Earth_vx1 = Earth[6]
    Earth_vy1 = Earth[7]

    mass_Jupiter = Jupiter_scale*1.8982 * (10**27) #kg
    Jupiter_x0 = Jupiter[0]
    Jupiter_y0 = Jupiter[1]
    Jupiter_vx0 = Jupiter[2]
    Jupiter_vy0 = Jupiter[3]
    Jupiter_x1 = Jupiter[4]
    Jupiter_y1 = Jupiter[5]
    Jupiter_vx1 = Jupiter[6]
    Jupiter_vy1 = Jupiter[7]

    mass_Sun = 1.98855 * (10**30) #kg
    Sun_x0 = Sun[0]
    Sun_y0 = Sun[1]
    Sun_vx0 = Sun[2]
    Sun_vy0 = Sun[3]
    Sun_x1 = Sun[4]
    Sun_y1 = Sun[5]
    Sun_vx1 = Sun[6]
    Sun_vy1 = Sun[7]



    timescale = np.arange(0,10*11.86,0.01)
    G = 1.9825455765 * (10**-29) # AU^3 * kg^{-1} * yr^{-2}
    del_t = 0.01

    # Arrays
    Earth_xpos = [Earth_x0,Earth_x1]
    Earth_ypos = [Earth_y0,Earth_y1]
    Earth_velx = [Earth_vx0,Earth_vx1]
    Earth_vely = [Earth_vy0,Earth_vy1]

    Jupiter_xpos = [Jupiter_x0,Jupiter_x1]
    Jupiter_ypos = [Jupiter_y0,Jupiter_y1]
    Jupiter_velx = [Jupiter_vx0,Jupiter_vx1]
    Jupiter_vely = [Jupiter_vy0,Jupiter_vy1]

    Sun_xpos = [Sun_x0,Sun_x1]
    Sun_ypos = [Sun_y0,Sun_y1]
    Sun_velx = [Sun_vx0,Sun_vx1]
    Sun_vely = [Sun_vy0,Sun_vy1]

    # Initial acceleration

    R_Sun_Earth = np.sqrt((Earth_x1 - Sun_x1)**2 + (Earth_y1 - Sun_y1)**2)
    R_Sun_Jupiter = np.sqrt((Jupiter_x1 - Sun_x1)**2 + (Jupiter_y1 - Sun_y1)**2)
    R_Earth_Jupiter = np.sqrt((Jupiter_x1 - Earth_x1)**2 + (Jupiter_y1 - Earth_y1)**2)

    Earth_ax1 = -(4*np.pi**2 * (Earth_x1 - Sun_x1)) / (R_Sun_Earth**3) - (4*np.pi**2 * (mass_Jupiter / mass_Sun) * (Earth_x1 - Jupiter_x1)) / (R_Earth_Jupiter**3)
    Earth_ay1 = -(4*np.pi**2 * (Earth_y1 - Sun_y1)) / (R_Sun_Earth**3) - (4*np.pi**2 * (mass_Jupiter / mass_Sun) * (Earth_y1 - Jupiter_y1)) / (R_Earth_Jupiter**3)

    Jupiter_ax1 = -(4*np.pi**2 * (Jupiter_x1 - Sun_x1)) / (R_Sun_Jupiter**3) - (4*np.pi**2 * (mass_Earth/mass_Sun) * (Jupiter_x1 - Earth_x1)) / (R_Earth_Jupiter**3)
    Jupiter_ay1 = -(4*np.pi**2 * (Jupiter_y1 - Sun_y1)) / (R_Sun_Jupiter**3) - (4*np.pi**2 * (mass_Earth/mass_Sun) * (Jupiter_y1 - Earth_y1)) / (R_Earth_Jupiter**3)

    Sun_ax1 = -(G * mass_Earth * (Sun_x1 - Earth_x1)) / (R_Sun_Earth**3) - (G * mass_Jupiter * (Sun_x1 - Jupiter_x1)) / (R_Sun_Jupiter**3)
    Sun_ay1 = -(G * mass_Earth * (Sun_y1 - Earth_y1)) / (R_Sun_Earth**3) - (G * mass_Jupiter * (Sun_y1 - Jupiter_y1)) / (R_Sun_Jupiter**3)

    # Iterate
    for i in range(len(timescale)):

        # Position Update
        Earth_x2,Earth_y2 = Pos_Update(Earth_x1,Earth_y1,Earth_vx1,Earth_vy1,Earth_ax1,Earth_ay1,0.01)
        Jupiter_x2,Jupiter_y2 = Pos_Update(Jupiter_x1,Jupiter_y1,Jupiter_vx1,Jupiter_vy1,Jupiter_ax1,Jupiter_ay1,0.01)
        Sun_x2,Sun_y2 = Pos_Update(Sun_x1,Sun_y1,Sun_vx1,Sun_vy1,Sun_ax1,Sun_ay1,0.01)

        # Acceleration Update
        Earth_ax2,Earth_ay2,Jupiter_ax2,Jupiter_ay2,Sun_ax2,Sun_ay2 = Accel_Update(Earth_x2,Earth_y2,Jupiter_x2,Jupiter_y2,Sun_x2,Sun_y2,Jupiter_scale)
        
        # Velocity Update
        Earth_vx2,Earth_vy2 = Vel_Update(Earth_vx1,Earth_vy1,Earth_ax1,Earth_ay1,Earth_ax2,Earth_ay2,0.01)
        Jupiter_vx2,Jupiter_vy2 = Vel_Update(Jupiter_vx1,Jupiter_vy1,Jupiter_ax1,Jupiter_ay1,Jupiter_ax2,Jupiter_ay2,0.01)
        Sun_vx2,Sun_vy2 = Vel_Update(Sun_vx1,Sun_vy1,Sun_ax1,Sun_ay1,Sun_ax2,Sun_ay2,0.01)

        # Append to arrays
        Earth_xpos.append(Earth_x2)
        Earth_ypos.append(Earth_y2)
        Earth_velx.append(Earth_vx2)
        Earth_vely.append(Earth_vy2)

        Jupiter_xpos.append(Jupiter_x2)
        Jupiter_ypos.append(Jupiter_y2)
        Jupiter_velx.append(Jupiter_vx2)
        Jupiter_vely.append(Jupiter_vy2)

        Sun_xpos.append(Sun_x2)
        Sun_ypos.append(Sun_y2)
        Sun_velx.append(Sun_vx2)
        Sun_vely.append(Sun_vy2)

        # Variable update
        Earth_x0 = Earth_x1
        Earth_x1 = Earth_x2
        Earth_y0 = Earth_y1
        Earth_y1 = Earth_y2
        Earth_vx1 = Earth_vx2
        Earth_vy1 = Earth_vy2
        Earth_ax1 = Earth_ax2
        Earth_ay1 = Earth_ay2

        Jupiter_x0 = Jupiter_x1
        Jupiter_x1 = Jupiter_x2
        Jupiter_y0 = Jupiter_y1
        Jupiter_y1 = Jupiter_y2
        Jupiter_vx1 = Jupiter_vx2
        Jupiter_vy1 = Jupiter_vy2
        Jupiter_ax1 = Jupiter_ax2
        Jupiter_ay1 = Jupiter_ay2

        Sun_x0 = Sun_x1
        Sun_x1 = Sun_x2
        Sun_y0 = Sun_y1
        Sun_y1 = Sun_y2
        Sun_vx1 = Sun_vx2
        Sun_vy1 = Sun_vy2
        Sun_ax1 = Sun_ax2
        Sun_ay1 = Sun_ay2
    
    return(Earth_xpos,Earth_ypos,Earth_velx,Earth_vely,Jupiter_xpos,Jupiter_ypos,Jupiter_velx,Jupiter_vely,Sun_xpos,Sun_ypos,Sun_velx,Sun_vely)

def Pos_Plotter(Earth_xpos,Earth_ypos,Jupiter_xpos,Jupiter_ypos,Sun_xpos,Sun_ypos):
    plt.figure(figsize=(10,10))
    plt.scatter(Earth_xpos,Earth_ypos,s=1)
    plt.scatter(Jupiter_xpos,Jupiter_ypos,s=1)
    plt.scatter(Sun_xpos,Sun_ypos,s=1)

    plt.grid(True,alpha=0.5)
    plt.xlabel('x (AU)',fontsize=24)
    plt.ylabel('y (AU)',fontsize=24)

    #plt.xlim(-6,6)
    #plt.ylim(-6,6)

    plt.savefig('/Users/ballanr/Desktop/hw3test.pdf',bbox_inches='tight',dpi=300)

def Poincare_Iterator(Earth,Jupiter,Sun,Jupiter_scale,Per_Count):

    # Initial conditions
    mass_Earth = 5.97237 * (10**24) #kg
    Earth_x0 = Earth[0]
    Earth_y0 = Earth[1]
    Earth_vx0 = Earth[2]
    Earth_vy0 = Earth[3]
    Earth_x1 = Earth[4]
    Earth_y1 = Earth[5]
    Earth_vx1 = Earth[6]
    Earth_vy1 = Earth[7]

    mass_Jupiter = Jupiter_scale*1.8982 * (10**27) #kg
    Jupiter_x0 = Jupiter[0]
    Jupiter_y0 = Jupiter[1]
    Jupiter_vx0 = Jupiter[2]
    Jupiter_vy0 = Jupiter[3]
    Jupiter_x1 = Jupiter[4]
    Jupiter_y1 = Jupiter[5]
    Jupiter_vx1 = Jupiter[6]
    Jupiter_vy1 = Jupiter[7]

    mass_Sun = 1.98855 * (10**30) #kg
    Sun_x0 = Sun[0]
    Sun_y0 = Sun[1]
    Sun_vx0 = Sun[2]
    Sun_vy0 = Sun[3]
    Sun_x1 = Sun[4]
    Sun_y1 = Sun[5]
    Sun_vx1 = Sun[6]
    Sun_vy1 = Sun[7]

    G = 1.9825455765 * (10**-29) # AU^3 * kg^{-1} * yr^{-2}
    del_t = 0.01

    # Setting up period scale
    #orbit = Orbit_Period(Jupiter_scale)

    # orbit = 2*np.pi*np.sqrt((5.2**3) / (G*(mass_Sun + mass_Jupiter)))
    # orbit = '%.2f' % np.round(orbit,2)
    # orbit = float(orbit)
    orbit = 11.86
        
    timescale = np.arange(0,Per_Count*orbit,0.01)
    time_sample = 0.4*orbit
    time_sample = '%.2f' % np.round(time_sample,2)
    time_sample = float(time_sample)

    orbit_periods = np.ones(Per_Count)
    for i in range(Per_Count):
        time = time_sample + (i*orbit)
        time = '%.2f' % np.round(time,2)
        orbit_periods[i] = float(time)

    # Arrays
    Earth_xpos = []
    Earth_ypos = []
    Earth_velx = []
    Earth_vely = []

    Jupiter_xpos = []
    Jupiter_ypos = []
    Jupiter_velx = []
    Jupiter_vely = []

    Sun_xpos = []
    Sun_ypos = []
    Sun_velx = []
    Sun_vely = []

    # Initial acceleration

    R_Sun_Earth = np.sqrt((Earth_x1 - Sun_x1)**2 + (Earth_y1 - Sun_y1)**2)
    R_Sun_Jupiter = np.sqrt((Jupiter_x1 - Sun_x1)**2 + (Jupiter_y1 - Sun_y1)**2)
    R_Earth_Jupiter = np.sqrt((Jupiter_x1 - Earth_x1)**2 + (Jupiter_y1 - Earth_y1)**2)

    Earth_ax1 = -(4*np.pi**2 * (Earth_x1 - Sun_x1)) / (R_Sun_Earth**3) - (4*np.pi**2 * (mass_Jupiter / mass_Sun) * (Earth_x1 - Jupiter_x1)) / (R_Earth_Jupiter**3)
    Earth_ay1 = -(4*np.pi**2 * (Earth_y1 - Sun_y1)) / (R_Sun_Earth**3) - (4*np.pi**2 * (mass_Jupiter / mass_Sun) * (Earth_y1 - Jupiter_y1)) / (R_Earth_Jupiter**3)

    Jupiter_ax1 = -(4*np.pi**2 * (Jupiter_x1 - Sun_x1)) / (R_Sun_Jupiter**3) - (4*np.pi**2 * (mass_Earth/mass_Sun) * (Jupiter_x1 - Earth_x1)) / (R_Earth_Jupiter**3)
    Jupiter_ay1 = -(4*np.pi**2 * (Jupiter_y1 - Sun_y1)) / (R_Sun_Jupiter**3) - (4*np.pi**2 * (mass_Earth/mass_Sun) * (Jupiter_y1 - Earth_y1)) / (R_Earth_Jupiter**3)

    Sun_ax1 = -(G * mass_Earth * (Sun_x1 - Earth_x1)) / (R_Sun_Earth**3) - (G * mass_Jupiter * (Sun_x1 - Jupiter_x1)) / (R_Sun_Jupiter**3)
    Sun_ay1 = -(G * mass_Earth * (Sun_y1 - Earth_y1)) / (R_Sun_Earth**3) - (G * mass_Jupiter * (Sun_y1 - Jupiter_y1)) / (R_Sun_Jupiter**3)

    # Iterate
    for i in range(len(timescale)):

        # Position Update
        Earth_x2,Earth_y2 = Pos_Update(Earth_x1,Earth_y1,Earth_vx1,Earth_vy1,Earth_ax1,Earth_ay1,0.01)
        Jupiter_x2,Jupiter_y2 = Pos_Update(Jupiter_x1,Jupiter_y1,Jupiter_vx1,Jupiter_vy1,Jupiter_ax1,Jupiter_ay1,0.01)
        Sun_x2,Sun_y2 = Pos_Update(Sun_x1,Sun_y1,Sun_vx1,Sun_vy1,Sun_ax1,Sun_ay1,0.01)

        # Acceleration Update
        Earth_ax2,Earth_ay2,Jupiter_ax2,Jupiter_ay2,Sun_ax2,Sun_ay2 = Accel_Update(Earth_x2,Earth_y2,Jupiter_x2,Jupiter_y2,Sun_x2,Sun_y2,Jupiter_scale)
        
        # Velocity Update
        Earth_vx2,Earth_vy2 = Vel_Update(Earth_vx1,Earth_vy1,Earth_ax1,Earth_ay1,Earth_ax2,Earth_ay2,0.01)
        Jupiter_vx2,Jupiter_vy2 = Vel_Update(Jupiter_vx1,Jupiter_vy1,Jupiter_ax1,Jupiter_ay1,Jupiter_ax2,Jupiter_ay2,0.01)
        Sun_vx2,Sun_vy2 = Vel_Update(Sun_vx1,Sun_vy1,Sun_ax1,Sun_ay1,Sun_ax2,Sun_ay2,0.01)

        # Append to arrays
        k = i * del_t
        k = '%.2f' % np.round(k,2)
        k = float(k)
        if k in orbit_periods:
            Earth_xpos.append(Earth_x2)
            Earth_ypos.append(Earth_y2)
            Earth_velx.append(Earth_vx2)
            Earth_vely.append(Earth_vy2)

            Jupiter_xpos.append(Jupiter_x2)
            Jupiter_ypos.append(Jupiter_y2)
            Jupiter_velx.append(Jupiter_vx2)
            Jupiter_vely.append(Jupiter_vy2)

            Sun_xpos.append(Sun_x2)
            Sun_ypos.append(Sun_y2)
            Sun_velx.append(Sun_vx2)
            Sun_vely.append(Sun_vy2)

        # Variable update
        Earth_x0 = Earth_x1
        Earth_x1 = Earth_x2
        Earth_y0 = Earth_y1
        Earth_y1 = Earth_y2
        Earth_vx1 = Earth_vx2
        Earth_vy1 = Earth_vy2
        Earth_ax1 = Earth_ax2
        Earth_ay1 = Earth_ay2

        Jupiter_x0 = Jupiter_x1
        Jupiter_x1 = Jupiter_x2
        Jupiter_y0 = Jupiter_y1
        Jupiter_y1 = Jupiter_y2
        Jupiter_vx1 = Jupiter_vx2
        Jupiter_vy1 = Jupiter_vy2
        Jupiter_ax1 = Jupiter_ax2
        Jupiter_ay1 = Jupiter_ay2

        Sun_x0 = Sun_x1
        Sun_x1 = Sun_x2
        Sun_y0 = Sun_y1
        Sun_y1 = Sun_y2
        Sun_vx1 = Sun_vx2
        Sun_vy1 = Sun_vy2
        Sun_ax1 = Sun_ax2
        Sun_ay1 = Sun_ay2
    
    return(Earth_xpos,Earth_ypos,Earth_velx,Earth_vely,Jupiter_xpos,Jupiter_ypos,Jupiter_velx,Jupiter_vely,Sun_xpos,Sun_ypos,Sun_velx,Sun_vely)

def Poincare(xpos,velx,ypos,vely):

    xpos = np.asarray(xpos)
    ypos = np.asarray(ypos)

    r = np.sqrt(xpos**2 + ypos**2)

    velx = np.asarray(velx)
    vely = np.asarray(vely)

    vel = np.sqrt(velx**2 + vely**2)

    plt.figure(figsize=(13,10))

    plt.plot(r,vel,linewidth = 1)
    plt.scatter(r,vel,s=10,color='black')

    plt.grid(True,alpha=0.5)
    plt.xlabel('r (AU)',fontsize=24)
    plt.ylabel('v (AU/year)',fontsize=24)
    #plt.legend(fontsize=20)

    plt.savefig('/Users/ballanr/Desktop/hw3test.pdf',bbox_inches='tight',dpi=300)

def Orbit_Period(Jupiter_scale):

    orbit = (2*np.pi*5.2)/(13.07*0.210805)/Jupiter_scale
    orbit = '%.2f' % np.round(orbit,2)
    orbit = float(orbit)
    
    return(orbit)
    
Earth,Jupiter,Sun = Euler(10)
#print(Earth)
#Verlet(Earth,Jupiter,Sun)
#E_xpos,E_ypos,E_velx,E_vely,J_xpos,J_ypos,J_velx,J_vely,S_xpos,S_ypos,S_velx,S_vely = Velocity_Verlet(Earth,Jupiter,Sun,100)
E_xpos,E_ypos,E_velx,E_vely,J_xpos,J_ypos,J_velx,J_vely,S_xpos,S_ypos,S_velx,S_vely = Poincare_Iterator(Earth,Jupiter,Sun,10,500)
#Pos_Plotter(E_xpos,E_ypos,J_xpos,J_ypos,S_xpos,S_ypos)
#Poincare(E_xpos,E_velx,E_ypos,E_vely)
Poincare(J_xpos,J_velx,J_ypos,J_vely)
#Poincare(S_xpos,S_velx,S_ypos,S_vely)
