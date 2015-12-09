#-*- coding:utf-8 -*-
'''
Created on 2015年11月29日

@author: LeoBrilliant
'''

import Logger.MyLogger as mlg
import DBAccess.MySQLdb.MySQLAccess as msql
import Loader.TuShare.TradingData.Test as t

if __name__ == '__main__':
    
    mylogger = mlg.MyLogger()
    mylogger.debug("Hello")
    
    ml = mlg.MyLogger.getLogger()  
    ml.debug("TEst")  
    mlg.MyLogger.getLogger().info("World")
    
    myconn = msql.MySQLConnection()
    
    test = t.HisTickDataTest("t_his_tick_data")

    #Here we are ss
    pass