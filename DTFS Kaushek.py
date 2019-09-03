import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

#signal
#....
fs=200
freq=2
k=15
f=float(1/fs)
w=2*np.pi*freq

x = np.linspace(0,1,fs)
u = signal.sawtooth(4*np.pi*x,0.5)
plt.subplot(2,2,1)
plt.plot(x,u)

#calculation
a=np.zeros(k)
b=np.zeros(k)
x1 = np.arange(0,k,1)
for i in range(0,k,1):
    cos=np.cos(w*x*i)
    sin=np.sin(w*x*i)
    for j in range(0,len(u),1):
        a[i]=a[i]+(u[j]*cos[j])
        b[i]=b[i]+(u[j]*sin[j])
        
plt.subplot(2,2,2)
plt.stem(x1,a)
plt.subplot(2,2,3)
plt.stem(x1,b)
        
#verification
t=np.arange(0,k,1)
x2=np.zeros(len(u))

for i in range(0,k,1):
    cos=np.cos(w*x*i)
    sin=np.sin(w*x*i)
    for j in range(0,len(u),1):
        x2[j]=x2[j]+(a[i]*cos[j]+b[i]*sin[j])
        
plt.subplot(2,2,4)
plt.plot(x,x2)