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


"""X1[n]"""
plt.subplot(2,2,1)
x1 = np.linspace(0,1,fs)
y1 = signal.square(2*np.pi*freq*x1)
l1 = len(y1)
plt.title("X1[n]")
plt.plot(x1,y1)

"""X2[n]"""
plt.subplot(2,2,2)
x2 = np.linspace(0,1,fs)
y2 = np.sin(2*np.pi*freq*x2)
l2 = len(y2)
plt.title("X2[n]")
plt.plot(x2,y2)

N = l1+l2-1
"""using builtin convolve func."""
plt.subplot(2,2,3)
x = np.linspace(0,1,N)
y = np.convolve(y1,y2)
plt.title("Convolve")
plt.plot(x,y)

yy = np.zeros(N)
"""without builtin convolve func."""
for i in range(0,N,1):
    for j in range(0,i+1,1):
        if j<l1 and i-j<l2:
            yy[i] += y1[j]*y2[i-j]
plt.subplot(2,2,4)
plt.title("Verfication")
plt.plot(x,yy)
plt.show()
