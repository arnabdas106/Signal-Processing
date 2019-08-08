import numpy as np
import matplotlib.pyplot as plt

freq = 10
Ts = 0.001
t = np.arange(0,1,Ts)
x = np.sin(2*np.pi*freq*t)

plt.title("Simple sine (1 Hz)")
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.plot(t,x)
plt.show()