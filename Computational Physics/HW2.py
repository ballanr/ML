import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def Projectile_Motion(x,y,v_x,v_y,m,b2_scale):

    x_pos = []
    y_pos = []

    while y > 0:

        x_pos.append(x)
        y_pos.append(y)

        del_t = 0.1

        v = np.sqrt(v_x**2 + v_y**2)

        x = x + (v_x * del_t)

        y = y + (v_y * del_t)

        B_2 = 0.5 * 0.5 * 1.225 * 0.1 * b2_scale

        drag_x = -(B_2) * v * v_x

        drag_y = -(B_2)* v * v_y

        v_x = v_x + (drag_x / m) * del_t

        v_y = v_y + (-9.81 + drag_y / m) * del_t



        fall_time = np.asarray(y_pos)

        time_array = fall_time[fall_time > 0]
        time = len(time_array)*del_t

    return(x_pos,y_pos,time_array,time)

'''Varying v_x'''

def v_x():

    x,y,t_array,t = Projectile_Motion(0,10**3.5,10,0,100,1)
    x1,y1,t_array1,t1 = Projectile_Motion(0,10**3.5,100,0,100,1)
    x2,y2,t_array2,t2 = Projectile_Motion(0,10**3.5,1000,0,100,1)
    x3,y3,t_array3,t3 = Projectile_Motion(0,10**3.5,10000,0,100,1)
    x_drop,y_drop,t_drop_array,t_drop = Projectile_Motion(0,10**3.5,0,0,100,1)

    #Plots
    plt.figure(figsize=(13,10))

    plt.plot(np.arange(0,len(y),1)*.1,y,linewidth=3,label=r'v_x = 10 m/s')
    plt.plot(np.arange(0,len(y1),1)*.1,y1,linewidth=3,ls = 'dashed',label=r'v_x = 100 m/s')
    plt.plot(np.arange(0,len(y2),1)*.1,y2,linewidth=3,ls='dashdot',label=r'v_x = 1000 m/s')
    plt.plot(np.arange(0,len(y3),1)*.1,y3,linewidth=3,ls='solid',label=r'v_x = 10,000 m/s')
    plt.plot(np.arange(0,len(y_drop),1)*.1,y_drop,linewidth=3,ls='dotted',label=r'v_x = 0 m/s')


    plt.xlabel(r'$\Delta t$ (s)',fontsize=30)
    plt.ylabel(r'$\Delta y$ (m)',fontsize=30)
    plt.yticks(fontsize=20)
    plt.ylim(0,3200)
    plt.legend(fontsize = 22)
    plt.grid(True,alpha=0.4)
    plt.savefig('/Users/ballanr/Desktop/test2.pdf',bbox_inches='tight',dpi=300)
    plt.savefig('/Users/ballanr/Desktop/vx.eps',bbox_inches='tight',dpi=300)

'''Varying height'''
def height():

    x,y,t_array,t = Projectile_Motion(0,0.5*10**3.5,10,0,100,1)
    x1,y1,t_array1,t1 = Projectile_Motion(0,10**3.5,10,0,100,1)
    x2,y2,t_array2,t2 = Projectile_Motion(0,2*10**3.5,10,0,100,1)
    x3,y3,t_array3,t3 = Projectile_Motion(0,5*10**3.5,10,0,100,1)
    x_drop,y_drop,t_drop_array,t_drop = Projectile_Motion(0,10**3.5,0,0,100,1)

    #Plots

    plt.figure(figsize=(13,10))

    plt.plot(np.arange(0,len(y),1)*0.1,y,linewidth=3,label=r'y$_0 = 0.5\times 10^{3.5}$ m')
    plt.plot(np.arange(0,len(y1),1)*0.1,y1,linewidth=3,ls = 'dashed',label=r'y$_0 = 10^{3.5}$ m')
    plt.plot(np.arange(0,len(y2),1)*0.1,y2,linewidth=3,ls='dashdot',label=r'y$_0 = 2\times 10^{3.5}$ m')
    plt.plot(np.arange(0,len(y3),1)*0.1,y3,linewidth=3,ls='solid',label=r'y$_0 = 5\times 10^{3.5}$ m')
    plt.plot(np.arange(0,len(y_drop),1)*0.1,y_drop,linewidth=3,ls='dotted',label=r'y$_0 = 10^{3.5}$ m')

    plt.xlabel(r'$\Delta t$ (s)',fontsize=30)
    plt.ylabel(r'$\Delta y$ (m)',fontsize=30)
    plt.yticks(fontsize=20)
    plt.ylim(0,1.62*10**4)
    plt.legend(fontsize = 22)
    plt.grid(True,alpha=0.4)
    plt.savefig('/Users/ballanr/Desktop/test2.pdf',bbox_inches='tight',dpi=300)
    plt.savefig('/Users/ballanr/Desktop/height.eps',bbox_inches='tight',dpi=300)

