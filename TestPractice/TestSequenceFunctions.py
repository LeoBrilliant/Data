#-*- coding:utf-8 -*-

'''
Created on 2015年12月6日

@author: LeoBrilliant
'''
import unittest
import random

class Test(unittest.TestCase):
    
    def setUp(self):
        self.seq = range(10)
        
    def testshuffle(self):
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))
        self.assertRaises(TypeError, random.shuffle,(1,2,3))
        
    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)
        
    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
            
        for element in random.sample(self.seq, 5):
            self.assertTrue( element in self.seq)
        

    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    ret = unittest.main()
    
    print ret