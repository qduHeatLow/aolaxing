# 积分商城自动签到与完成任务

### 介绍 b站：糸梦
已从原作者代码更新至 20220519可用



任务网址：http://www.100bt.com/m/creditMall/?gameId=2#task        
自动化目标：  

已优化至自动完成多种任务

## 开始

前提需要：python3.5 + selenium

### 使用

python3.5
```bash

pip install selenium
```
### 配置

首次使用运行 'cookies.py'  
```
python cookies.py 
```
登录自己的账号
成功后会自动退出并在目录生成一个 cookies.txt 文件

还需一个适合自己的 chromedriver.exe  
[chromedriver下载](https://chromedriver.storage.googleapis.com/index.html)  
具体搭建请百度  

### 启动

获取cookies成功后
启动 'biantian.py'

```
python baitian.py
```

如需静默运行 请在 biantian.py 中的头信息处添加
```
chromeOptions.add_argument('--incognito') 
```
centos运行请添加
```
chromeOptions.add_argument('--incognito') 
chromeOptions.add_argument('--no-sandbox')
```
### 多用户版 未实现 仍是原作者的

运行 'cookies.py'            
获得用户的cookie        
添加后缀 0 1 2 3 按照数字顺序 有多个就加多少      
列如
```
cookies0.py
cookies1.py
```
> 注意一定要从 0 开始

修改 `duoyonghu.py` 内的 语句
```for s in range(6)```
()内的数字 为用户总数量

> 此脚本只在windows系统测试     linux\mac\centos 并未测试 但区别不大  



### 云服务器版
baitian_yun.py 用于部署到服务器

### 重要必看提示：
其他用户请将代码改为自己可用的在运行哦~

