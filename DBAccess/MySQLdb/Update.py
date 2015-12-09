#-*- coding:utf-8 -*-

'''
Created on 2015年11月22日

@author: LeoBrilliant
'''
import MySQLdb

#连接数据库，当前参数为地址、用户、密码（可控）、数据库
db = MySQLdb.connect("localhost", "root", "", "test")

#获取操作游标
cursor = db.cursor()

#执行SQL语句
#如果存在就删除table
table_name = "employee_2"
sql = "update %s set age = age + 1 \
    where sex = '%c' " % (table_name, 'M')

try:
    ret = cursor.execute(sql)
    db.commit()
except:
    db.rollback()

print("Return value: %s " % ret)

#关闭连接
db.close()