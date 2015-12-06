#-*- coding:utf-8 -*-
'''
Created on 2015年11月29日

@author: LeoBrilliant
'''
import MySQLdb
import Logger.MyLogger as mlg

class MySQLConnection(object):
    '''
    classdocs
    '''
    
    __conn = None
    
    def __init__(self):
        '''
        Constructor
        '''
        __ip = 'localhost'
        __user = 'root'
        __pw = ''
        __schema = 'Data'
    
        self.__init_connections(ip=__ip, user=__user, pw=__pw, schema=__schema)
    
        mlg.MyLogger.getLogger().info("Initialize Connection Success")
        
    def __init_connections(self, ip='localhost', user='root', pw='', schema=''):
        MySQLConnection.__conn = MySQLdb.connect(host=ip, user=user, passwd=pw, db=schema, charset="utf8")
    
    @classmethod
    def GetConnection(cls):        
        return cls.__conn
    
    
    def ReleaseConnection(self, conn):
        pass