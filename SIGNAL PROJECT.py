# -*- coding: utf-8 -*
"""
Created on Fri Sep 27 19:47:25 2019
@author: Arnab Das
"""
"""the builtin function sd.rec() records sound and a makes a 2d array in
time domain which python treats it as a matrix....so fft function wont work.At
 that time we need to use fft2()(2 means 2-d array). 
if you don't want to use fft2() flatten the recorded signal to make a 2-d array
to a 1-d array"""


import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fftpack import fft
import numpy as np
from scipy import signal
import scipy.io.wavfile
import time

print(" Welcome to NOISE CANCELLATION centre ")

"""details for sound recording"""
Fs = int(input("Enter the sampling frequency: "))

duration=int(input("Enter the duration of your recording: "))

lowcut = int(input("Enter lowcut: "))
highcut = int(input("Enter highcut: "))
while(lowcut>highcut):
    print("Invalid Inputs....Enter again")
    lowcut = int(input("Enter lowcut: "))
    highcut = int(input("Enter highcut: "))
while(highcut>=int(Fs/2)):
    highcut = int(input("Enter highcut frequency less than "+str(Fs/2)+" : "))
    
nyq = 0.5*Fs
low = lowcut/nyq
high = highcut/nyq


"""Recording"""
print("Start Speaking")
"""t = np.arange(0,duration,1/Fs)
a = np.sin(2*np.pi*500*t)"""
myrecording = sd.rec(int(duration*Fs) , Fs , 1 , blocking = "True")
myrecording = myrecording.flatten()
scipy.io.wavfile.write('save.wav',Fs,myrecording)

print("End Recording")

#play
sd.play(myrecording,Fs)
time.sleep(duration+1)

"""tranforming time domain to freq domain DTFT"""
X_f = fft(myrecording)

#create freq axis
n = np.size(myrecording)
fr = (Fs/2)*np.linspace(0,1,round(n/2))
X_m = (2/n)*abs(X_f[0:np.size(fr)])

    
order = 2
b,a = scipy.signal.butter(order, [low, high], 'bandpass',analog = False)
y = scipy.signal.filtfilt(b,a,myrecording,axis = 0)
sd.play(y,Fs)

"""plot the recorded sound"""
plt.title("Recorded Signal")
plt.plot(myrecording)

#plot spectrum
plt.figure()
plt.xlabel("Freq")
plt.ylabel("Magnitude")
plt.title("Sound Spectrum")
plt.plot(fr,X_m)

plt.figure()
plt.title("Filtered Signal")
plt.plot(y)
