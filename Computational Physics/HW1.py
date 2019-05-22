import matplotlib.pyplot as plt
import numpy as np

def Radioactive_Spiders(timestep,gamma):
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    # Setting up time steps
    time_length = 1
    time_range = np.arange(0,time_length + timestep,timestep)

    tau_a = 1

    tau_b = tau_a / gamma

    N_A0 = 1000

    N_B = 0

    N_A_arr = []
    N_B_arr = []

    # Iteration loop
    for time in range(len(time_range)):

        if time_range[time] == 0:
            N_A = N_A0 * np.exp(-time_range[time]/tau_a)
            N_A_arr.append(N_A)
            N_B_arr.append(N_B)

        else:
            N_A = N_A0 * np.exp(-time_range[time]/tau_a)
            der_N_B = (N_A / tau_a) - (N_B / tau_b)
            N_B_1 = N_B + der_N_B * timestep
            N_A_arr.append(N_A)
            N_B_arr.append(N_B_1)
            N_B = N_B_1
    
    return(N_A_arr,N_B_arr,time_range)

    # y(t + h) = y(t) + y'(t)h

    # y'(t) = a(t) / tau_a - y(t) / tau_b
    
a1,b1,time1 = Radioactive_Spiders(0.01,1)
a2,b2,time2 = Radioactive_Spiders(0.01,1.5)
a3,b3,time3 = Radioactive_Spiders(0.01,2)

a4,b4,time4 = Radioactive_Spiders(0.01,0.5)
a5,b5,time5 = Radioactive_Spiders(0.01,0.25)
a6,b6,time6 = Radioactive_Spiders(0.01,0.125)
a7,b7,time7 = Radioactive_Spiders(0.01,10)

b_a_1 = np.asarray(b1) / np.asarray(a1)
b_a_2 = np.asarray(b2) / np.asarray(a2)
b_a_3 = np.asarray(b3) / np.asarray(a3)

b_a_4 = np.asarray(b4) / np.asarray(a4)
b_a_5 = np.asarray(b5) / np.asarray(a5)
b_a_6 = np.asarray(b6) / np.asarray(a6)
b_a_7 = np.asarray(b7) / np.asarray(a7)

plt.figure(figsize=(8,6))
# plt.plot(time1,b_a_1)
# plt.plot(time1,b_a_2)
plt.scatter(time1,b_a_1,s=3,marker = 'D',label='Gamma = 1')
plt.scatter(time1,b_a_2,s=3,marker = '*',label='Gamma = 1.5')
plt.scatter(time1,b_a_3,s=3,marker = ',',label='Gamma = 2')

plt.scatter(time4,b_a_4,s=3,marker = 'D',label='Gamma = 0.5')
plt.scatter(time5,b_a_5,s=3,marker = '*',label='Gamma = 0.25')
plt.scatter(time6,b_a_6,s=3,marker = ',',label='Gamma = 0.125')
plt.scatter(time7,b_a_7,s=3,marker = ',',label='Gamma = 0.001')

plt.legend()
plt.xlabel("T")
plt.ylabel("Nb / Na")
plt.savefig('/Users/Daemeyn/Desktop/test.pdf', bbox_inches='tight',dpi=300)

