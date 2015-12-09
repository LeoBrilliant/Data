#-*- coding:utf-8 -*-

'''
Created on 2015年11月29日

@author: LeoBrilliant
'''

#-*- coding:utf-8 -*-

'''
Created on 2015年11月25日

@author: LeoBrilliant

#获取大盘指数历史行情
'''
import DBAccess.MySQLdb.MySQLAccess as msql

import tushare as ts
from datetime import datetime

#连接数据库，当前参数为地址、用户、密码（可控）、数据库
#db = MySQLdb.connect("localhost", "root", "", "Data")
#db = MySQLdb.connect(host="localhost", user="root", passwd="", db="Data", charset="utf8")

db = msql.MySQLConnection.GetConnection()

tradingday = datetime.strftime(datetime.today(), "%Y-%m-%d")

code = '600848'

tradingday = '2015-11-27'

data = ts.get_tick_data(code=code, date=tradingday)

data['tradingday'] = tradingday

data['code'] = code

indexdata = data.set_index(['tradingday', 'code'])

#ret = indexdata.to_sql("t_his_tick_data", db, flavor="mysql", if_exists="append")

#关闭连接
db.close()

print("Success") 