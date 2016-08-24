# coding: UTF-8

'''
Created on 2016��8��24��

@author: user
'''

import multiprocessing
import time
import random
import sys


def calculate(func, args):
    result = func(*args)
    return "%s says that %s%s = %s" % (
        multiprocessing.current_process().name,
        func.__name__, args, result)
    

def calculatestar(args):
    return calculate(*args)

def mul(a, b):
    time.sleep(0.5 * random.random())
    return a * b

def plus(a, b):
    time.sleep(0.5 * random.random())
    return a + b

def f(x):
    return 1.0 / (x - 5.0)

def pow3(x):
    return x ** 3

def noop(x):
    pass


def test():
    print("cpu_count() = %d\n" % multiprocessing.cpu_count())
    
    PROCESSES = 4
    
    print("Creating pool with %d processes\n" % PROCESSES)
    pool = multiprocessing.Pool(PROCESSES)
    print("pool = %s" % pool)
    print
    
    
if __name__ == "__main__":
    multiprocessing.freeze_support()
    
    assert len(sys.argv) in (1, 2)
    
    if len(sys.argv) == 1 or sys.argv[1] == "processes":
        print("Using processes ".center(79, "-"))
        
    elif sys.argv[1] == "threads":
        print("Using threads ".center(79, "_"))
    else:
        print("Usage:\n\t%s [processes | threads]" % sys.argv[0])
        raise SystemExit(2)
    
    test()
        