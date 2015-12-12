#-*- coding:utf-8 -*-

'''
Created on 2015年12月10日

@author: LeoBrilliant
'''

from DBAccess.MySQLdb.MySQLAccess import MySQLConnection
import Logger.MyLogger as mlg
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(String(20), primary_key = True)
    name = Column(String(20))
    
    
if __name__ == '__main__':
    mylogger = mlg.MyLogger()
    
    msql = MySQLConnection()
    
    conn = msql.GetConnection()
    
    cursor = conn.cursor()
    
    
    #cursor.execute("create table user(id varchar(20) primary key, name varchar(20))")
#     mylogger.info("tabel user created")
#     
#     cursor.execute("insert into user(id, name) values (%s, %s)", ["1", "Michael"])
#     mylogger.info("insert %d record(s)" % cursor.rowcount)
#     
#     conn.commit()
    
    cursor.execute("select * from user where id = %s" , ["1"])
    
    values = cursor.fetchall()
    
    print(values)
    
    cursor.close()
    
    connstr = "mysql+mysqldb://root@localhost:3306/Data"
    engine = create_engine(connstr)
    
    DBSession = sessionmaker(bind=engine)
    
    session = DBSession()
    
    new_user = User(id="5", name="Bob")
    
    #session.add(new_user)
    
    session.commit()
    
    session.close()
    
    session = DBSession()
    
    user = session.query(User).filter(User.id == "5").one()
    
    print("type:", type(user))
    print("name:", user.name)
    
    session.close()