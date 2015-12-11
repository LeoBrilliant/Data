#-*- coding:utf-8 -*-
'''
Created on 2015年12月11日

@author: le
'''

class LeiFeng:
    def Sweep(self):
        print("LeiFeng sweep")
        
class Student(LeiFeng):
    def Sweep(self):
        print("Student sweep")
        
class Volenteer(LeiFeng):
    def Sweep(self):
        print("Volenteer sweep")
        
class LeiFengFactory:
    def CreateLeiFeng(self):
        temp = LeiFeng()
        return temp

class StudentFactory(LeiFengFactory):
    def CreateLeiFeng(self):
        temp = Student()
        return temp

class VolenteerFactory(LeiFengFactory):
    def CreateLeiFeng(self):
        temp = Volenteer()
        return temp

if __name__ == "__main__":
    sf = StudentFactory()
    s = sf.CreateLeiFeng()
    
    s.Sweep()
    
    sdf = VolenteerFactory()
    sd = sdf.CreateLeiFeng()
    sd.Sweep()