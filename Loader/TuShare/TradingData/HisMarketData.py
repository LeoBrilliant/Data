#-*- coding:utf-8 -*-

'''
Created on 2015年11月22日

@author: LeoBrilliant
'''

import MySQLdb
import tushare as ts
import datetime as datetime

#连接数据库，当前参数为地址、用户、密码（可控）、数据库
db = MySQLdb.connect(host="localhost", user="root", passwd="", db="Data", charset="utf8")

code = "000001"

begindate = "19900101"

data = ts.get_h_data(code=code, start=begindate, autype=None)

data['code'] = code

indexdata = data.set_index(['code'], append=True)

indexdata.to_sql("t_his_market_data", db, flavor="mysql", if_exists="append")


#关闭连接
db.close()

print("Success")