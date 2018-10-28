import requests
from bs4 import BeautifulSoup
import threading
import  time
from selenium import webdriver


driver_path='/home/alex/PycharmProjects/chromedriver'

count=0
index_url="http://qun.qzone.qq.com"
#options=webdriver.ChromeOptions
#options.add_argument('--headless')
#options.binary_location="/opt/google/chrome/google-chrome"
browser=webdriver.Chrome(driver_path)
browser.get(index_url)

while browser.current_url==index_url:
    if count>10:
        print('ERROR:页面超时，退出')
        exit(1)
    time.sleep(5)
    print('INFO: 等待扫描二维码')
    count=count+1

if browser.current_url!=index_url:
    time.sleep(3)
    print('INFO: 直接url跳转群空间')

browser.get('http://qun.qzone.qq.com/group#!/302765357/home')











