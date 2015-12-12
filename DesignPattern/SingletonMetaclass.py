#-*- coding:utf-8 -*-
'''
Created on 2015年12月12日

@author: le
'''
class Singleton(type):
    def __call__(cls, *args, **kwargs):
        print "Singleton call"
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instance
    def __new__(cls, name, bases, dct):
        print "Singleton new"
        return type.__new__(cls, name, bases, dct)
 
    def __init__(cls, name, bases, dct):
        print "Singleton init"
        super(Singleton, cls).__init__(name, bases, dct)
 
class Cache(object):
    __metaclass__ = Singleton
    def __new__(cls, *args, **kwargs):
        print "Cache new"
        return object.__new__(cls, *args, **kwargs)
    def __init__(cls, *args, **kwargs):
        print "Cache init"
    def __call__(cls, *args, **kwargs):
        print "Cache call"
 
print Cache()
print Cache()

c = Cache()
c.a = 1
print c.a
