#-*- coding:utf-8 -*-

'''
Created on 2015年12月11日

@author: LeoBrilliant
'''

class TestPaper:
    def TestQuestion1(self):
        print("Test1: A. B. C. D.")
        print("%s" % self.Answer1())
        
    def TestQuestion2(self):
        print("Test2: A. B. C. D.")
        print("%s" % self.Answer2())
        
    def Answer1(self):
        return ""
    
    def Answer2(self):
        return ""
    
class TestPaperA(TestPaper):
    def Answer1(self):
        return "B"
    
    def Answer2(self):
        return "C"
    
class TestPaperB(TestPaper):
    def Answer1(self):
        return "D"
    
    def Answer2(self):
        return "D"
    
if __name__ == "__main__":
    s1 = TestPaperA()
    s2 = TestPaperB()
    
    print("Student 1")
    s1.TestQuestion1()
    s1.TestQuestion2()
    
    print("Student 2")
    s2.TestQuestion1()
    s2.TestQuestion2()