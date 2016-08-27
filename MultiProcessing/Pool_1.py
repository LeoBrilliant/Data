#encoding: utf-8
# coding=UTF-8

#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2016年8月20日

@author: LeoBrilliant
'''

from multiprocessing import Pool

def f(x):
    return x * x


if __name__ == "__main__":
    p = Pool(5)
    print(p.map(f, [1, 2, 3]))
    print("中文测试")
