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
sql = "drop table if exists %s" % table_name
cursor.execute(sql)

sql = """create table %s (
    first_name char(20) not null,
    last_name char(20),
    age int,
    sex char(1),
    income float)""" % table_name
    
#创建表
data =  cursor.execute(sql)

print("Database version: %s " % data)

#关闭连接
db.close()