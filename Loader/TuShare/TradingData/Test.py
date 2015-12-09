#-*- coding:utf-8 -*-
'''
Created on 2015年11月29日

@author: LeoBrilliant
'''

import DBAccess.MySQLdb.MySQLAccess as msql
import Logger.MyLogger as mlg
import tushare as ts
from datetime import datetime
import Loader.TuShare.BaseDataLoader as bdl

class HisTickDataTest(bdl.BaseDataLoader):
    '''
    classdocs
    '''
    


    def __init__(self, tableName):
        '''
        Constructor
        '''
        bdl.BaseDataLoader.__init__(self, tableName)
        #self.db = msql.MySQLConnection.GetConnection()
        #self.ml = mlg.MyLogger.getLogger()
        #tradingday = datetime.strftime(datetime.today(), "%Y-%m-%d")
        
        code = '600848'
        
        tradingday = '2015-11-30'
        
        self.ml.info("Loading Data")
        data = ts.get_tick_data(code=code, date=tradingday)
        
        data['tradingday'] = tradingday
        
        data['code'] = code
        
        indexdata = data.set_index(['tradingday', 'code'])
        
        self.ml.info("Saving Data")
        indexdata.to_sql(self.tableName, self.db, flavor="mysql", if_exists="append")
        
        #关闭连接
        #db.close()
        
        self.ml.info("Saving Success") 