'''
Created on 20151001

@author: le
'''
'''
Created on 20151001

@author: le
'''
# -*- coding: utf-8 -*- 
#coding=utf-8

import matplotlib.pyplot as plt

import numpy as np

x = np.linspace(0, 100, 10000)

y = x ** 2

z = x ** 3

f1 = np.abs(np.sin(x)) * x

f2 = np.power(x, np.e)

f3 = np.power(1+ 1/x, x)

f4 = x * np.log2(x)

f5 = np.power(1.03, x)

f6 = np.tan(x)

y1 = [0 for i in x]

#t = np.tan(x)

plt.grid()

plt.title(u'函数测试')

ax1 =  plt.subplot(1,1,1)

ax1.plot(x,y, label=r'$x^2$')

ax1.plot(x,z, label=r'$x^3$')

ax1.plot(x, f1, label=r'$x\sin(x)$')

ax1.plot(x, f2, label=r'$x^e$')

#ax1.plot(x, f3, label=r'$(1+\frac{1}{x})^x$')

ax1.plot(x, f4, label=r'$x*\log{_2}{^x}$')

ax1.plot(x, f5, label=r'$1.03^x$')

#ax1.plot(x, f6, label=r'$\tan(x)$')

ax1.plot(x, y1)

ax1.set_ylim(0, 100)

ax1.legend(loc='best')

ax1.set_xlabel('X')
ax1.set_ylabel('Y')

ax1.set_xticks(np.arange(0,100,10))

# ax2 = plt.subplot(2,1,2)
# 
# ax2.plot(x,x)
# 
# ax2.set_xlabel('x')
# ax2.set_ylabel('y')
# 
# 
# ax3 = plt.subplot(2,2,2)

#ax4 = plt.subplot(3,1,3)

#plt.legend(r'$cos(x)$')

#plt.plot(x,t)

plt.show()
