# coding: UTF-8

'''
Created on 2016年9月2日

@author: user
'''

import random

def BubbleSort(elements):
    length = len(elements)
    
    i = 0; 
    j = length - 1;
    while j > 0:
        i = 0
        while i < j:
            if elements[i] > elements[i + 1]:
                tmp = elements[i]
                elements[i]= elements[i + 1]
                elements[i + 1] = tmp
            i = i + 1
        
        j = j - 1
        

if __name__ == '__main__':
    MAX = 10
    elements = [x for x in range(MAX)]
    
    print elements
    
    random.shuffle(elements)
    
    print elements
    
    BubbleSort(elements)
    
    print elements