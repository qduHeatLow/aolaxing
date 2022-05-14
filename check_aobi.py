from selenium import webdriver
import time
import json

#头信息
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import smtplib
# 发送字符串的邮件
from email.mime.text import MIMEText
# 需要 MIMEMultipart 类
from email.mime.multipart import MIMEMultipart


options = Options()
options.add_argument('--incognito')
options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36"')

Path = 'D:/python_tool/geckodriver.exe'
aola = webdriver.Firefox(options=options, executable_path=Path)
#进入网页+登录
aola.get('http://www.100bt.com/m/creditMall/?gameId=2#home')




def sendmail(to,subject,contents):
    # 设置服务器所需信息
    fromEmailAddr = '1442984671@qq.com'  # 邮件发送方邮箱地址
    password = 'bdrkmmoarksphefc'  # (注意不是邮箱密码，而是为授权码)
    toEmailAddrs = [to]  # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发

    # 设置email信息
    # ---------------------------发送带附件邮件-----------------------------
    # 邮件内容设置
    message = MIMEMultipart()
    # 邮件主题
    message['Subject'] = subject
    # 发送方信息
    message['From'] = fromEmailAddr
    # 接受方信息
    message['To'] = toEmailAddrs[0]
    # 邮件正文内容
    message.attach(MIMEText(contents, 'plain', 'utf-8'))
    # 登录并发送邮件
    try:
        server = smtplib.SMTP('smtp.qq.com')  # qq邮箱服务器地址，端口默认为25
        server.login(fromEmailAddr, password)
        server.sendmail(fromEmailAddr, toEmailAddrs, message.as_string())
        server.quit()
    except smtplib.SMTPException as e:
        print("error:", e)


aola.refresh()
time.sleep(0.3)
aola.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(1)
aola.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(1)
_30aobi = aola.find_element_by_xpath("/html/body/div[1]/div[1]/div[4]/div/div[2]/div/div[29]/div[1]/div[2]").text
print(_30aobi)
if _30aobi == "库存:0":
    pass
else:
    sendmail("1442984671@qq.com","库存补充","30奥币已补充")