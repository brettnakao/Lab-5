#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:57:13 2024

@author: brettnakao
"""

import numpy as np

# Constants
vo = 30 # m/s
theta = 45 # in degrees
g = 9.8 # in m/s^2

theta_rad = np.radians(theta)

# Calculate initial velocities along x and y
vo_y = vo*np.sin(theta_rad)
vo_x = vo*np.cos(theta_rad)

# Calculate total time
t_total = 2*vo_y/g

time_intervals = np.linspace(0, t_total, 10)

x = np.empty(len(time_intervals))
y = np.empty(len(time_intervals))

for i in range(len(time_intervals)):
    x_t = vo_x*time_intervals[i]
    y_t = vo_y*time_intervals[i] - .5*g*time_intervals[i]**2
    x[i] = x_t
    y[i] = y_t

# Plot the curves
import matplotlib.pyplot as plt

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

