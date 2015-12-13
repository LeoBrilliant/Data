#-*- coding:utf-8 -*-

'''
Created on 2015年12月13日

@author: LeoBrilliant
'''

#可迭代对象
#迭代器

class count_iterator(object):
    n = 0
    def __iter__(self):
        return self
    
    def next(self):
        y = self.n
        self.n += 1
        return y
    
class SimpleList(object):
    def __init__(self, *items):
        self.items = items
        self.index = 0
        self.maxindex = len(items)
    
#     def __getitem__(self, i):
#         return self.items[i]
    
    def __iter__(self):
        return self
    
    def next(self):
        if self.maxindex <= self.index :
            #return None
            raise StopIteration
        temp = self.items[self.index]
        self.index += 1
        return temp
        
    
if __name__ == "__main__":
    counter = count_iterator()
    print(next(counter))
    print(next(counter))
    print(next(counter))
    
    a = SimpleList(1, 2, 3)
    it = iter(a)
    print(next(it))
    print(next(it))
    
    for i in a:
        print i