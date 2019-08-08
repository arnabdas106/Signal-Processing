# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 22:30:17 2019

@author: Arnab Das
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

freq = 10
fs = 1000
x = np.linspace(0,1,fs)
y = (signal.square(2*np.pi*freq*x)+1)/2
#plt.ylim(0,2)
plt.plot(x,y)
plt.show()