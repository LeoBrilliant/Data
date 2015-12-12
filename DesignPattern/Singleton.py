#-*- coding:utf-8 -*-
'''
Created on 2015年12月12日

@author: le
'''

class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, "_instance"):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
            
        return cls._instance
    
class MyClass(Singleton):
    a = 1
    
one = MyClass()
two = MyClass()

print("Origin a")
print one.a
print two.a

two.a = 3
print ("Set two.a = 3")
print one.a
print two.a

print id(one)
print id(two)

print one == two
print one is two


class Borg(object):
    _state = {}
    def __new__(cls, *args, **kw):
        ob = super(Borg, cls).__new__(cls, *args, **kw)
        ob.__dict__ = cls._state
        return ob
    
class MyClass2(Borg):
    a = 1
    
one = MyClass2()
two = MyClass2()

print("Origin a")
print one.a
print two.a

two.a = 3
print ("Set two.a = 3")
print one.a
print two.a

print id(one)
print id(two)

print one == two
print one is two

print id(one.__dict__)
print id(two.__dict__)

# 
# class Singleton2(type):
#     def __init__(cls, name, bases, dict):
#         super(Singleton2, cls).__init__(name, bases, dict)
#         cls._instance = None
#     #@classmethod    
#     def __call__(cls, *args, **kw):
#         if cls._instance is None:
#             cls._instance = super(Singleton2, cls).__call__(*args, **kw)
#         return cls._instance
#     
# class MyClass3(object):
#     __metaclass__ = Singleton2
#     
# 
# one = MyClass3()
# two = MyClass3()
#     
# print("Origin a")
# print one.a
# print two.a
# 
# two.a = 3
# print ("Set two.a = 3")
# print one.a
# print two.a
# 
# print id(one)
# print id(two)
# 
# print one == two
# print one is two

def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
            
        return instances[cls]
    
    return _singleton

@singleton
class MyClass4(object):
    a = 1 
    def __init__(self, x = 0):
        self.x = x
        
one = MyClass4()
two = MyClass4()
    
print("Origin a")
print one.a
print two.a

two.a = 3
print ("Set two.a = 3")
print one.a
print two.a

print id(one)
print id(two)

print one == two
print one is two