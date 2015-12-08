#-*- coding:utf-8 -*-
'''
Created on 2015年11月30日

@author: LeoBrilliant
'''

import DBAccess.MySQLdb.MySQLAccess as msql
import Logger.MyLogger as mlg

class BaseDataLoader(object):
    '''
    classdocs
    '''


    def __init__(self, tableName):
        '''
        Constructor
        '''
        self.tableName = tableName
        self.db = msql.MySQLConnection.GetConnection()
        self.ml = mlg.MyLogger.getLogger()
        self.data = None
        self.ml.info("BaseDataLoader Initialized: " + self.tableName)
        pass
    
    def CheckCurrentData(self):
        
        pass
    
    def GetDataFrame(self):
        
        pass
    
    def SaveDataFrame(self):
        
        pass    