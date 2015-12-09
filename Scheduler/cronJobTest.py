#-*- coding:utf-8 -*-

'''
Created on 2015年12月5日

@author: LeoBrilliant
'''

from apscheduler.schedulers.background import BackgroundScheduler 
from time import sleep

i = 0
def RoundWork():
    i += 1
    print("i = %d" % i)
     
sched = BackgroundScheduler()

job = sched.add_job(RoundWork, 'interval',  seconds=2, id='my_job_id')

sched.print_jobs()

sched.start()

sleep(10)

sched.shutdown()
