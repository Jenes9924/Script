import requests
from bs4 import BeautifulSoup
def zongHengNovel(url):
    context = requests.get(url)
    html = BeautifulSoup(context.text, 'lxml')

    latest = html.find_all(name='div', attrs={'class': 'tit'})
    tag_a = latest[1].find(name='a',attrs={'target':'_blank'})
    print(tag_a.string)
    chaptername = tag_a.string
    return  chaptername



zongHengNovel( 'http://book.zongheng.com/book/672340.html')
zongHengNovel('http://book.zongheng.com/book/342974.html')
zongHengNovel('http://book.zongheng.com/book/95252.html')