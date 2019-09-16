# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 22:00:02 2019

@author: Arnab Das
"""

import numpy as np
import matplotlib.pyplot as plt

fs = 200
freq = 1
ft = []

a = np.arange(-10,10,1)
b = np.zeros(len(a))
ind = np.where(a==0)
b[ind] = 1

plt.subplot(2,1,1)
plt.stem(a,b)

w = np.pi*freq

"""DTFT"""

for k in range(len(b)):
    temp = 0
    for n in range(len(b)):
        xn = b[n]
        exp = np.exp(-2j*w*n)
        temp += xn*exp
    ft.append(temp)
 
plt.subplot(2,1,2)
plt.stem(a,ft)
plt.show()
