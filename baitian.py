# -*- coding:utf-8 -*- 
#引入selenium package, 建立webdriver对象
from os import close
from telnetlib import EC

from selenium import webdriver
import time
import json

#头信息
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.add_argument('--incognito')
options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36"')

Path = 'D:/python_tool/geckodriver.exe'
aola = webdriver.Firefox(options=options, executable_path=Path)
#进入网页+登录
aola.get('http://www.100bt.com/m/creditMall/?gameId=2#task')



def mission():
    aola.refresh()
    time.sleep(0.3)
    aola.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(0.3)

    # 开始任务
    # 每日签到
    # try:
    #     # print(1)
    #     aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div/div[2]/div[1]/div[3]').click()
    #     time.sleep(0.5)
    #     aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[5]/div[2]/div[7]/div').click()
    # except:
    #     pass
    # time.sleep(1)
    # 答题
    # 从上至下依次点击
    try:
        elements = aola.find_elements_by_xpath('//*[@id="app"]/div[1]/div[3]/div/div[2]/*/div[3]')
        length = int(len(elements))
        print(length)
        cnt = 0

        for element in elements:
            aola.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            if element.text == "已完成":
                print("已完成!")
                cnt = cnt + 1
                continue
            elif element.text == "去完成":
                element.click()
                if cnt == 0:
                    time.sleep(2)
                    print('success 1')
                elif cnt == length - 1:
                    time.sleep(5)
                    print('success 2')
                    aola.get('http://www.100bt.com/m/creditMall/?gameId=2#task')
                else:
                    # 等待取消按钮出现
                    WebDriverWait(aola, 60).until(
                        lambda the_driver: the_driver.find_element_by_xpath(
                            '/html/body/div[1]/div[1]/div[16]/div[2]/div[8]/div').is_displayed(), '失败')
                    time.sleep(35)
                    print('success 3')
                    aola.find_element_by_xpath('/html/body/div[1]/div[1]/div[16]/div[2]/div[8]/div').click()
                cnt = cnt + 1
            time.sleep(2)
        print("结束")
    except Exception as e:
        print(e)

# aola.delete_all_cookies()
# with open('cookies.txt','r') as f:
#     cookies_list = json.load(f)
#     for cookie in cookies_list:
#         aola.add_cookie(cookie)
#     mission()
#     aola.quit

aola.delete_all_cookies()
with open('cookies2.txt','r') as f:
    cookies_list = json.load(f)
    for cookie in cookies_list:
        aola.add_cookie(cookie)
    mission()
    aola.quit




# zhanghao_text = aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[1]/div[2]/span[1]').text
# jifen_text = aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[1]/div[2]/span[2]').text



# print(zhanghao_text)
# print(jifen_text)