# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 11:33:49 2019

@author: Arnab Das
"""

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.io.wavfile import write

duration = 5  # seconds

fs = 44100
x = np.linspace(0,duration*fs,duration*fs)
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
sd.wait()
plt.plot(x,myrecording)
sd.play(myrecording,fs)
write("save1.wav", fs, myrecording)
