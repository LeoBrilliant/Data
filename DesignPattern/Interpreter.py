#-*- coding:utf-8 -*-

'''
Created on 2015年12月12日

@author: LeoBrilliant
'''

class Context:
    def __init__(self):
        self.input = ""
        self.output = ""
        
class AbstractExpression:
    def Interprete(self, context):
        pass
    
class Expresstion(AbstractExpression):
    def Interprete(self, context):
        print("terminal interpete")
        
class NonTerminalExpression(AbstractExpression):
    def Interprete(self, context):
        print("NonTerminal interprete")
        
if __name__ == "__main__":
    context = ""
    c = []
    c = c + [Expresstion()]
    c = c + [NonTerminalExpression()]
    c = c + [Expresstion()]
    c = c + [Expresstion()]
    
    for a in c:
        a.Interprete(context)