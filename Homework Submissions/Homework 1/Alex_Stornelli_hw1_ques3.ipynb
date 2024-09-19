# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 12:58:59 2024

@author: alexs
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define Constants
K = 1e7
r = 0.1

# function that returns dQ/dt
def model(N,t):
    dNdt = r*N*(1-N/K)
    return dNdt

# initial condition for charge
N0 = [1e6,9e5,2e7]

# time points
t = np.linspace(0,100)

for n in N0:
    # solve ODE
    N = odeint(model,n,t)
    plt.plot(t,N,label='N_0')
# plot results
plt.xlabel('Time')
plt.ylabel('N(t)')
plt.show()

for n in N0:
    N = odeint(model,n,t)
    dNdt = (N[1:]-N[:-1])/(t[1:]-t[:-1])
    plt.plot(N[1:],dNdt)
    
plt.xlabel(r'$N$')
plt.ylabel(r'$\dot{N}$')
plt.show()
