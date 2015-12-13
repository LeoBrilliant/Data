#-*- coding:utf-8 -*-

'''
Created on 2015年12月13日

@author: LeoBrilliant
'''

def fib():
    first, second = 0, 1
    while True:
        yield second
        first, second = second, first + second
    
    
if __name__ == "__main__":
    for i in fib():
        print i 
        if i > 10000000:
            break