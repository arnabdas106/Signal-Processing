# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 22:34:42 2019

@author: Arnab Das
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10,10,1)
y = np.zeros(len(x))
ind = np.where(x>=0)
y[ind] = 1

plt.title("Step Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.stem(x,y)
plt.show()