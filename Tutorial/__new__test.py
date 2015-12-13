#-*- coding:utf-8 -*-

'''
Created on 2015年12月13日

@author: LeoBrilliant
'''


class inch(float):
    def __new__(cls, arg=0.0):
        print("This is __new__")
        return float.__new__(cls, arg * 0.254)
    
    
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton,cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
if __name__ == "__main__":        
    a = inch(1)  
    print a      