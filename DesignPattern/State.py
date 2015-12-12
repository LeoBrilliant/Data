#-*- coding:utf-8 -*-
'''
Created on 2015年12月12日

@author: le
'''

class State:
    def WriteProgram(self, w):
        pass
    
class Work:
    def __init__(self):
        self.hour = 9
        self.current = ForenoonState()
        
    def SetState(self, temp):
        self.current = temp
        
    def WriteProgram(self):
        self.current.WriteProgram(self)
        
class NoonState(State):
    def WriteProgram(self, w):
        print("Noon Working")
        if(w.hour < 13):
            print("Fun.")
        else:
            print("Need to rest.")
            
class ForenoonState(State):
    def WriteProgram(self, w):
        if(w.hour < 12):
            print("Morning Working")
            print("Energetic")
        else:
            w.SetState(NoonState())
            w.WriteProgram()
            
if __name__ == "__main__":
    mywork = Work()
    mywork.hour = 9
    mywork.WriteProgram()
    
    mywork.hour = 14
    mywork.WriteProgram()