# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 20:00:06 2019

@author: Arnab Das
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

freq = 10
fs = 1000
temp = 0
yy=np.zeros(1999)

plt.subplot(3,1,1)
x1 = np.linspace(0,1,fs)
y1 = signal.square(2*np.pi*freq*x1)
l1 = len(y1)
plt.plot(x1,y1)

plt.subplot(3,1,2)
x2 = np.linspace(0,1,fs)
y2 = np.sin(2*np.pi*freq*x2)
l2 = len(y2)
plt.plot(x2,y2)

plt.subplot(3,1,3)
x = np.linspace(0,1,1999)
y = np.convolve(y1,y2)
N = l1+l2-1
plt.plot(x,y)
plt.show()

"""for i in range(len(x1)):
    for j in range(0,i+1,1): 
        temp+=(y1[j]*y2[i-j])
    yy.append(temp)
    temp = 0"""
for i in range(0,N,1):
    for j in range(0,i+1,1):
        if j<l1 and i-j<l2:
            yy[i]+=y1[j]*y2[i-j]
    
plt.plot(x,yy)