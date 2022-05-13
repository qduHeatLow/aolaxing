# -*- coding:utf-8 -*- 
from selenium import webdriver
import time
import json


Path = 'D:/python_tool/geckodriver.exe'
driver = webdriver.Firefox(executable_path=Path)  # 使用FireFox进行模拟点击，运行此段代码的时候，会启动firefox
driver.get('http://www.100bt.com/m/creditMall/?gameId=2#home')

time.sleep(1)

while True:
    if driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[1]/div[2]/span[1]').text == '登录有礼':
        pass
    else:
        break
   
with open('cookies2.txt','w') as f:
    # 将cookies保存为json格式
    f.write(json.dumps(driver.get_cookies()))

driver.close()