# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 09:14:28 2019

@author: Arnab Das
"""

import matplotlib.pyplot as plt
import numpy as np

N = 26
ft = []
freq = 10
fs = 1000
conv = []

"""H(jw)"""
a = np.linspace(0,2*np.pi,N)
b = np.zeros(len(a))
ind1 = np.where(a>np.pi/2)
b[ind1] = 10
ind2 = np.where(a>3*np.pi/2)
b[ind2] = 0

plt.subplot(4,1,1)
plt.title("H(jw)")
plt.stem(a,b,label = "H(jw)")
plt.legend()


"""IFT"""
for t in range(0,len(a),1):
    sum=0
    w=a[t]
    for i in range(0,25,1):
        sum=sum+(((b[i])*np.complex(np.cos(w*i),np.sin(w*i))))
    ft.append(sum.real)


a1 = np.linspace(0,26,26)
plt.subplot(4,1,2)
plt.title("Inverse Fourier transform")
plt.stem(a1,ft,label = "IFT")
plt.legend()

"""Input Signal"""
a2 = np.linspace(0,1,fs)
b2 = np.sin(2*np.pi*freq*a2)
plt.subplot(4,1,3)
plt.title("Input Signal")
plt.stem(a2,b2,label = "i/p")
plt.legend()


"""Convolution"""
l1 = len(ft)
l2 = len(b2)
No = l1+l2-1
conv = np.convolve(ft,b2)

t = np.linspace(0,1,No)
plt.subplot(4,1,4)
plt.title("x(n)")
plt.stem(t,conv,label = "x(n)")
plt.legend()
plt.show()
