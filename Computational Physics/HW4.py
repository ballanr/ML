import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Relaxation_15(array):
    
    # Variable to keep track of change
    del_V = []

    # Loop through grid
    for i in range(13):
        i += 1

        for j in range(13):
            j += 1

            if j < 5 or j > 9:
                old = array[i,j]
                array[i,j] = (array[i-1,j] + array[i+1,j] + array[i,j-1] + array[i,j+1]) / 4
                new = array[i,j]
                change = np.abs(new - old)
                del_V.append(change)

            if i < 5 or i > 9:
                old = array[i,j]
                array[i,j] = (array[i-1,j] + array[i+1,j] + array[i,j-1] + array[i,j+1]) / 4
                new = array[i,j]
                change = np.abs(new - old)
                del_V.append(change)
        
            else:
                change = 0
                del_V.append(change)

    del_V = np.asarray(del_V)
    max_del_V = max(del_V)
    del_V_sum = np.sum(del_V) / (13**2)

    array[5:10,5:10] = 1

    return(array,del_V_sum,max_del_V)

def Relaxation_25(array):
    
    # Variable to keep track of change
    del_V = []

    # Loop through grid
    for i in range(23):
        i += 1

        for j in range(23):
            j += 1

            if j < 10 or j > 14:
                old = array[i,j]
                array[i,j] = (array[i-1,j] + array[i+1,j] + array[i,j-1] + array[i,j+1]) / 4
                new = array[i,j]
                change = np.abs(new - old)
                del_V.append(change)

            if i < 10 or i > 14:
                old = array[i,j]
                array[i,j] = (array[i-1,j] + array[i+1,j] + array[i,j-1] + array[i,j+1]) / 4
                new = array[i,j]
                change = np.abs(new - old)
                del_V.append(change)
        
            else:
                change = 0
                del_V.append(change)

    del_V = np.asarray(del_V)
    max_del_V = max(del_V)
    del_V_sum = np.sum(del_V) / (23**2)

    array[10:15,10:15] = 1

    return(array,del_V_sum,max_del_V)

def Relaxation_35(array):
    
    # Variable to keep track of change
    del_V = []

    # Loop through grid
    for i in range(33):
        i += 1

        for j in range(33):
            j += 1

            if j < 15 or j > 19:
                old = array[i,j]
                array[i,j] = (array[i-1,j] + array[i+1,j] + array[i,j-1] + array[i,j+1]) / 4
                new = array[i,j]
                change = np.abs(new - old)
                del_V.append(change)

            if i < 15 or i > 19:
                old = array[i,j]
                array[i,j] = (array[i-1,j] + array[i+1,j] + array[i,j-1] + array[i,j+1]) / 4
                new = array[i,j]
                change = np.abs(new - old)
                del_V.append(change)
        
            else:
                change = 0
                del_V.append(change)

    del_V = np.asarray(del_V)
    max_del_V = max(del_V)
    del_V_sum = np.sum(del_V) / (33**2)

    array[15:20,15:20] = 1

    return(array,del_V_sum,max_del_V)

def Relaxation_45(array):
    
    # Variable to keep track of change
    del_V = []

    # Loop through grid
    for i in range(43):
        i += 1

        for j in range(43):
            j += 1

            if j < 20 or j > 24:
                old = array[i,j]
                array[i,j] = (array[i-1,j] + array[i+1,j] + array[i,j-1] + array[i,j+1]) / 4
                new = array[i,j]
                change = np.abs(new - old)
                del_V.append(change)

            if i < 20 or i > 24:
                old = array[i,j]
                array[i,j] = (array[i-1,j] + array[i+1,j] + array[i,j-1] + array[i,j+1]) / 4
                new = array[i,j]
                change = np.abs(new - old)
                del_V.append(change)
        
            else:
                change = 0
                del_V.append(change)

    del_V = np.asarray(del_V)
    max_del_V = max(del_V)
    del_V_sum = np.sum(del_V) / (43**2)

    array[20:25,20:25] = 1

    return(array,del_V_sum,max_del_V)

