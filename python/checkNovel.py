import requests
from bs4 import BeautifulSoup

import smtplib
import email.mime.multipart
import email.mime.text
import pymysql
import re
import time


#返回5表示有多条记录
#返回4表示插入数据库错误
#返回3表示更新数据库错误
#返回2表示最新章节未更新
#返回0表示小说不存在或者数据库连接出错
def sqlSearch(chaptername, novelname):
    # 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
    conn = pymysql.connect(host='localhost', user='root', passwd='password', db='python_script', port=3306,
                           charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    try:

        #检查小说是否存在
        sta = cur.execute("SELECT count(*) FROM novel WHERE name='"+novelname+"'")
        data = cur.fetchall()
        exist=re.findall(r'\d+',str(data))
        exist=int(exist[0])
        if exist==0:
            cur.execute("INSERT INTO novel VALUES ('"+novelname+"','"+chaptername+"')")
            if sta != 1:
                return '4'
            conn.commit()
        elif exist==1:
            print('-----查询正常，返回一条记录')
            pass
        else:
            return '5'
        cur.execute("select newest from novel WHERE name='" + str(novelname) + "'")
        data = cur.fetchall()
        # for d in data :
        #     #注意int类型需要使用str函数转义
        #     print("ID: "+str(d[0])+'  用户名： '+d[1]+"  注册时间： "+d[2])

        sql_chaptername = str(str(data).split("'")[1]).strip()
        if sql_chaptername != chaptername:
            sta = cur.execute("update novel SET newest='" + str(chaptername) + "' WHERE name='" + str(novelname) + "'")
            if sta != 1:
                return '3' #返回3表示更新数据库错误
            conn.commit()
            return chaptername
        else:
            return '2'
    except  Exception:
         return '0'
    finally:
        cur.close()  # 关闭游标
        conn.close()  # 释放数据库资源

def resultJudge(result,novelname,chaptername):
    if result == '0':
        sendEmail('小说《' + novelname + '》数据库connect出错！请检查')
    elif result == '3':
        sendEmail('小说《' + novelname + '》数据库update出错！请检查')
    elif result == '2':
        print('----无更新')
        pass
    elif result == chaptername:
        sendEmail('小说《' + novelname + '》已更新至:' + chaptername)
    elif result == '4':
        sendEmail('小说《' + novelname + '》数据库insert into出错！请检查')
    elif result == '5':
        sendEmail('小说《' + novelname + '》数据库查询返回多条记录！请检查')
    else:
        sendEmail('小说《' + novelname + '》自动更新脚本返回未知状态,请检查')

#获取最新章节名
def zongHengNovel(url):
    context = requests.get(url)
    html = BeautifulSoup(context.text, 'lxml')

    latest = html.find_all(name='div', attrs={'class': 'tit'})
    tag_a = latest[1].find(name='a', attrs={'target': '_blank'})
    chaptername = tag_a.string
    return chaptername

#获取最新章节名
def qiDianNovel(url):
    context = requests.get(url)
    html = BeautifulSoup(context.text, 'lxml')
    p_tag = html.find(name='li', attrs={'class': 'update'})
    a_tag = p_tag.find(name='a', attrs={'class': 'blue'})
    return a_tag.text

def sendEmail2(emailname):
    """"""
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = 'r316097@163.com'
    msg['to'] = 'QQ号码@qq.com'
    msg['subject'] = emailname + "----来自爬虫"
    content = emailname
    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)
    smtp = smtplib
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login('r316097@163.com', 'qwe333')
    smtp.sendmail('r316097@163.com', 'QQ号码@qq.com', str(msg))
    smtp.quit()


def sendEmail(emailname):
    """"""
    '''uhixwpfjmfhvbehd'''
    '''rwcbyeqdnyecbeff'''
    '''rluqabbksnsabccc'''
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = 'QQ号码@qq.com'
    msg['to'] = 'QQ号码@qq.com'
    msg['subject'] = emailname + "----来自爬虫"
    content = emailname
    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)
    smtp = smtplib
    smtp = smtplib.SMTP_SSL()
    smtp.connect('smtp.qq.com')
    smtp.login('QQ号码@qq.com', 'rluqabbksnsabccc')
    smtp.sendmail('QQ号码@qq.com', 'QQ号码@qq.com', str(msg))
    smtp.quit()


# 新建纵横中文网任务
def startOne(url,novelname):
    print('《' + novelname + '》')
    chaptername = zongHengNovel(url)
    result = sqlSearch(chaptername, novelname)
    resultJudge(result, chaptername=chaptername, novelname=novelname)

#新建起点中文网任务
def startOneQiDian(url,name):
    print('《' + name + '》')
    chaptername = qiDianNovel(url)
    result = sqlSearch(chaptername, name)
    resultJudge(result, chaptername=chaptername, novelname=name)

'''http://book.zongheng.com/book/342974.html'''

print('任务开始：'+time.strftime("%Y-%m-%d %H:%M:%S"))
startOne( 'http://book.zongheng.com/book/672340.html','剑来')
startOne('''http://book.zongheng.com/book/342974.html''','永夜君王')
startOne('http://book.zongheng.com/book/95252.html','桃花')
startOneQiDian('https://book.qidian.com/info/1890269','大圣传')

print('任务结束：'+time.strftime("%Y-%m-%d %H:%M:%S"))