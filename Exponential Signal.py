# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 18:16:14 2019

@author: Arnab Das
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10,10,0.1)
y = np.exp(x)

plt.title("Exponential Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.plot(x,y)
plt.show()