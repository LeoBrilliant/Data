#-*- coding:utf-8 -*-

'''
Created on 2015年12月6日

@author: LeoBrilliant
'''

import unittest

class TestData(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_get(self):
        pass
    
    
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestData)
    unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()