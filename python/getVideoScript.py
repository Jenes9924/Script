import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from  selenium.webdriver.chrome.options  import Options
import time

result_map={}
driver_path='G:\\chromedriver_win32\\chromedriver.exe'
options=Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
options.binary_location="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
browser=webdriver.Chrome(driver_path,chrome_options=options)

def getPageScore(video_name):
    url = 'https://movie.douban.com/subject_search?search_text=' + video_name + '&cat=1002'
    browser.get(url)
    details = browser.find_elements_by_class_name('detail')
    count = 0
    time.sleep(3)
    for detail in details:
        # 此处如果使用find_element_by_class_name 容易出错
        title = detail.find_elements_by_class_name('title')
        if len(title)== 0 :
            print('没有获取到标题！')
            break
        if len(title)>1:
            print("====ERROR:   错误，获取多个标题"+str(len(title)))
            print(video_name)
            print('=====')
            break
        title = title[0]
        test = detail.find_element_by_class_name('abstract')
        if title.text.find(video_name) != -1 and test.text.find('分钟')!=-1:
            if count == 1:
                print('=====ERROR:   错误，豆瓣电影名称重复，需要手动查找')
                break
            try:
                score = detail.find_element_by_class_name('rating_nums')
            except:
                print('暂无评分！')
                return
            print(title.text)
            print(score.text)
            result_map[title.text]=score.text


def getNewestFilmName():
    all_video_names=[]
    url='http://www.dytt8.net/'
    target_url=''

    html_text=requests.get(url)
    charset_code=html_text.text.split('charset=')[1]
    if not charset_code:
        print('====ERROR:   无法获取网页编码！')
        exit(0)
    charset_code=charset_code.split('"')[0]
    html_text.encoding=charset_code
    html = BeautifulSoup(html_text.text,"lxml")
    elements=html.find_all('div',{'class':'co_content8'})
    for element in elements:
        first_a = element.find('a')
        if str(first_a).find('最新电影下载') == -1 and str(first_a).find('迅雷电影资源') == -1:
            continue
        else:
            all_a_tag = element.find_all('a')
            for a in all_a_tag:
                video_name = a.string.split('》')[0].split('《')
                if len(video_name)!=2:
                    continue
                else:
                    video_name=video_name[1]
                    all_video_names.append(video_name)

    return  all_video_names


def start(all_video_names):
    if len(all_video_names) <1:
        print('====ERROR:   参数错误，请检查！')
        exit(1)
    for name in all_video_names:
        getPageScore(name)
    browser.close()


all_video_names = getNewestFilmName()
start(all_video_names)

result = sorted(result_map.items(),key=lambda x:x[1])

for video in result:
    print(video)
    print('\n')