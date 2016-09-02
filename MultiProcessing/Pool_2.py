# coding=UTF-8

'''
Created on 2016年8月20日

@author: LeoBrilliant
'''

from multiprocessing import Process
import os

def info(title):
    print(title)
    print("module name %s" % __name__)
    if(hasattr(os, 'getppid')):
        print("parent process: %d" % os.getppid())
    print("process id: %d" % os.getpid())
    
def f(name):
    info("function f")
    print("hello %s" % name)
    
if __name__ == "__main__":
    info("main line")
    p = Process(target = f, args = ("bob", ))
    p.start()
    p.join()
    
    