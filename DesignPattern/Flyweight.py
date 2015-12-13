#-*- coding:utf-8 -*-

'''
Created on 2015年12月12日

@author: LeoBrilliant
'''

import sys

class WebSite:
    def Use(self):
        pass
    
class ConcreteWebSite(WebSite):
    def __init__(self, strName):
        self.name = strName
        
    def Use(self, user):
        print("Website type: %s, user: %s" %(self.name, user))

class UnShareWebSite(WebSite):
    def __init__(self, strName):
        self.name = strName
    def Use(self, user):
        print("UnShare Website type: %s, user: %s" % (self.name, user))        

class WebFactory:
    def __init__(self):
        test = ConcreteWebSite("test")
        self.webtype = {"test": test}
        self.count = {"test": 0}
        
    def GetWeb(self, webtype):
        if webtype not in self.webtype:
            temp = ConcreteWebSite(webtype)
            self.webtype[webtype] = temp
            self.count[webtype] = 1
        else:
            temp = self.webtype[webtype]
            self.count[webtype] = self.count[webtype] + 1
            
        return temp
    
    def GetCount(self):
        for key in self.webtype:
            print("type: %s, count:%d " %(key, self.count[key]))
            
if __name__ == "__main__":
    f = WebFactory()
    ws = f.GetWeb("blog")
    ws.Use("Lee")
    ws2 = f.GetWeb("show")
    ws2.Use("Jack")
    ws3 = f.GetWeb("blog")
    ws3.Use("Chen")
    ws4 = UnShareWebSite("TEST")
    ws4.Use("Mr.Q")
    
    print(f.webtype)
    f.GetCount()
        