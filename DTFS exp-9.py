# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 22:33:46 2019

@author: Arnab Das
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

#signal
#....
fs=200
freq=2
k=10
f=float(1/fs)
w=2*np.pi*freq

x = np.linspace(0,1,fs)
u = signal.sawtooth(4*np.pi*x,0.5)
plt.subplot(2,2,1)
plt.title("Input Signal")
plt.plot(x,u,label = "Input")
plt.legend()

#calculation
a=np.zeros(k)
b=np.zeros(k)
x1 = np.arange(0,k,1)
for i in range(0,k,1):
    cos=np.cos(w*x*i)
    sin=np.sin(w*x*i)
    for j in range(0,len(u),1):
        a[i] += u[j]*cos[j]
        b[i] += u[j]*sin[j]
        
plt.subplot(2,2,2)
plt.title("an")
plt.stem(x1,a,label = "an")
plt.subplot(2,2,3)
plt.legend()
plt.title("bn")
plt.stem(x1,b,label = "bn")
plt.legend()
        
#verification
t=np.arange(0,k,1)
x2=np.zeros(len(u))

for i in range(0,k,1):
    cos=np.cos(w*x*i)
    sin=np.sin(w*x*i)
    for j in range(0,len(u),1):
        x2[j] += a[i]*cos[j]+b[i]*sin[j]
        
plt.subplot(2,2,4)
plt.title("Verification")
plt.plot(x,x2,label = "Ver.")
plt.legend()
plt.show()
