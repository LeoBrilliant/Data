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
#插入一条记录
table_name = "employee_2"
#sql = "drop table if exists %s" % table_name
sql = """insert into %s ( first_name,
    last_name,
    age,
    sex, 
    income) values ( 'Leo',
    'Brilliant',
    25,
    'M',
    10000)""" % table_name
    
sql = "insert into %s( first_name, \
    last_name, age, sex, income) \
    values('%s', '%s', '%d', '%c', '%d')" % \
    (table_name, 'Mac', 'Mohan', 20, 'M', 2000)

try:
    #执行SQL语句
    ret = cursor.execute(sql)
    #提交
    db.commit()
except:
    #异常则回滚
    db.rollback()


print("Return value: %s " % ret)

#关闭连接
db.close()