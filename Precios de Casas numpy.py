# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 15:36:09 2021

@author: Xavier
"""

import numpy as np

data = np.array([150000, 125000, 320000, 540000, 200000, 120000,
                 160000, 230000, 280000, 290000, 300000, 500000,
                 420000, 100000, 150000, 280000])

m = np.mean(data)
s = np.std(data)

low = m - s
high = m + s

print(len(data[(low < data) & (data < high)]) / len(data) * 100)