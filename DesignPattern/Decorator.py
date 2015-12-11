#-*- coding:utf-8 -*-
'''
Created on 2015年12月11日

@author: le
'''

class Person:
    def __init__(self, tname):
        self.name = tname
        
    def Show(self):
        print("dressed %s" % (self.name))
        
class Finery(Person):
    component = None
    
    def __init__(self):
        pass
    
    def Decorate(self, ct):
        self.component = ct
        
    def Show(self):
        if(self.component != None):
            self.component.Show()
            
class TShirts(Finery):
    def __init__(self):
        pass
    
    def Show(self):
        print("Big T-shirt")
        self.component.Show()
        
class BigTrouser(Finery):
    def __init__(self):
        pass
    
    def Show(self):
        print("Big Trouser")
        self.component.Show()
        
if __name__ == "__main__":
    p = Person("somebody")
    bt = BigTrouser()
    ts = TShirts()
    bt.Decorate(p)
    ts.Decorate(bt)
    
    ts.Show()