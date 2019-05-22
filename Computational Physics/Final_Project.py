import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter


def cellular_automata(zmin,zmax,gridsize,grains):

    # Initialize array
    main_array = array_init(zmin,zmax,gridsize)
    avalanche_number = np.zeros((gridsize,gridsize))
    avalanche_size = np.zeros((gridsize,gridsize))

    avsize = []
    avdur = []
    dursize = []

    plotter(main_array,'Initial',gridsize)

    # Drop a grain
    for i in range(grains):

        print('Adding grain ' + str(i))

        # Generating a random position on array for grain
        x,y = random_grain(gridsize)
        main_array[x,y] += 1

        # Checking for avalanches
        avalanche_flag = False

        # Initial avalanche
        if main_array[x,y] >= zmax:
            avalanche_array = np.zeros((gridsize,gridsize))
            main_array,avalanche_array = avalanches(x,y,main_array,avalanche_array,gridsize)
            avalanche_flag = True
            duration = 1

        # Continued avalanches
        while avalanche_flag == True:
            x,y = np.where(main_array >= zmax)
            cascade = True
            
            if len(x) == 0:
                avalanche_flag = False
                cascade = False

            for k in range(len(x)):
                main_array,avalanche_array = avalanches(x[k],y[k],main_array,avalanche_array,gridsize)
                duration += 1

            # if cascade == True:
            #     plotter(avalanche_array,'Grain ' + str(i),gridsize)

            avsum = sum(avalanche_array.sum(axis=0))

            avalanche_number += avalanche_array
            avalanche_size += avsum * avalanche_array
            avsize.append(avsum)
            avdur.append(duration)

            dursize.append((duration,avsum))

    # Mean avalanche size
    avsize = np.asarray(avsize)
    mean = avsize.sum() / len(avsize)
    avdur = np.asarray(avdur)
    print('\n')
    print('Max size: ' + str(max(avsize)))
    print('Number of avalanches: ' + str(len(avsize)))
    print('Average size: ' + str(mean))
    print('Max duration: ' + str(max(avdur)))
    print('Average duration: ' + str(avdur.sum()/len(avdur)))

    # Mean avalanche size per cell
    for a in range(gridsize):
        for b in range(gridsize):
            if avalanche_number[a,b] > 0:
                avalanche_size[a,b] = avalanche_size[a,b] / avalanche_number[a,b]

    # Number of avalanches vs. size
    unique_sizes,counts = np.unique(avsize,return_counts=True)
    z = np.polyfit(unique_sizes,counts,1)

    plt.figure(figsize=(13,10))
    plt.scatter(unique_sizes,counts,label='_nolegend_')
    plt.plot(unique_sizes,unique_sizes*z[0] + z[1],color='red',label=r'$\tau = $' + str(np.round(z[0],2)))
    plt.xlabel('Size')
    plt.ylabel('Number of avalanches')
    plt.xscale('linear')
    plt.yscale('linear')
    plt.legend(fontsize = 20, loc = 'upper right')
    plt.savefig('test.pdf',bbox_inches='tight',dpi=300)
    plt.clf()
    plt.close()

    # Duration vs. size
    dursize = np.asarray(dursize)
    dursize = sorted(dursize, key=itemgetter(1))
    
    x = []
    y = []
    xavg = []
    for element in dursize:
        x.append(element[1])
        y.append(element[0])

    x_uniques,counts = np.unique(x,return_counts=True)
    for k in range(len(x_uniques)):
        avg = 0
        count = counts[k]
        for i in range(len(x)):
            if x[i] == x_uniques[k]:
                avg += y[i]
        xavg.append(avg/count)

    z = np.polyfit(x_uniques,xavg,1)

    plt.figure(figsize=(13,10))
    plt.scatter(x_uniques,xavg,label='_nolegend_')
    plt.plot(x_uniques,x_uniques*z[0] + z[1],color='red',label=r'$\tau = $' + str(np.round(z[0],2)))
    plt.xlabel('Size')
    plt.ylabel('Duration of avalanches')
    plt.legend(fontsize=20,loc='upper left')
    plt.savefig('test1.pdf',bbox_inches='tight',dpi=300)
    plt.clf()
    plt.close()

    # Plots
    plotter(avalanche_number,'Number',gridsize)
    plotter(avalanche_size,'Size',gridsize)
    plotter(main_array,'relax',gridsize)

    print('All done.')

def array_init(zmin,zmax,gridsize):

    #array = np.random.randint(zmin,zmax//2,(gridsize,gridsize))
    array = np.random.randint(zmax-3,zmax-1,(gridsize,gridsize))

    return(array)

def plotter(array,name,gridsize):

    plt.figure(figsize=(13,10))
    plt.imshow(array,cmap='jet')
    plt.xticks(np.arange(0,gridsize,5),fontsize=18)
    plt.yticks(np.arange(0,gridsize,5),fontsize=18)
    if name == 'Initial' or name == 'relax':
        plt.colorbar()
    elif name == 'Number' or name == 'Size':
        plt.colorbar()
    plt.savefig('Final_Project_Plots/Avalanches/' + name + '.pdf',bbox_inches='tight',dpi=300)
    plt.clf()
    plt.close()
    
def random_grain(gridsize):

    x = np.random.randint(0,gridsize)
    y = np.random.randint(0,gridsize)

    return(x,y)

def avalanches(x,y,main_array,avalanche_array,gridsize):

    main_array[x,y] -= 4
    avalanche_array[x,y] = 1

    if x > 0 and x <= gridsize - 1:
        main_array[x-1,y] += 1
        avalanche_array[x-1,y] = 1
    if x >= 0 and x < gridsize - 1:
        main_array[x+1,y] += 1
        avalanche_array[x+1,y] = 1
    if y > 0 and y <= gridsize - 1:
        main_array[x,y-1] += 1
        avalanche_array[x,y-1] = 1
    if y >= 0 and y < gridsize - 1:
        main_array[x,y+1] += 1
        avalanche_array[x,y+1] = 1

    return(main_array,avalanche_array)


cellular_automata(0,5,100,4000)

'''IDEAS'''
# 1 - Determine mean avalanche size over time series for each grid point
# 2 - Investigate initial conditions
# 3 - Investigate grain placement