#!将从chrome浏览器复制的headers格式化成标准dict

import os


path='D:\\jsonTemp.txt'
file=open(path,'r')
while True:
    line=file.readline()
    if not  line:
        break
    #遇到多个分号时以第一个分号为准
    if line.count(':')>1:
        # print(line)
        # print('此行具有多个分号，无法格式化')
        # break
        index=line.index(':')
        new_line2="'"+str(line)[0:index]+"':'"+str(str(line)[index+1:len(line)]).strip()+"',"
        print(new_line2)
        #print('test')
        continue
    if line.find(':')!=-1:
        words=line.split(':')
        new_line="'"+str(words[0]).strip()+"':'"+str(words[1]).strip()+"',"
        print(new_line)
    else:
        print(line)