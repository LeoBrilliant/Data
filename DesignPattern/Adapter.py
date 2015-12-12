#-*- coding:utf-8 -*-
'''
Created on 2015年12月12日

@author: le
'''

class Target:
    def Request(self):
        print("Common Request")
        
class Adaptee(Target):
    def SpecificRequest(self):
        print("Specific Request")
        
class Adapter(Target):
    def __init__(self, ada):
        self.adaptee = ada
        
    def Request(self):
        self.adaptee.SpecificRequest()
        
if __name__ == "__main__":
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    adapter.Request()
        
