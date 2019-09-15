# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 18:19:10 2019

@author: Arnab Das
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

fs = 200
freq = 2
k = 15
w = 2*np.pi*freq

"""input signal"""
n = np.linspace(0,1,fs)
u = signal.sawtooth(4*np.pi*n,0.5)
plt.subplot(5,3,1)
plt.stem(n,u , label = "i/p")
plt.legend()

"""coefficients for original signal"""
t = np.arange(0,k,1)
a = np.zeros(k)
b = np.zeros(k)
for i in range(0,k,1):
    cos = np.cos(w*i*n)
    sin = np.sin(w*i*n)
    for j in range(0,len(n),1):
        a[i] += (u[j]*cos[j])
        b[i] += (u[j]*sin[j])
        
plt.subplot(5,3,2)
plt.stem(t,a,label ="a")
plt.legend()
plt.subplot(5,3,3)
plt.stem(t,b,label = "b")
plt.legend()

"""linearity property"""
u1 = 0.3*u
a1 = np.zeros(k)
b1 = np.zeros(k)
for i in range(0,k,1):
    cos = np.cos(w*i*n)
    sin = np.sin(w*i*n)
    for j in range(0,len(n),1):
        a1[i] += (u1[j]*cos[j])
        b1[i] += (u1[j]*sin[j])

u2 = 0.7*u
a2 = np.zeros(k)
b2 = np.zeros(k)
for i in range(0,k,1):
    cos = np.cos(w*i*n)
    sin = np.sin(w*i*n)
    for j in range(0,len(n),1):
        a2[i] += (u2[j]*cos[j])
        b2[i] += (u2[j]*sin[j])
               
plt.subplot(5,3,4)
plt.stem(t,a1,label = "a1")
plt.legend()
plt.subplot(5,3,5)
plt.stem(t,b1,label = "b1")
plt.legend()
plt.subplot(5,3,6)
plt.stem(t,a2,label = "a2")
plt.legend()
plt.subplot(5,3,7)
plt.stem(t,b2,label = "b2")
plt.legend()

#verifying linearity
a3 = a1+a2
b3 = b1+b2
u3 = np.zeros(len(n))
for i in range(0,k,1):
    cos=np.cos(w*n*i)
    sin=np.sin(w*n*i)
    for j in range(0,len(n),1):
        u3[j] += (a3[i]*cos[j] + b3[i]*sin[j])
        
plt.subplot(5,3,8)
plt.stem(n,u3,label = "ver of lin")
plt.legend()

"""Time shifting"""
To = 100

#changed input signal
n1 = np.linspace(0+To,1+To,fs)
u1 = signal.sawtooth(4*np.pi*n,0.5)
plt.subplot(5,3,9)
plt.stem(n1,u1,label = "Time shif.")
plt.legend()

#coefficients of changed input signal
a4 = np.zeros(k)
b4 = np.zeros(k)
for i in range(0,k,1):
    cos = np.cos(w*i*n1)
    sin = np.sin(w*i*n1)
    for j in range(0,len(n1),1):
        a4[i] += (u1[j]*cos[j])
        b4[i] += (u1[j]*sin[j])

plt.subplot(5,3,10)
plt.stem(t,a4,label = "a4")
plt.legend()
plt.subplot(5,3,11)
plt.stem(t,b4,label = "b4")
plt.legend()

"""Frequency Shifting"""
Wo = 10
a5 = np.zeros(k)
b5 = np.zeros(k)
u2 = np.zeros(len(n))
for i in range(Wo,k,1):
    a5[i] = a[i-Wo]
    b5[i] = b[i-Wo]
    
for i in range(0,k,1):
    cos=np.cos(w*n*i)
    sin=np.sin(w*n*i)
    for j in range(0,len(u2),1):
        u2[j] += (a5[i]*cos[j] + b5[i]*sin[j])

plt.subplot(5,3,12)
plt.stem(t,a5,label = "a5")
plt.legend()
plt.subplot(5,3,13)
plt.stem(t,b5,label = "b5")
plt.legend()
plt.subplot(5,3,14)
plt.plot(n,u2,label = "freq shifted")
plt.legend()
plt.show()