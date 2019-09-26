from scipy.signal import filtfilt
from scipy import stats
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
import sounddevice as sd
from scipy.io.wavfile import write


def plot():
    data = pd.read_csv('./save.csv')
    sensor_data = data[['data']]
    
    sensor_data = np.array(sensor_data)
    time = np.linspace(0,0.0002,44100)
    plt.subplot(2,1,1)
    plt.plot(time,sensor_data)
    plt.show()
    sd.play(sensor_data,44100)
    sd.wait()
    filtered_signal = bandpass(sensor_data)
    plt.subplot(2,1,2)
    plt.plot(time,filtered_signal)
    plt.show()
    sd.play(filtered_signal,44100)
    sd.wait()
    
def bandpass(signal):
    fs = 44100.0
    lowcut = 400.0
    highcut = 2000.0
    
    nyq = 0.5*fs
    low = lowcut/nyq
    high = highcut/nyq
    
    order = 2
    b,a = scipy.signal.butter(order, [low, high], 'bandpass',analog = False)
    y = scipy.signal.filtfilt(b,a,signal,axis = 0)
    return(y)
    

duration = 1  # seconds

fs = 44100
x = np.linspace(0,duration*fs,duration*fs)
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
sd.wait()

#np.savetxt("save.csv",myrecording,delimiter = ',')
plot()
