# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 18:18:03 2019

@author: Arnab Das
"""

import numpy as np
import matplotlib.pyplot as plt

freq = 10
Ts = 0.01
t = np.arange(0,1,Ts)
x = np.sin(2*np.pi**freq*t)
y = np.cos(2*np.pi*freq*t)

plt.title("Complex Signal")
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.plot(t,x,label = "Sine Wave")
plt.plot(t,y,label="Cosine Wave")
plt.legend()
plt.show()