def Relaxation_75(array):
    
    # Variable to keep track of change
    del_V = []

    # Loop through grid
    for i in range(73):
        i += 1

        for j in range(73):
            j += 1

            if j < 35 or j > 39:
                old = array[i,j]
                array[i,j] = (array[i-1,j] + array[i+1,j] + array[i,j-1] + array[i,j+1]) / 4
                new = array[i,j]
                change = np.abs(new - old)
                del_V.append(change)

            if i < 35 or i > 39:
                old = array[i,j]
                array[i,j] = (array[i-1,j] + array[i+1,j] + array[i,j-1] + array[i,j+1]) / 4
                new = array[i,j]
                change = np.abs(new - old)
                del_V.append(change)
        
            else:
                change = 0
                del_V.append(change)

    del_V = np.asarray(del_V)
    max_del_V = max(del_V)
    del_V_sum = np.sum(del_V) / (73**2)

    array[35:40,35:40] = 1

    return(array,del_V_sum,max_del_V)

def Relaxation_125(array):
    
    # Variable to keep track of change
    del_V = []

    # Loop through grid
    for i in range(123):
        i += 1

        for j in range(123):
            j += 1

            if j < 60 or j > 64:
                old = array[i,j]
                array[i,j] = (array[i-1,j] + array[i+1,j] + array[i,j-1] + array[i,j+1]) / 4
                new = array[i,j]
                change = np.abs(new - old)
                del_V.append(change)

            if i < 60 or i > 64:
                old = array[i,j]
                array[i,j] = (array[i-1,j] + array[i+1,j] + array[i,j-1] + array[i,j+1]) / 4
                new = array[i,j]
                change = np.abs(new - old)
                del_V.append(change)

            else:
                change = 0
                del_V.append(change)

    del_V = np.asarray(del_V)
    max_del_V = max(del_V)
    del_V_sum = np.sum(del_V) / (123**2 - 25)

    array[60:65,60:65] = 1

    return(array,del_V_sum,max_del_V)

def Plotter(array,counter):

    savestring = '/Users/ballanr/Desktop/Computational/Homework 4/' + str(counter) + '.pdf'

    plt.figure(figsize=(13,10))
    plt.imshow(array,cmap='jet_r')
    plt.colorbar(orientation='vertical')
    plt.savefig(savestring,bbox_inches='tight',dpi=300)
    plt.clf()
    plt.close()

def Laplace_15(precision,loops,loop_type):

    array = np.random.rand(15,15)

    array[0] = 0
    array[-1] = 0
    array[:,0] = 0
    array[:,-1] = 0
    array[5:10,5:10] = 1
    #Plotter(array,0)

    if loop_type == 'for':

        del_V_array = []
        k = 0

        for i in range(loops):
            k += 1
            array1,del_V,max_del_V = Relaxation_15(array)
            #Plotter(array1,k)
            array = array1
            print(del_V)
            #del_V_array.append(del_V)
    
        return(del_V,k,array)
        
    elif loop_type == 'while':

        del_V_sum = 1
        max_del_V = 1
        k = 0

        while del_V_sum > precision and max_del_V > 2*precision:
            k += 1
            array1,del_V_sum,max_del_V = Relaxation_15(array)
            #Plotter(array1,k)
            array = array1
            print(del_V_sum)
            
        return(del_V_sum,k,array)

def Laplace_25(precision,loops,loop_type):

    array = np.random.rand(25,25)

    array[0] = 0
    array[-1] = 0
    array[:,0] = 0
    array[:,-1] = 0
    array[10:15,10:15] = 1
    #Plotter(array,0)

    if loop_type == 'for':

        del_V_array = []
        k = 0

        for i in range(loops):
            k += 1
            array1,del_V,max_del_V = Relaxation_25(array)
            #Plotter(array1,k)
            array = array1
            print(del_V)
            #del_V_array.append(del_V)
    
        return(del_V,k,array)
        
    elif loop_type == 'while':

        del_V_sum = 1
        max_del_V = 1
        k = 0

        while del_V_sum > precision and max_del_V > 2*precision:
            k += 1
            array1,del_V_sum,max_del_V = Relaxation_25(array)
            #Plotter(array1,k)
            array = array1
            print(del_V_sum)
            
        return(del_V_sum,k,array)

