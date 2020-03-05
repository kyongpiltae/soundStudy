#%% 
import numpy as np
import matplotlib.pyplot as plt

#%% 
#simple signwave

A =.8
f0 = 1000
phi = np.pi /2
fs = 44100

t = np.arange (-0.002,.002,1.0/fs)
x = A * np.cos(2*np.pi *f0 * t +phi)

plt.plot(t,x)
plt.axis([-.002,.002, -.8,.8])
plt.xlabel('time')
plt.ylabel("Amplitude")
plt.show()

#%% 

#complex sinewave
# real part of sine
N = 500
k = 3 # period
n = np.arange(-N/2,N/2)
s = np.exp(1j *2 * np.pi * k *n / N )
plt.plot(n,np.real(s))
plt.axis([-N/2,N/2-1,-1,1])
plt.xlabel('n')
plt.ylabel("amplitude")
plt.show()

# %%
#iamagenary part
# 3 period off 
N = 500
k = 3 # period
n = np.arange(-N/2,N/2)
s = np.exp(1j *2 * np.pi * k *n / N )
plt.plot(n,np.imag(s))
plt.axis([-N/2,N/2-1,-1,1])
plt.xlabel('n')
plt.ylabel("amplitude")
plt.show()

# %%
N = 32 # 32 sample 
k = 5 # period wave 갯수 
n = np.arange(-N/2,N/2)
s = np.exp(1j *2 * np.pi * k *n / N )
plt.plot(n,np.imag(s))
plt.axis([-N/2,N/2-1,-1,1])
plt.xlabel('n')
plt.ylabel("amplitude")
plt.show()

# %%
