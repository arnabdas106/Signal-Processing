# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 11:36:36 2019

@author: Arnab Das
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

#input signal
fs = 200
temp = 0
an = []
bn = []
x = np.linspace(0,1,fs)
a = signal.sawtooth(4*np.pi*x,0.5)
plt.subplot(2,2,1)
plt.plot(x,a)

for N in range(0,15,1):
    an.append(np.trapz(a*np.cos(N*x),x))
    bn.append(np.trapz(a*np.sin(N*x),x))

x1 = np.linspace(0,1,len(an))
plt.subplot(2,2,2)
plt.stem(x1,an)
plt.subplot(2,2,3)
plt.stem(x1,bn)

plt.subplot(2,2,4)
for i in range(0,15,1):
    a1 = an[i]*np.cos(x*i)
    a2 = an[i]*np.sin(x*i)
    temp = a1+a2
    
plt.plot(x,temp)
plt.show()