#-*- coding:utf-8 -*-

'''
Created on 2015年12月13日

@author: LeoBrilliant
'''

 
class Singleton2(type):
    def __init__(cls, name, bases, dict):
        super(Singleton2, cls).__init__(name, bases, dict)
        cls._instance = None    
    def __call__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = super(Singleton2, cls).__call__(*args, **kw)
        return cls._instance
     
class MyClass3(object):
    __metaclass__ = Singleton2
     

class C(object):
    def __init__(self, s):
        print s
myclass = C
type(C)
type(myclass) 

def make_class(class_name):
    class C(object):
        def print_class_name(self):
            print class_name
    C.__name__ = class_name
    return C
C1, C2 = map(make_class, ["C1", "C2"])
c1, c2 = C1(), C2()
c1.print_class_name()
c2.print_class_name()

MyClass = type("MyClass", (object,), {"my_attribute": 0,})
type(MyClass)
o = MyClass()
o.my_attribute

def myclass_init(self, my_attr):
    self.my_attribute = my_attr
MyClass = type("MyClass", (object,), {"my_attribute": 0, "__init__": myclass_init})
type(MyClass)
o = MyClass("Test")
o.my_attribute

def mymetaclass(name, parents, attributes):
    return "Hello"

class C1(object):
    __metaclass__ = mymetaclass   
    
print C1

def log_everything_metaclass(class_name, parents, attributes):
    print "Creating class", class_name
    myattributes = {}
    for name, attr in attributes.items():
        myattributes[name] = attr
        if hasattr(attr, '__call__'):
            #myattributes[name] = print("Hello __call__")
            pass
        
    return type(class_name, parents, myattributes)

class C2(object):
    __metaclass__ = log_everything_metaclass
    
    def __init__(self, x):
        self.x = x
        
    def print_x(self):
        print self.x
        
print "Starting object Ctreation"
c = C2("Test2")
c.print_x()

class my_metaclass(type):
    def __new__(cls, class_name, parents, attributes):
        print "- my_metaclass.__new__ - Creating class instance of type", cls
        return super(my_metaclass, cls).__new__(cls, 
                                                class_name, 
                                                parents,
                                                attributes)
        
    def __init__(self, class_name, parents, attributes):
        print "- my_metaclass.__init__ - Initializing the class instance", self
        super(my_metaclass, self).__init__(self)
        
    def __call__(self, *args, **kwargs):
        print "- my_metaclass.__call__ - Creating object of type ", self

def my_class_decorator(cls):
    print "- my_class_decorator - Chance to modify the class", cls
    return cls

@my_class_decorator
class C3(object):
    __metaclass__ = my_metaclass
    
    def __new__(cls):
        print "- C3.__new__ - Creating object."
        return super(C3, cls).__new__(cls)
    
    def __init__(self):
        print "- C.__init__ - Initializing object."

c = C3()
print c
    

one = MyClass3()
two = MyClass3()
     
print("Origin a")
#print one.a
#print two.a
 
two.a = 3
print ("Set two.a = 3")
print one.a
print two.a
 
print id(one)
print id(two)
 
print one == two
print one is two