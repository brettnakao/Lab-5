#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 18:08:30 2024

@author: brettnakao
"""

import numpy as np

masses = np.array([2, 4, 6, 8])
velocities = np.array([3, 6, 9, 12])

y = np.empty(len(masses))

for i in range(len(masses)):
    mass = masses[i]
    velocity = velocities[i]
    kinetic_energy = 0.5 * mass * velocity**2
    y[i] = kinetic_energy
    
import matplotlib.pyplot as plt

plt.bar(masses, y)
plt.xlabel('mass')
plt.ylabel('kinetic energy')
plt.title('kinetic energy bar graph')
plt.xticks(masses)
plt.show()