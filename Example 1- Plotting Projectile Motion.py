#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:57:13 2024

@author: brettnakao
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants
v0 = 2.2 # in m/s
theta = 30 # in degrees
g = 9.8 # in m/s^2s

theta_rad = np.radians(theta)

# Calculate initial velocities along x and y
v0_y = v0*np.sin(theta_rad)
v0_x = v0*np.cos(theta_rad)

# Calculate total time
t_total = 2*v0_y/g

time_intervals = np.linspace(0, t_total, 20)

# Create empty arrays
x = np.empty(len(time_intervals))
y = np.empty(len(time_intervals))

# Fill arrays with x and y values
for i in range(len(time_intervals)):
    x_t = v0_x*time_intervals[i]
    y_t = v0_y*time_intervals[i] - .5*g*time_intervals[i]**2
    x[i] = x_t
    y[i] = y_t

# Plot the curves
plt.subplot(1,3,1)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('x vs y')

plt.subplot(1,3,2)
plt.plot(time_intervals, x)
plt.xlabel('time')
plt.ylabel('x')
plt.title('x vs t')

plt.subplot(1,3,3)
plt.plot(time_intervals, y)
plt.xlabel('time')
plt.ylabel('y')
plt.title('y vs t')

plt.tight_layout()
plt.show()

