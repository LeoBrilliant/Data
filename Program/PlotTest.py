'''
Created on 20151001

@author: le
'''
# -*- coding: utf-8 -*- 
#coding=utf-8

import matplotlib.pyplot as plt

import numpy as np

x = np.linspace(0, 100, 10000)

y = np.sin(x)

z = np.cos(x)

f1 = np.sqrt(x)

f2 = np.power(x, 1/3.0)

f3 = x**2

f4 = np.log(x)

f5 = np.log2(x)

f6 = np.log10(x)

f7 = np.power(1+ 1/x, x)

y1 = [0 for i in x]

#t = np.tan(x)

plt.grid()

plt.title(u'函数测试')

ax1 =  plt.subplot(1,1,1)

ax1.plot(x,y, label=r'$sin(x)$')

ax1.plot(x,z, label=r'$cos(x)$')

ax1.plot(x, f1, label=r'$\sqrt{x}$')

ax1.plot(x, f2, label=r'$\sqrt[3]{x}$')

#ax1.plot(x, f3, label=r'$x^2$')

ax1.plot(x, f4, label=r'$\ln{^x}$')

ax1.plot(x, f5, label=r'$\log^x_2$')

ax1.plot(x, f6, label=r'$\lg{x}$')

ax1.plot(x, f7, label=r'$(1+\frac{1}{x})^x$')

ax1.plot(x, y1)

#ax1.set_ylim(0, 100)

ax1.legend(loc='lower right')

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
