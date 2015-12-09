#-*- coding:utf-8 -*-

'''
Created on 2015年12月6日

@author: LeoBrilliant
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_exe_dir = r'C:\Users\LeoBrilliant\AppData\Local\360Chrome\Chrome\Application\360chrome.exe'

chrome_op = Options()

chrome_op.binary_location = chrome_exe_dir

browser = webdriver.Chrome(chrome_options=chrome_op)

browser.get("http://www.baidu.com")

browser.maximize_window()

browser.get("http://www.youdao.com")

actions = ActionChains(browser)

actions.send_keys(Keys.CONTROL, 't').perform()

tab1 = browser.current_window_handle

tabs = browser.window_handles

tab2 = tabs[1]

browser.switch_to_window(tab2)

actions.send_keys(Keys.ESCAPE).perform()

browser.get("http://www.jd.com")

sleep(5.0001)

print( 'Success')

browser.close()

#some message