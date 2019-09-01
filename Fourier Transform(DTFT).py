# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 21:23:20 2019

@author: Arnab Das
"""

import numpy as np
import matplotlib.pyplot as plt

N = 1

ft = []

a = np.arange(-10,10,1)
b = np.zeros(len(a))
ind = np.where(a==0)
b[ind] = 1

plt.subplot(2,1,1)
plt.stem(a,b)

w = np.pi/N

def DTFT(a):
    a = np.asarray(a)
    for k in range(len(a)):
        temp = 0
        for n in range(len(a)):
            xn = a[n]
            exp = np.exp(-2j*w*n*k)
            temp += xn*exp
            
        ft.append(temp)
    return ft

result = DTFT(b)

plt.subplot(2,1,2)
plt.stem(a,result)
plt.show()