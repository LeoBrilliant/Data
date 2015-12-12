#-*- coding:utf-8 -*-
'''
Created on 2015年12月12日

@author: le
'''

class Person:
    def CreateHead(self):
        pass 
    
    def CreateHand(self):
        pass
    
    def CreatefBody(self):
        pass
    
    def CreateFoot(self):
        pass
    
class ThinPerson(Person):
    def CreateHead(self):
        print("Thin Head")
        
    def CreateHand(self):
        print("Thin Hand")
        
    def CreateBody(self):
        print("Thin Body")
        
    def CreateFoot(self):
        print("Thin Foot")
        
class ThickPerson(Person):
    def CreateHead(self):
        print("Thick Head")
        
    def CreateHand(self):
        print("Thick Hand")
        
    def CreateBody(self):
        print("Thick Body")
        
    def CreateFoot(self):
        print("Thick Foot")
        
class Director:
    def __init__(self, temp):
        self.p = temp
    
    def Create(self):
        self.p.CreateHead()
        self.p.CreateBody()
        self.p.CreateHand()
        self.p.CreateFoot()
        
if __name__ == "__main__":
    p = ThickPerson()
    d = Director(p)
    d.Create()
    
    
        
