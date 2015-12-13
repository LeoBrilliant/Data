#-*- coding:utf-8 -*-

'''
Created on 2015年12月13日

@author: LeoBrilliant
'''

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
        return super(my_metaclass, self).__call__(*args, **kwargs)
    
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
        return super(C3, self).__init__(self)
        
    def __call__(self, *args, **kwargs):
        print "- C.__call__ - Creating object of type", self
        return super(C3, self).__call__(*args, **kwargs)

c = C3()
print c