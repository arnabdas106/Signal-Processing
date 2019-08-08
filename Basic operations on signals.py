# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 18:41:13 2019

@author: Arnab Das
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

x1 = np.linspace(0,1,500)
y1 = np.sin(2*np.pi*5*x1)

y2 = signal.square(2*np.pi*5*x1)
plt.grid(True)

plt.subplot(5,2,1)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Sine Function")
plt.plot(x1,y1)

plt.subplot(5,2,2)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Square Signal")
plt.plot(x1,y2)

z = y1+y2 #addition of two signals

plt.subplot(5,2,3)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Result")
plt.plot(x1,z)


#Amplitude Scaling
plt.subplot(5,2,4)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Amplitude Scaling")
plt.plot(x1,0.5*z)

#Time Shifting
plt.subplot(5,2,5)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Time Shifting +")
plt.plot(x1+2,z)

#Time Shifting
plt.subplot(5,2,6)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Time Shifting -")
plt.plot(x1-2,z)

#Time Scaling
plt.subplot(5,2,7)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Time Scaling")
plt.plot(2*x1,z)

#Time Reversal
plt.subplot(5,2,8)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Time Reversal")
plt.plot(-1*x1,z)

plt.show()