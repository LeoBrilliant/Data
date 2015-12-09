#-*- coding:utf-8 -*-

'''
Created on 2015年11月25日

@author: LeoBrilliant

#获取大盘指数历史行情
'''
import MySQLdb
import tushare as ts
from datetime import datetime

#连接数据库，当前参数为地址、用户、密码（可控）、数据库
#db = MySQLdb.connect("localhost", "root", "", "Data")
db = MySQLdb.connect(host="localhost", user="root", passwd="", db="Data", charset="utf8")

data = ts.get_index()

tradingday = datetime.strftime(datetime.today(), "%Y%m%d")

data['tradingday'] = tradingday
indexdata = data.set_index(['tradingday', 'code'])

ret = indexdata.to_sql("t_index_data", db, flavor="mysql", if_exists="append")

#关闭连接
db.close()

print("Success")