#-*- coding:utf-8 -*-

'''
Created on 2015��11��22��

@author: LeoBrilliant
'''

import MySQLdb
import tushare as ts

#连接数据库，当前参数为地址、用户、密码（可控）、数据库
db = MySQLdb.connect(host="localhost", user="root", passwd="", db="Data", charset="utf8")

data = ts.get_stock_basics()

data.to_sql("t_stock_basics", db, flavor="mysql", if_exists="append")

# #获取操作游标
# cursor = db.cursor()
# 
# #执行SQL语句
# #插入一条记录
# table_name = "employee_2"
# #sql = "drop table if exists %s" % table_name
# sql = """insert into %s ( first_name,
#     last_name,
#     age,
#     sex, 
#     income) values ( 'Leo',
#     'Brilliant',
#     25,
#     'M',
#     10000)""" % table_name
#     
# sql = "insert into %s( first_name, \
#     last_name, age, sex, income) \
#     values('%s', '%s', '%d', '%c', '%d')" % \
#     (table_name, 'Mac', 'Mohan', 20, 'M', 2000)
# 
# try:
#     #执行SQL语句
#     ret = cursor.execute(sql)
#     #提交
#     db.commit()
# except:
#     #异常则回滚
#     db.rollback()
# 
# 
# print("Return value: %s " % ret)

#关闭连接
db.close()

print("Success")