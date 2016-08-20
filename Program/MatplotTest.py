'''
Created on 20151001

@author: le
'''

import matplotlib.pyplot as plt

import numpy as np

x = np.linspace(0, 2 * np.pi, 1000)

y = np.sin(x)

z = np.cos(x)

y1 = [0 for i in x]

#t = np.tan(x)

plt.grid()

plt.title(r'$y=sin(x)$')

ax1 =  plt.subplot(2,2,1)

ax1.plot(x,y, label=r'$sin(x)$')

ax1.plot(x,z, label=r'$cos(x)$')

ax1.plot(x, y1)

ax1.legend()

ax2 = plt.subplot(2,1,2)

ax2.plot(x,x)

ax2.set_xlabel('x')
ax2.set_ylabel('y')


ax3 = plt.subplot(2,2,2)

#ax4 = plt.subplot(3,1,3)

#plt.legend(r'$cos(x)$')

#plt.plot(x,t)

plt.show()