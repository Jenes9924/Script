import requests
from bs4 import BeautifulSoup
import json


#'clinicType'集合
clinicType_list=set([])

cookie='_sid_=151149634025420178067161; _e_m=1511496340265; _fp_code_=11e7c1175a00b569312793faffcb0e05; _ipgeo=province%3A%E4%B8%8A%E6%B5%B7%7Ccity%3A%E4%B8%8D%E9%99%90; mlc=2%26todayask_doctor%2Cdoctor_select%2Cdoctor%26%7B%22doctor_id%22%3A%2204108a62-a02b-40c2-87f9-87683ed91817000%22%7D; searchHistory=%E5%BC%A0%E5%8A%B2%E6%9D%BE%2C%7C%E9%BB%84%E7%BB%A7%E5%BF%A0%2C%7C%E4%B8%8A%E6%B5%B7%E7%B2%BE%E7%A5%9E%E5%8D%AB%E7%94%9F%E4%B8%AD%E5%BF%83%E5%92%A8%E8%AF%A2%2C%7C%E7%B2%BE%E7%A5%9E%E5%8D%AB%E7%94%9F%E7%A0%94%E7%A9%B6%E4%B8%AD%E5%BF%83%2C%7C%E4%B8%8A%E6%B5%B7%E7%B2%BE%E7%A5%9E%E5%8D%AB%E7%94%9F%E7%A0%94%E7%A9%B6%E4%B8%AD%E5%BF%83%2C%7C%E6%96%B0%E5%8D%8E%E5%8C%BB%E9%99%A2%20%E5%BC%A0%E5%8A%B2%E6%9D%BE%2C%7C%2Cclear; Hm_lvt_66fcb71a7f1d7ae4ae082580ac03c957=1513922230,1514282832,1514282868; _sh_ssid_=1514287424447; monitor_sid=4; mst=1514287425008; JSESSIONID=1mcxdd7g7qzyw1ryo8nlxounuh; __wyt__=!PvQ8jE97Dr0vM_O0ggjPhN5le07RihAdHMp1HDTXkicIxccaEFuA1X0jubc8AEERAI_Ga0jzy83mvb32YPzEDGj7Xj9PX8mY7x-JWc_Tk1RwlXUMJG-6ChkCHOE2AKqRBS82DeUG0V15lJBn14R1wxxDF5hJM2ZMtkaXcTiZfsKOE; _ci_=slWmbNgmyeT/IiGDA7+7G9lCxA3QBKz9mzd+oQ88XYj8LHVkvqXo8AH45fJfxWSj; __i__=2Dg1z1h3klRy5aLsnP8fs9lcjOGgmc29v7I5gN2EQx8=; __usx__=fv/ebEvROtXFGuPZHkcaFhzH9KvbwRp1wJKyHgD+gqE=; __up__=VYfXlYcOBmFkLTrlVAetqDKzzW+EM3F+fJxpasJ8vys=; _exp_=2r7jzsMSVoosq67l8/z/9c63d3MV8y55fLKX0uWTk8E=; __p__=Fj/XpmN4o8f0J/PXXfcXqYJ5VwMNB0+SYXWimWpmOORzhrgheRZyqg==; __un__=FaVIrwlLcIIHZ2PePiOeKxylcCxv7eN/NTiUttLlmvKBtn1ti1eTcCdNg+dODvqNTgiA1XynEhw=; __rf__=187GnVF+7uWX+aPmymx4KM2LyKOA3Ruu2p7P1UkrcigWgqWaCzPx+DMbyjbH8ss4WG5dBeVuMyKKXnsB/UFhqeD1Pe+3JjDloMRMDSGLeSH8C90WHML3B31RGTL8F4zhJe/rQy2kFl8=; Hm_lpvt_66fcb71a7f1d7ae4ae082580ac03c957=1514288966; monitor_seq=8; mlt=1514288966173';
headers={

        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'cookie': cookie,
        'dnt': '1;',
        'pragma': 'no-cache',
        'referer': 'https://www.guahao.com/expert/04108a62-a02b-40c2-87f9-87683ed91817000?hospDeptId=5ddfea46-52bd-40bd-99f8-2018e80f04e8000&hospitalId=4bb95ed1-b830-4e32-a692-89bca3a32d2f000',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'

    }
session=requests.session()
session.headers=headers


url='https://www.guahao.com/expert/new/shiftcase/?expertId=04108a62-a02b-40c2-87f9-87683ed91817000&hospDeptId=5ddfea46-52bd-40bd-99f8-2018e80f04e8000&hospId=4bb95ed1-b830-4e32-a692-89bca3a32d2f000&_=1514287645953'
test_url='https://www.guahao.com/expert/new/shiftcase/?expertId=97760ae7-c720-11e1-913c-5cf9dd2e7135000&hospDeptId=4ba5695a-9867-4fb6-9dca-b26eb038bdf2000&hospId=986c9800-c720-11e1-913c-5cf9dd2e7135000&_=1514288966521'
html=session.get(url)
#print(html.text)
json_all=json.loads(html.text)
with open('tmp.json','w+')as file:
    file.write(str(json_all))
    file.close()


#print(json_all)
count=0
count2=0
all_outpatient_info=json_all['data']['shiftSchedule']
#print(all_outpatient_info)
print('此次抓取到'+str(len(all_outpatient_info))+'条信息')
for info in all_outpatient_info:
    clinicType_list.add(info['clinicType'])
    if int(info['status'])==4 and int(info['price'])<100 and (info['clinicType'])=='心理门诊':
        print('发送短信通知')

    if int(info['status'])!=4:
        count=count+1
        continue
    if int(info['price']) >300 :
        print(info)
        count2=count2+1
        continue
    elif (info['clinicType'])=='心理门诊': #如果正式使用的话这里门诊类型需要修改
        print(info['shiftcaseDate']+','+info['week']+'的门诊价格为：'+str(info['price'])+',可预约'+',门诊类型为：'+info['clinicType'])




print('共有'+str(count)+'次不可预约')
print('共有'+str(count2)+'次价格过高放弃预约')
print('门诊类型全部有:'+str(clinicType_list))
if count==0:
    print('此次抓取可能登录未成功，获取的是无效数据！！！！')