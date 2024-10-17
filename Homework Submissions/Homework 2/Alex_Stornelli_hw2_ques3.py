# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 10:22:52 2024

@author: alexs
"""

import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(r, x):
    return r * x - np.sin(x)

# Define values of r
r_values = [-0.5, 0, 0.5, 1.5]

# Create an array of x values
x = np.linspace(-10, 10, 400)

# Set up the plot
plt.figure(figsize=(8, 6))

# Plot the function for different values of r
for r in r_values:
    plt.plot(x, f(r, x), label=f'r = {r}')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('$\dot{x}$')
plt.title('$\dot{x}$ for different values of r')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
