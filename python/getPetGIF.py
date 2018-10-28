import requests
from bs4 import BeautifulSoup
import selenium.webdriver
from selenium.webdriver.chrome import options
import uuid
import json
import time as thread

def getImage(image_url,path):
    image_context=requests.get(image_url,timeout=15)
    fileName=str(uuid.uuid1())
    file_path=path+str(fileName)+'.'+str(image_url).split('.')[-1]
    file=open(file_path,'wb')
    file.write(image_context.content)
    file.close()
    print('已下载图片:'+str(image_url))
    print('')

web_url='https://www.duitang.com/album/?id=81893281&spm=2014.12553688.202.0#!albumpics'
ajax_url='https://www.duitang.com/napi/blog/list/by_album/'

path='/home/alex/PycharmProjects/untitled/图片/'
album_id=web_url.split('id=')[1].split('&')[0]
limit=24
include_fields='top_comments,is_root,source_link,buyable,root_id,status,like_count,sender,reply_count'
index=1

start=24

time=''

options=selenium.webdriver.ChromeOptions()

'''无头模式'''
#options.add_argument('--headless')

browser=selenium.webdriver.Chrome('/home/alex/PycharmProjects/driver/chromedriver',chrome_options=options)
browser.get(web_url)
time=browser.execute_script('return Date.parse(new Date())')
print('time='+str(time))

browser.close()


first_result=requests.get(ajax_url+'?album_id='+album_id+'&limit='+str(limit)+'&include_fields='+str(include_fields)+'&start='+str(limit*index)+'&_='+str(time))

print(first_result.text)
print('----------------------')
result=json.loads(first_result.text)

total=int(result['data']['total'])

count=(total-total%limit)/limit+1
print('count='+str(count))
img=[]
for i in range(int(count)):
    html=requests.get(ajax_url+'?album_id='+album_id+'&limit='+str(limit)+'&include_fields='+str(include_fields)+'&start='+str(start)+'&_='+str(time))
    json_text=json.loads(html.text)
    if int(json_text['status'])!=1:
        print('返回状态错误！！！！！！！！！')
        thread.sleep(5000)
        continue
    img_list=json_text['data']['object_list']
    print('len(imgh_list)='+str(len(img_list)))
    for j in range(len(img_list)):
        img.append(img_list[j]['photo']['path'])
        print(img_list[j]['photo']['path'])

    start=json_text['data']['next_start']
    time=int(time)+1


for image_url in img:
    getImage(image_url,path)













