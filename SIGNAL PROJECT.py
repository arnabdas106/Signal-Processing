# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 19:47:25 2019

@author: Arnab Das
"""

"""before using this code make sure to install 'sounddevice' library
    pip install sounddevice"""

"""the builtin function sd.rec() records sound and a makes a 2d array in
time domain which python treats it as a matrix....so fft function wont work.At that time we need
to use fft2()(2 means 2-d array). 
if you don't want to use fft2() flatten the recorded signal to make a 2-d array
to a 1-d array"""


import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fftpack import fft, fft2
import numpy as np

"""details for sound recording"""
Fs = 16000
duration = 3

"""Recording"""
print("Start Speaking")
"""t = np.arange(0,duration,1/Fs)
a = np.sin(2*np.pi*500*t)"""
myrecording = sd.rec(int(duration*Fs) , Fs , 1 , blocking = "True")
myrecording = myrecording.flatten()

print("End Recording")

#play
sd.play(myrecording,Fs)

"""plot the recorded sound"""
plt.title("Recorded Signal")
plt.plot(myrecording)

"""tranforming time domain to freq domain DTFT"""
X_f = fft(myrecording)

#create freq axis
n = np.size(myrecording)
fr = (Fs/2)*np.linspace(0,1,round(n/2))
X_m = (2/n)*abs(X_f[0:np.size(fr)])

#plot spectrum
plt.figure()
plt.xlabel("Freq")
plt.ylabel("Magnitude")
plt.title("Sound Spectrum")
plt.plot(fr,X_m)