def Laplace_35(precision,loops,loop_type):

    array = np.random.rand(35,35)

    array[0] = 0
    array[-1] = 0
    array[:,0] = 0
    array[:,-1] = 0
    array[15:20,15:20] = 1
    #Plotter(array,0)

    if loop_type == 'for':

        del_V_array = []
        k = 0

        for i in range(loops):
            k += 1
            array1,del_V,max_del_V = Relaxation_35(array)
            #Plotter(array1,k)
            array = array1
            print(del_V)
            #del_V_array.append(del_V)
    
        return(del_V,k,array)
        
    elif loop_type == 'while':

        del_V_sum = 1
        max_del_V = 1
        k = 0

        while del_V_sum > precision and max_del_V > 2*precision:
            k += 1
            array1,del_V_sum,max_del_V = Relaxation_35(array)
            #Plotter(array1,k)
            array = array1
            print(del_V_sum)
            
        return(del_V_sum,k,array)

def Laplace_45(precision,loops,loop_type):

    array = np.random.rand(45,45)

    array[0] = 0
    array[-1] = 0
    array[:,0] = 0
    array[:,-1] = 0
    array[20:25,20:25] = 1
    #Plotter(array,0)

    if loop_type == 'for':

        del_V_array = []
        k = 0

        for i in range(loops):
            k += 1
            array1,del_V,max_del_V = Relaxation_45(array)
            #Plotter(array1,k)
            array = array1
            print(del_V)
            #del_V_array.append(del_V)
    
        return(del_V,k,array)
        
    elif loop_type == 'while':

        del_V_sum = 1
        max_del_V = 1
        k = 0

        while del_V_sum > precision and max_del_V > 2*precision:
            k += 1
            array1,del_V_sum,max_del_V = Relaxation_45(array)
            #Plotter(array1,k)
            array = array1
            print(del_V_sum)
            
        return(del_V_sum,k,array)

def Laplace_75(precision,loops,loop_type):

    array = np.random.rand(75,75)

    array[0] = 0
    array[-1] = 0
    array[:,0] = 0
    array[:,-1] = 0
    array[35:40,35:40] = 1
    #Plotter(array,0)
    
    if loop_type == 'for':

        del_V_array = []
        k = 0

        for i in range(loops):
            k += 1
            array1,del_V,max_del_V = Relaxation_75(array)
            #Plotter(array1,k)
            array = array1
            print(del_V)
            #del_V_array.append(del_V)
    
        return(del_V,k,array)
        
    elif loop_type == 'while':

        del_V_sum = 1
        max_del_V = 1
        k = 0

        while del_V_sum > precision and max_del_V > 2*precision:
            k += 1
            array1,del_V_sum,max_del_V = Relaxation_75(array)
            #Plotter(array1,k)
            array = array1
            print(del_V_sum)
            
        return(del_V_sum,k,array)

def Laplace_125(precision,loops,loop_type):

    array = np.random.rand(125,125)

    array[0] = 0
    array[-1] = 0
    array[:,0] = 0
    array[:,-1] = 0
    array[60:65,60:65] = 1
    #Plotter(array,0)
    

    if loop_type == 'for':

        del_V_array = []
        k = 0

        for i in range(loops):
            k += 1
            array1,del_V,max_del_V = Relaxation_125(array)
            #Plotter(array1,k)
            array = array1
            print(del_V)
            #del_V_array.append(del_V)
    
        return(del_V,k,array)
        
    elif loop_type == 'while':

        del_V_sum = 1
        max_del_V = 1
        k = 0

        while del_V_sum > precision and max_del_V > 2*precision:
            k += 1
            array1,del_V_sum,max_del_V = Relaxation_125(array)
            #Plotter(array1,k)
            array = array1
            print(del_V_sum)
            
        return(del_V_sum,k,array)

