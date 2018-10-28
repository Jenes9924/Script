'''
用来统计QQ群有多少成员，多少妹子爆照的一个简单脚本
多功能合一
包括下载空间相册
获取所有群成员
'''
import json
import requests
import uuid
import time
from functools import cmp_to_key
import  os
import random


class Man:
    remark = ''
    qqNumber = ''

    def __init__(self, a_remark, a_qqNumber):
        self.remark = a_remark
        self.qqNumber = a_qqNumber

    def __str__(self):
        return '{remark=' + str(self.remark) + ',qqNumber=' + str(self.qqNumber) + '}'

class User:
    nick=''
    qqNumber=''

    def __str__(self):
        return '{nick='+str(self.nick)+',qqNumber='+str(self.qqNumber)+'}'


class AlbumInfo:
    images = []
    image_num = 0
    date = ''
    msg = ""
    like_total=''
    nick = ''
    qqNumber = ''

    def __init__(self, image_num, date, nick, qqNumber, msg,like_total):
        self.image_num = image_num
        self.date = date
        self.nick = nick
        self.qqNumber = qqNumber
        self.msg = msg
        self.like_total=like_total
        self.images = []
        #print(type())

    def add_url(self,imageUrl):
        self.images.append(imageUrl)

    # def __cmp__(self, other):
    #     return (self, other)

    # def __str__(self):
    #     return  '{'+ 'image_num =' +str(self.image_num)+',date = '+str(self.date)+',user = '+str(self.user)+',msg = '+str(self.msg)+',like_total='+self.like_total+'}'


    def __cmp__(self, other):
        if self.like_total < other.like_total:
            return -1
        if self.like_total == other.like_total:
            return 0
        else:
            return 1


def cmp(a1,a2):
    if a1< a2:
        return -1
    if a1== a2:
        return 0
    else:
        return 1

def getImage(image_url, path,qqNumber,count,like_total):
    image_context = requests.get(image_url, timeout=15)
    # path=path+'/'+str(qqNumber)
    # if not os.path.exists(path):
    #     os.mkdir(path)
    # 默认jpg格式，如有需要可自定义
    fileName = str(like_total)+"-"+str(qqNumber)+'第'+str(count)+'张.jpg'
    file_path = path + str(fileName)
    file = open(file_path, 'wb')
    file.write(image_context.content)
    file.close()

    # print('已下载图片:' + str(image_url))
    print('')


def dealNickName():
    file_json = open('qun-member.json', 'r')
    json_data = json.load(file_json)['data']

    total = json_data['total']
    print('共计' + str(total) + '人')
    # 存放所有mm对象的集合
    all_mm = []
    all_other = []

    # 上海mm计数
    count_mm_SH = 0
    # 外地mm计数
    count_mm_out = 0
    # gg计数
    count_gg = 0
    # 非正常man计数
    count_other = 0

    count_gg_out = 0
    count_gg_SH = 0
    all_user = json_data['user']

    for user in all_user:
        man = Man(str(user['qun_remark']), str(user['uin']))

        remark = man.remark
        # print(remark)
        qqNumber = man.qqNumber
        if str(remark).find('MM') != -1 or remark.find('mm') != -1 or remark.find('女') != -1:
            if str(remark).find('上海') != -1:
                all_mm.append(man)
                count_mm_SH = count_mm_SH + 1
            elif remark.find('魔都') != -1:
                all_mm.append(man)
                count_mm_SH = count_mm_SH + 1
            elif remark.find('盐城') != -1:
                count_mm_out = count_mm_out + 1
                print(man)
            else:
                count_mm_out = count_mm_out + 1
                pass
        elif remark.find('GG') != -1 or remark.find('gg') != -1:
            count_gg = count_gg + 1
            if str(remark).find('上海') != -1:
                # all_mm.append(man)
                count_gg_SH = count_gg_SH + 1
            elif remark.find('魔都') != -1:
                # all_mm.append(man)
                count_gg_SH = count_gg_SH + 1
            else:
                count_gg_out = count_gg_out + 1
                pass
        else:
            count_other = count_other + 1
            all_other.append(man)

    print('上海共有' + str(count_mm_SH) + '人')
    print('外地共有' + str(count_mm_out) + '人')
    print('男性共有' + str(count_gg) + '人')
    print('上海男性共有' + str(count_gg_SH) + '人')
    print('外地男性共有' + str(count_gg_out) + '人')
    print('非正常共有' + str(count_other) + '人')
    # for man in all_mm:
    #     print(man)
    #
    # print('========================================================================')
    #
    # for man in all_other:
    #     print(man)


def dealAlbum():
    path = './image/'
    if not os.path.exists(path):
        os.mkdir(path)

    file = open('QQAlbum.json', 'r',encoding='utf-8')
    str_json = file.read();
    file.close()

    json_data = eval(str_json)
    count = 1
    #存放所有相册信息
    all_album=[]
    for data in json_data:
        feeds=data['data']['feeds']

        for info in feeds:
            #格式化时间戳
            timeArray = time.localtime(int(info['time']))
            otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            #获取相册主人
            user=info['user']

            #昵称
            nick=user['nick']
            #print('nick=' + str(nick))
            #号码
            qqNumber=user['uin']
            #相册文本内容
            msg=info['msg']['fdesc']
            #相册照片数量
            images_num=info['msg']['photo_num']
            #点赞人数
            like_total=int(info['like_total'])
            if info['like_total'] =='':
                print('=================================')
            #print('like_total='+str(like_total))
            album=AlbumInfo( images_num, otherStyleTime, nick, qqNumber, msg,like_total)

            images=info['msg']['pics']
            for image in images:
                album.add_url(image['url'])
            all_album.append(album)




        #print(data)
        count = count + 1
        # if count > 3:
        #     break
        #     all_album=[]
        #     continue

    print("共有"+str(count)+"组")
    #排序
    all_album = sorted(all_album,key=cmp_to_key(lambda x,y: int(x.like_total)-int(y.like_total)))
    all_img_count = 0
    count=0
    # print("all_album的数量为    ：      "+str(len(all_album)))
    for album in all_album:
        print(str(album.nick)+' :   '+str(album.qqNumber)+' ，点赞数：'+str(album.like_total))
        img_count=0
        count=count+1
        # print("album.images的数量为        ：      " + str(len(album.images)))
        for img_url in album.images:
            img_count=img_count+1
            all_img_count = all_img_count+1
            # if all_img_count < 1278 :
            #     continue
            getImage(img_url,path,album.qqNumber,img_count,album.like_total)
            time.sleep(0.3)
            print('下载'+str(all_img_count)+'张图片')

    print("共有"+str(count)+"人爆照")

dealAlbum()
