#-*- coding:utf-8 -*-
'''
Created on 2015年11月29日

@author: LeoBrilliant
'''

import logging

class MyLogger(object):
    '''
    classdocs
    '''

    myLogger = None
    
    def __init__(self):
        '''
        Constructor
        '''
        logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='a')
        '''
         %(levelno)s: 打印日志级别的数值
         %(levelname)s: 打印日志级别名称
         %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
         %(filename)s: 打印当前执行程序名
         %(funcName)s: 打印日志的当前函数
         %(lineno)d: 打印日志的当前行号
         %(asctime)s: 打印日志的时间
         %(thread)d: 打印线程ID
         %(threadName)s: 打印线程名称
         %(process)d: 打印进程ID
         %(message)s: 打印日志信息
         '''
        #定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)
        
        MyLogger.myLogger = logging.getLogger('')
        self.info("MyLogger Initialized")
        
    def debug(self, message):
        self.myLogger.debug(message)
        
    
    def info(self, message):
        self.myLogger.info(message)
        
    def warning(self, message):
        self.myLogger.warning(message)
        
    def error(self, message):
        self.myLogger.error(message)
        
    def fatal(self, message):
        self.myLogger.fatal(message)
     
    @classmethod
    def getLogger(cls):
        
        return cls.myLogger