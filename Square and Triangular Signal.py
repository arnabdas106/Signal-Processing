# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 18:22:03 2019

@author: Arnab Das
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

"""for tiaingular amplitude from 0->1"""
fs = 500
freq = 10
x = np.linspace(0,1,fs)
y = (1+signal.sawtooth(2*np.pi*freq*x,0.5))/2
plt.subplot(4,1,1)
plt.plot(x,y)
plt.show()

"""for amplitude from -1->1"""
y = signal.sawtooth(2*np.pi*freq*x,0.5)
plt.subplot(4,1,2)
plt.plot(x,y)
plt.show()

"""for square signal ampliude -1->1"""
y = signal.square(2*np.pi*freq*x,0.5)
plt.subplot(4,1,3)
plt.plot(x,y)
plt.show()

"""for square signal ampliude 0->1"""
y = (1+signal.square(2*np.pi*freq*x,0.5))/2
plt.subplot(4,1,4)
plt.plot(x,y)
plt.show()
