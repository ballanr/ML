import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def array_init(gridsize):

    # Creating an array with odd values (assuming even input)
    array = np.zeros((gridsize+1,gridsize+1))

    # Finding the center of the array
    middle = gridsize // 2

    # Setting nucleus
    array[middle,middle] = 1

    return(array)

def walker_init(gridsize,array):

    # Finding the middle (starting point) of the grid/cluster
    middle = gridsize // 2

    # Determining cluster size
    radius = (np.sum(array[middle,:]) // 2) + 5

    # Randomly picking the left or ride side to spawn a seed
    k = np.random.randint(0,2,1)

    if k == 1: # Right side spawn
        j = np.random.randint(middle+1,middle+1+radius,1)
    else: # Left side spawn
        j = np.random.randint(middle-radius,middle,1)

    return(j,radius)

def direction():

    # Array for containing direction of step
    step = np.zeros((1,2))

    # Randomly choosing a number 1-4 corresponding to the 4 possible step directions
    probability = np.random.randint(0,4,1)

    # Setting step array to direction selected
    if probability == 0:
        step[0,0] = 1
    elif probability == 1:
        step[0,1] = 1
    elif probability == 2:
        step[0,0] = -1
    elif probability == 3:
        step[0,1] = -1

    return(step)

def linear_walkabout(gridsize,array):

    # Boolean controls
    walk_flag = False
    init_flag = False
    update = False

    # Initializing a seed
    a = gridsize // 2
    b,radius = walker_init(gridsize,array)

    # Loop to make sure a seed is generated in an empty space
    while init_flag == False:
        
        if b > gridsize or b < 0:
            init_flag = True
            walk_flag = True
            update = False

        if init_flag == False:
            if array[a,b] == 1:
                b,radius = walker_init(gridsize,array)
            else:
                init_flag = True

    # Loop to walk the seed around until it hits the cluster or dies
    while walk_flag == False:

        step = direction()
        a_next = a + int(step[0,0])
        b_next = b + int(step[0,1])

        # Conditionals for deleting the seed

        if a_next > gridsize or a_next < 0:
            walk_flag = True
            update = False

        elif b_next > gridsize or b_next < 0:
            walk_flag = True
            update = False

        elif a_next > (gridsize // 2) + round(1.5*radius,0):
            walk_flag = True
            update = False

        elif b_next > (gridsize // 2) + round(1.5*radius,0):
            walk_flag = True
            update = False

        elif radius > gridsize // 2:
            walk_flag = True
            update = False

        # Condition for updating array
        if walk_flag == False:
            if array[a_next,b_next] != 1:
                a = a_next
                b = b_next

            # Exits the loop and updates array position 
            else:
                walk_flag = True
                update = True

    if update == True:
        array[a,b] = 1

    return(array)

def main(gridsize,init_type):

    array = array_init(gridsize)


    # x-axis seed initialization
    if init_type == 'Linear':
        walkers = int(np.round(0.1*(gridsize**2),0)) # Setting number of walkers to be 10% of gridsize
        print(walkers)
        for i in range(walkers):
            array = linear_walkabout(gridsize,array)
        masses,radii = Dimension(gridsize,array)

    # Radial seed initialization
    elif init_type == 'Radial':
        walkers = int(np.round(0.3*(gridsize**2),0)) # Setting number of walkers to be 30% of gridsize
        print(walkers)
        for i in range(walkers):
            array = radial_walkabout(gridsize,array)
        masses,radii = Dimension(gridsize,array)
    
    DLA_Plotter(array)
    Dimension_Plotter(radii,masses)

def Dimension_Plotter(radii,masses):

    # Taking the log of the radii and mass
    logradii = np.log10(radii)
    logmasses = np.log10(masses)

    # Finding best fit line (dimensionality)
    z = np.polyfit(logradii,logmasses,1)
    print(z)

    y = z[0]*np.asarray(logradii) + z[1]

    # Plotting data with best fit line
    plt.figure(figsize=(13,10))

    plt.plot(logradii,logmasses)
    plt.plot(logradii,y)
    plt.scatter(logradii,logmasses)

    plt.xlabel('Radius',fontsize=20)
    plt.ylabel('Mass',fontsize=20)
    plt.grid(True,alpha=0.35)
    plt.savefig('/Users/ballanr/Desktop/Dimensionality.pdf',bbox_inches='tight',dpi=300)

def DLA_Plotter(array):

    # Cluster plotter
    plt.figure(figsize=(13,10))
    plt.imshow(array,cmap='magma')
    plt.savefig('/Users/ballanr/Desktop/Cluster.pdf',bbox_inches='tight',dpi = 300)

def Dimension(gridsize,array):

    r_array = array_init(gridsize)

    fracs = np.arange(0.05,1.05,0.05)
    radii = []
    

    middle = gridsize // 2
    masses = []


    for i,row in enumerate(array):
        for j,value in enumerate(row):
                
            x = middle - i
            y = middle - j
            radius = np.sqrt(x**2 + y**2)
            #print(i,j,radius)
            r_array[i,j] = radius
    
    for element in fracs:
        mass = 0
        element = int(np.round(middle * element,0))

        for i,row in enumerate(array):
            for j,value in enumerate(row):
                if r_array[i,j] < element:
                    if array[i,j] == 1:
                        mass += 1
        
        radii.append(element)
        masses.append(mass)

    return(masses,radii)

def radial_walker(gridsize,array):

    # Generating a random angle
    # angle = np.random.random()
    # double = np.random.randint(1,3)

    # if double == 2:
    #     angle = double * angle * np.pi
    
    # else:
    #     angle = angle * np.pi

    angle = np.random.randint(1,361) / (2*np.pi)

    # Getting sin and cos
    x = np.cos(angle)
    y = np.sin(angle)
    
    middle = gridsize // 2

    # Setting radius
    x_radius = (max(array.sum(axis=1)) // 2) + 5
    y_radius = (max(array.sum(axis=0)) // 2) + 5

    radius = np.sqrt(x_radius**2 + y_radius**2)
    radius = np.round(radius,0)

    # Setting x and y positions
    x = np.round(middle + x*radius,0)
    y = np.round(middle + y*radius,0)

    return(int(x),int(y),radius)

def radial_walkabout(gridsize,array):

    # Boolean controls
    walk_flag = False
    init_flag = False

    # Initializing a seed
    b,a,radius = radial_walker(gridsize,array)

    # Loop to make sure a seed is generated in an empty space
    while init_flag == False:
        
        if a > gridsize or a < 0:
            init_flag = True
            walk_flag = True
            update = False
        
        elif b > gridsize or b < 0:
            init_flag = True
            walk_flag = True
            update = False

        if init_flag == False:
            if array[a,b] == 1:
                b,a,radius = radial_walker(gridsize,array)
            else:
                init_flag = True
    
    # Loop to walk seed around until it hits the cluster or dies
    while walk_flag == False:

        step = direction()
        a_next = a + int(step[0,0])
        b_next = b + int(step[0,1])

        # Conditionals for deleting the seed
        if a_next > gridsize or a_next < 0:
            walk_flag = True
            update = False

        elif b_next > gridsize or b_next < 0:
            walk_flag = True
            update = False

        elif a_next > (gridsize // 2) + round(1.5*radius,0):
            walk_flag = True
            update = False

        elif b_next > (gridsize // 2) + round(1.5*radius,0):
            walk_flag = True
            update = False

        elif radius > gridsize // 2:
            walk_flag = True
            update = False

        # Condition for updating array
        if walk_flag == False:
            if array[a_next,b_next] != 1:
                a = a_next
                b = b_next

            # Exits loop and updates array position
            else:
                walk_flag = True
                update = True

    if update == True:
        array[a,b] = 1

    return(array)



main(100,'Radial')
