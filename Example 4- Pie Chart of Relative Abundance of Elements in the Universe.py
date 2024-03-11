#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 18:32:08 2024

@author: brettnakao
"""

import matplotlib.pyplot as plt

elements = ['O','Si','Al','Fe','Ca']
abundance = [46.6, 27.7, 8.23, 5.0, 3.63]
plt.pie(abundance, labels=elements, autopct='%1.1f%%')
plt.title('Percent Abundance of Elements')
plt.legend(elements, loc='upper left', bbox_to_anchor=(1,0.5))
plt.show()