'''
Created on 20150210

@author: le
'''
#-*- coding: utf-8 -*- 
#coding=utf-8
from win32gui import *

titles = set()

def foo(hwnd, nouse):
    if IsWindow(hwnd) and IsWindowEnabled(hwnd) and IsWindowVisible(hwnd):
        print GetWindowText(hwnd)
        #titles.add(GetWindowText(hwnd))
        
EnumWindows(foo, 0)
lt = [t for t in titles if t ]
lt.sort()

for t in lt:
    print t    
if __name__ == '__main__':
    print "HelloWorld.py"
    print u'流浪'
    print '中文'
    pass