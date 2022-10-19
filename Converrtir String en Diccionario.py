# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 09:13:38 2022

@author: Xavier
"""

a = """name: Alex Fox
age: 12

class: 12b"""

t = [i.strip() for i in a.split('\n') if i]
d = {}
print(t)

for elem in t:
    key, val = (i.strip() for i in elem.split(":"))
    d[key] = int(val) if val.isdecimal() else val
print(d)