#-*- coding:utf-8 -*-
'''
Created on 2015年12月12日

@author: le
'''

class Observer:
    def __init__(self, strname, strsub):
        self.name = strname
        self.sub = strsub
        
    def Update(self):
        pass 
    
    
class StockObserver(Observer):
    def Update(self):
        print("%s:%s, stop watching Stock and go on work!" % (self.name, self.sub.action))
        
class NBAObserver(Observer):
    def Update(self):
        print("%s:%s, stop watching NBA and go on work!" % (self.name, self.sub.action))
    
class SecretaryBase:
    def __init__(self):
        self.observers = []
    
    def Attach(self, new_observer):
        pass
    
    def Notify(self):
        pass
    
class Secretary(SecretaryBase):
    def Attach(self, new_observer):
        self.observers.append(new_observer)
        
    def Notify(self):
        for p in self.observers:
            p.Update()
            
if __name__ == "__main__":
    p = Secretary()
    s1 = StockObserver("xh", p)
    s2 = NBAObserver("wyt", p)
    p.Attach(s1)
    p.Attach(s2)
    p.action = "WARNING:BOSS"
    p.Notify()
    