def Iterations():
    
    del_v1,k1,array1 = Laplace_15(10*(10**-6),10,'for')
    del_v2,k2,array2 = Laplace_15(10*(10**-6),50,'for')
    del_v3,k3,array3 = Laplace_15(10*(10**-6),100,'for')
    del_v4,k4,array4 = Laplace_15(10*(10**-6),150,'for')
    # del_v25,k25,array25 = Laplace_25(10*(10**-6),100,'while')
    # del_v35,k35,array35 = Laplace_35(10*(10**-6),100,'while')
    # del_v45,k45,array45 = Laplace_45(10*(10**-6),100,'while')
    # del_v75,k75,array75 = Laplace_75(10*(10**-6),100,'while')
    # del_v125,k125,array125 = Laplace_125(10*(10**-6),100,'while')

    del_v1 = np.log(del_v1)
    del_v2 = np.log(del_v2)
    del_v3 = np.log(del_v3)
    del_v4 = np.log(del_v4)

    plt.figure(figsize=(13,10))
    plt.scatter(k1,del_v1)
    plt.scatter(k2,del_v2)
    plt.scatter(k3,del_v3)
    plt.scatter(k4,del_v4)

    
    # x = np.arange(0,125,1)
    # plt.scatter(x,x**2)

    plt.show()

def Error_Grid_Size(size):

    del_v15,k15,array15 = Laplace_15(10*(10**-10),100,'while')

    if size == 25:

        del_v25,k25,array25 = Laplace_25(10*(10**-10),100,'while')

        big_array = array25[5:20,5:20]

        print(len(big_array[:,0]),len(array15[:,0]))
        big_avg = np.sum(big_array) / (15**2)
        array_15_avg = np.sum(array15) / (15**2)

        avg_diff = big_avg - array_15_avg
    
    elif size == 35:

        del_v25,k25,array35 = Laplace_35(10*(10**-10),100,'while')

        big_array = array35[10:25,10:25]

        print(len(big_array[:,0]),len(array15[:,0]))
        big_avg = np.sum(big_array) / (15**2)
        array_15_avg = np.sum(array15) / (15**2)

        avg_diff = big_avg - array_15_avg

    elif size == 45:

        del_v25,k25,array45 = Laplace_45(10*(10**-10),100,'while')

        big_array = array45[15:30,15:30]

        print(len(big_array[:,0]),len(array15[:,0]))
        big_avg = np.sum(big_array) / (15**2)
        array_15_avg = np.sum(array15) / (15**2)

        avg_diff = big_avg - array_15_avg

    elif size == 75:

        del_v25,k25,array75 = Laplace_75(10*(10**-10),100,'while')

        big_array = array75[30:45,30:45]

        print(len(big_array[:,0]),len(array15[:,0]))
        big_avg = np.sum(big_array) / (15**2)
        array_15_avg = np.sum(array15) / (15**2)

        avg_diff = big_avg - array_15_avg

    return(avg_diff)

def Initial_Conditions():

    del_v15,k15,array15 = Laplace_15(10*(10**-10),100,'while')
    del_v25,k25,array25 = Laplace_25(10*(10**-10),100,'while')

def Error_Grid_Plot():

    diff1 = Error_Grid_Size(25)
    diff2 = Error_Grid_Size(35)
    diff3 = Error_Grid_Size(45)
    diff4 = Error_Grid_Size(75)

    plt.figure(figsize=(13,10))
    plt.scatter((25,35,45,75),(diff1,diff2,diff3,diff4))
    plt.plot((25,35,45,75),(diff1,diff2,diff3,diff4))

    plt.show()

Iterations()

# del_v,k,array = Laplace_15(10**-6,100,'while')
# print(k)

# savestring = '/Users/ballanr/Desktop/test.pdf'

# plt.figure(figsize=(13,10))
# plt.xticks(size = 20)
# plt.yticks(size = 20)
# plt.imshow(array,cmap='jet_r')
# plt.colorbar(orientation='vertical')
# plt.savefig(savestring,bbox_inches='tight',dpi=300)
