#-*- coding:utf-8 -*-
'''
Created on 2015年12月11日

@author: le
'''

class CashSuper:
    def AcceptCash(self, money):
        return 0
    
class CashNormal(CashSuper):
    def AcceptCash(self, money):
        return money
    
class CashRebate(CashSuper):
    discount = 0
    
    def __init__(self, ds):
        self.discount = ds
        
    def AcceptCash(self, money):
        return money * self.discount
    
class CashReturn(CashSuper):
    total = 0
    ret = 0
    def __init__(self, t, r):
        self.total = t
        self.ret = r
        
    def AcceptCash(self, money):
        if(money >= self.total):
            return money - self.ret
        else:
            return money
        
class CashContext:
    def __init__(self, csuper):
        self.cs = csuper
    def GetResult(self, money):
        return self.cs.AcceptCash(money)
    
if __name__ == "__main__":
    money = input("money:")
    strategy = {}
    strategy[1] = CashContext(CashNormal())
    strategy[2] = CashContext(CashRebate(0.8))
    strategy[3] = CashContext(CashReturn(300, 100))
    
    ctype = input("type: [1] for normal, [2] for 80% discount, [3] for 300 -100.")
    if ctype in strategy:
        cc = strategy[ctype]
    else:
        print("Undefined type. Use normal mode")
        cc = strategy[1]
        
    print("you will pay: %d" % (cc.GetResult(money)))
    
    