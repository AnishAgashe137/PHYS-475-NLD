# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 11:19:28 2024

@author: alexs
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameters
c_min, c_max = -2.0, 0.5  # Range of c (real axis)
c_values = np.linspace(c_min, c_max, 1000)  # Discretize c
iterations = 1000  # Number of iterations
last_iterations = 100  # Points to visualize after transient behavior

# Initialize an empty list to store bifurcation points
bifurcation_points = []

# Generate bifurcation data
for c in c_values:
    z = 0  # Start with z_0 = 0
    trajectory = []
    for i in range(iterations):
        z = z**2 + c
        # Store the last few iterations for visualization
        if i >= iterations - last_iterations:
            trajectory.append(z.real)  # Only take the real part for bifurcation
    bifurcation_points.extend((c, x) for x in trajectory)

# Extract c and z values for plotting
c_vals, z_vals = zip(*bifurcation_points)

# Plot bifurcation diagram
plt.figure(figsize=(10, 6))
plt.scatter(c_vals, z_vals, s=0.1, color="black", alpha=0.5)
plt.title("Bifurcation Diagram for the Mandelbrot Set (Real Axis)")
plt.xlabel("Real part of c")
plt.ylabel("Real part of z")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()
