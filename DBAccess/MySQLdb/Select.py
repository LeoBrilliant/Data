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

#执行查询
#查询数据库版本
cursor.execute("select version()")

#获取一条记录
data =  cursor.fetchone()

print("Database version: %s " % data)

table_name = "employee_2"
#不要轻易给表名加修饰
#字符串自动转换成整数
sql = "select * from %s \
    where income < '%d'" % (table_name, 10000)

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print("fname=%s, lname=%s, age=%d, sex=%s, income=%.2f" % (fname, lname, age, sex, income))

except:
    print("Error: unable to fetch data")
            
#关闭连接
db.close()
