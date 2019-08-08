# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 22:23:25 2019

@author: Arnab Das
"""

import numpy as np
import matplotlib.pyplot as plt

Ts = 1
x = np.arange(-10,10,Ts)
l = len(x)
y = np.zeros(l)
ind = np.where(x==0)
y[ind] = 1

plt.title("Impulse Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.stem(x,y)
plt.show()