# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 14:50:13 2022

@author: Xavier
"""

data = [1, 2, 3, 4, 5]



for i in data[:]:
    x = data.count(i)
    if x == 1:
        data.remove(i)
        
print(data)

