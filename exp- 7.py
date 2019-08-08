# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 11:49:09 2019

@author: Arnab Das
"""

import numpy as np
import matplotlib.pyplot as plt
freq=10
temp=0
y5=[]
y6=[]
c1=[]
c2=[]
temp1=[]
temp2=[]
subplots=5
x1=np.arange(0,1,0.01)
y1=2*(np.sinc(2*10*np.pi*x1))
plt.subplot(subplots,2,1)
plt.ylabel("Amp")
plt.stem(x1,y1,label="h1[n]")
plt.legend()

x2=np.arange(0,1,0.01)
y2=-3*np.sinc(2*10*np.pi*x2)
plt.subplot(subplots,2,2)
plt.ylabel("Amp")
plt.stem(x2,y2,label="h1[n]")
plt.legend()

x3=np.arange(0,1,0.01)
y3=5*np.sinc(2*10*np.pi*x3)
x3+=5
plt.subplot(subplots,2,3)
plt.ylabel("Amp")
plt.stem(x3,y3,label="h3[n]")
plt.legend()

x4=np.linspace(0,1,100)
y4=y1+y2
plt.subplot(subplots,2,4)
plt.ylabel("amp")
plt.stem(x4,y4,label="w1=[n]")
plt.legend()
for i in range(len(y3)):
    for j in range(0,i+1,1):
        temp+=(y3[j]*y4[i-j])
    y5.append(temp)
    temp=0
plt.subplot(subplots,2,5)
x5=np.linspace(0,1,100)
plt.ylabel("amp")
plt.stem(x5,y5, label = "W1[n] * h3[n]")
plt.legend()

plt.subplot(5,2,6)
temp1 = np.convolve(y4,y3)
for i in range(len(x5)):
    c1.append(temp1[i]) 
plt.ylabel("Amp.")
plt.stem(x5,c1,label = "w1 convolve h3")

a = np.arange(0,1,0.01)
b = 7*(np.sin(2*freq*np.pi*a))
plt.subplot(subplots,2,7)
plt.ylabel("Amp.")
plt.stem(a,b,label = "X[n]")
plt.legend()

plt.subplot(subplots,2,8)
temp2=np.convolve(b,y5)
for i in range(len(a)):
    c2.append(temp2[i])
plt.ylabel("Amp.")
plt.stem(x5,c2,label="x1 convolve h[n]")
plt.legend()

temp=0
for i in range(len(y5)):
    for j in range(0,i+1,1):
        temp+=(b[j]*y5[i-j])
    y6.append(temp)
    temp=0
    
plt.subplot(subplots,2,9)
x6=np.linspace(0,1,100)
plt.ylabel("amp.")
plt.stem(x6,y6,label="x[n]*h[n]")
plt.legend()
plt.show()
    