'''Varying mass'''
def mass():

    x,y,t_array,t = Projectile_Motion(0,10**3.5,10,0,10,1)
    x1,y1,t_array1,t1 = Projectile_Motion(0,10**3.5,10,0,100,1)
    x2,y2,t_array2,t2 = Projectile_Motion(0,10**3.5,10,0,1000,1)
    x3,y3,t_array3,t3 = Projectile_Motion(0,10**3.5,10,0,10000,1)
    x_drop,y_drop,t_drop_array,t_drop = Projectile_Motion(0,10**3.5,0,0,100,1)

    #Plots

    plt.figure(figsize=(13,10))

    plt.plot(np.arange(0,len(y),1)*0.1,y,linewidth=3,label=r'm = 10 kg')
    plt.plot(np.arange(0,len(y1),1)*0.1,y1,linewidth=3,ls = 'dashed',label=r'm = 100 kg')
    plt.plot(np.arange(0,len(y2),1)*0.1,y2,linewidth=3,ls='dashdot',label=r'm = 1000 kg')
    plt.plot(np.arange(0,len(y3),1)*0.1,y3,linewidth=3,ls='solid',label=r'm = 10,000 kg')
    plt.plot(np.arange(0,len(y_drop),1)*0.1,y_drop,linewidth=3,ls='dotted',label=r'm = 100 kg')

    plt.xlabel(r'$\Delta t$ (s)',fontsize=30)
    plt.ylabel(r'$\Delta y$ (m)',fontsize=30)
    plt.yticks(fontsize=20)
    plt.ylim(0,3200)
    plt.legend(fontsize = 22)
    plt.grid(True,alpha=0.4)
    plt.savefig('/Users/ballanr/Desktop/test2.pdf',bbox_inches='tight',dpi=300)
    plt.savefig('/Users/ballanr/Desktop/mass.eps',bbox_inches='tight',dpi=300)

'''Varying drag'''

def drag():

    x,y,t_array,t = Projectile_Motion(0,10**3.5,10,0,100,1)
    x1,y1,t_array1,t1 = Projectile_Motion(0,10**3.5,10,0,100,2)
    x2,y2,t_array2,t2 = Projectile_Motion(0,10**3.5,10,0,100,5)
    x3,y3,t_array3,t3 = Projectile_Motion(0,10**3.5,10,0,100,10)
    x_drop,y_drop,t_drop_array,t_drop = Projectile_Motion(0,10**3.5,0,0,100,1)

    #Plots

    plt.figure(figsize=(13,10))

    plt.plot(np.arange(0,len(y),1)*0.1,y,linewidth=3,label=r'F$_{drag}$')
    plt.plot(np.arange(0,len(y1),1)*0.1,y1,linewidth=3,ls = 'dashed',label=r'2F$_{drag}$')
    plt.plot(np.arange(0,len(y2),1)*0.1,y2,linewidth=3,ls='dashdot',label=r'5F$_{drag}$')
    plt.plot(np.arange(0,len(y3),1)*0.1,y3,linewidth=3,ls='solid',label=r'10F$_{drag}$')
    plt.plot(np.arange(0,len(y_drop),1)*0.1,y_drop,linewidth=3,ls='dotted',label=r'F$_{drag}$')

    plt.xlabel(r'$\Delta t$ (s)',fontsize=30)
    plt.ylabel(r'$\Delta y$ (m)',fontsize=30)
    plt.ylim(0,3200)
    plt.yticks(fontsize=20)
    plt.legend(fontsize = 22)
    plt.grid(True,alpha=0.4)
    plt.savefig('/Users/ballanr/Desktop/test2.pdf',bbox_inches='tight',dpi=300)
    plt.savefig('/Users/ballanr/Desktop/drag.eps',bbox_inches='tight',dpi=300)

v_x()
#height()
#mass()
#drag()
