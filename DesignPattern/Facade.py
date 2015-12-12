#-*- coding:utf-8 -*-

'''
Created on 2015年12月11日

@author: LeoBrilliant
'''

class SubSystemOne:
    def MethodOne(self):
        print("SubSystemOne")
        
class SubSystemTwo:
    def MethodTwo(self):
        print("SubSystemTwo")
        
class SubSystemThree:
    def MethodThree(self):
        print("SubSystemThree")
        
        
class SubSystemFour:
    def MethodFour(self):
        print("SubSystemFour")
        
class Facade:
    def __init__(self):
        self.one = SubSystemOne()
        self.two = SubSystemTwo()
        self.three = SubSystemThree()
        self.four = SubSystemFour()
        
    def MethodA(self):
        print("MethodA")
        self.one.MethodOne()
        self.two.MethodTwo()
        self.four.MethodFour()
        
    def MethodB(self):
        print("MethodB")
        self.two.MethodTwo()
        self.three.MethodThree()
        
if __name__ == "__main__":
    facade = Facade()
    facade.MethodA()
    facade.MethodB()
    