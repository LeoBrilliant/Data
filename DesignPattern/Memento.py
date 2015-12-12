#-*- coding:utf-8 -*-
'''
Created on 2015年12月12日

@author: le
'''

class Originator:
    def __init__(self):
        self.state = ""
        
    def Show(self):
        print(self.state)
        
    def CreateMemo(self):
        return Memo(self.state)
    
    def SetMemo(self, memo):
        self.state = memo.state
    
class Memo:
    state = ""
    def __init__(self, ts):
        self.state = ts
        
class Caretaker:
    memo = ""
    
if __name__ == "__main__":
    on = Originator()
    on.state = "on"
    on.Show()
    
    c = Caretaker()
    c.memo = on.CreateMemo()
    c.memo.state = "off"
    on.SetMemo(c.memo)
    on.Show()