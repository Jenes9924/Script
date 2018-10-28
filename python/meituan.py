import zlib
import json
import requests
import time
import random
import base64

class ROHR:

    #省略aM
    def __init__(self,rId, ver, ts, cts, brVD, brR, bI, mT, kT, aT, tT,sign):
        self.rId = rId
        self.ver = ver
        self.ts = ts
        self.cts = cts
        self.brVD = brVD
        self.brR = brR
        self.bI = bI
        self.mT = mT
        self.kT = kT
        self.aT = aT
        self.tT = tT

        self.sign=sign

    def __str__(self):
        return '''{"rId":'''+str(self.rId).replace(' ','')+''',"ver":"'''+str(self.ver).replace(' ','')+'''","ts":'''''+str(self.ts).replace(' ','')+',"cts":'+str(self.cts).replace(' ','')+',"brVD":'+str(self.brVD).replace(' ','')+',"brR":'+str(self.brR).replace(' ','')+',"bI":'+str(self.bI).replace(' ','')+',"mT":'+str(self.mT).replace(' ','')+',"kT":'+str(self.kT).replace(' ','')+',"aT":'+str(self.aT).replace(' ','')+',"tT":'+str(self.tT).replace(' ','')+',"aM":"","sign":"'+str(self.sign).replace(' ','')+'"}'





# rohr=''' rId: Rohr_Opt.Flag,
#                 ver: "1.0.5",
#                 ts: new Date().getTime(),
#                 cts: new Date().getTime(),
#                 brVD: getBrowserViewportDimensions(),
#                 brR: getBrowserResolution(),
#                 bI: getBaseInfo(),
#                 mT: [],
#                 kT: [],
#                 aT: [],
#                 tT: [],
#                 aM: getAutomate()'''

ts=int(time.time()*1000)-random.randint(30000,70000)
cts=int(time.time()*1000)

sign='"wmpoiid=325203032547253"'
sign1=zlib.compress(sign.encode('utf-8'))
sign=base64.b64encode(sign1).decode('utf-8')
print(sign)

rohr=ROHR(100010,"1.0.5",ts,cts,[412,660],[[412,732],[412,732],24,24],'["http://i.waimai.meituan.com/mti/restaurant/288098810011219","http://i.waimai.meituan.com/mti/restaurant/288098810011219"]','["348,104"]',[],'["348,104,SPAN"]',[],sign)
# comp='{"rId":100010,"ver":"1.0.5","ts":1516377681682,"cts":1516377756677,"brVD":[412,660],"brR":[[412,732],[412,732],24,24],"bI":["http://i.waimai.meituan.com/mti/restaurant/288098810011219","http://i.waimai.meituan.com/mti/restaurant/288098810011219"],"mT":["348,104"],"kT":[],"aT":["348,104,SPAN"],"tT":[],"aM":"","sign":"eJxTKs8tyM/MTLE1srAwsLSwMDQwMDQ0MrRUAgBh7AaF"}'
#
res=str(rohr)
#
# print(str(rohr)==comp)
# print('len(res)='+str(len(res)))
# print('len(comp)='+str(len(comp)))
# print(res)
# for i in range(len(comp)):
#     if res[i]!=comp[i]:
#         print(res[i])
#         print(comp[i])
#         print(res[0:i])
#         print(comp[0:i])
#         break

# print(res)
res=zlib.compress(res.encode('utf-8'))
token=base64.b64encode(res).decode('utf-8')
print(token)


headers={
'Accept':'*/*',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9',
'Content-Length':'131',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':'_lxsdk_cuid=15ed0e4a891c8-08a61a49759a63-5848211c-1fa400-15ed0e4a892c8; _lxsdk=15ed0e4a891c8-08a61a49759a63-5848211c-1fa400-15ed0e4a892c8; _ga=GA1.3.477917090.1516369501; _gid=GA1.3.705071630.1516369501; iuuid=6FA5BB892FF3549B11F015201F8982783922CAB1BA801C3D27C2E4F83B547813; ci=10; cityname=%E4%B8%8A%E6%B5%B7; webp=1; __utma=74597006.1603297605.1516369518.1516369518.1516369518.1; __utmz=74597006.1516369518.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); w_utmz="utm_campaign=(direct)&utm_source=5007&utm_medium=(none)&utm_content=(none)&utm_term=(none)"; w_uuid=0nShdQsAXv8AuOlxfuljJKLgJGTuYG7-4C4DVmAMz4qTM7xDWP5rD27jLkxSIrOW; utm_source=0; w_cid=310100; w_cpy_cn="%E4%B8%8A%E6%B5%B7"; w_cpy=shanghai; mtcdn=K; i_extend=C_b1Gimthomepagecategory1394H__a100040__b1; isid=AA9F9177AE1354CD554C45512CFDE58E; oops=Ayd5JrDotdhlNGiIfWTz7wJ5SacAAAAARQUAAD_c6nyjbnfRbmXVUV4fddDvZUl6uEl7ce5_l0GW8AGXqS6mqsdeEqF4wZUjQNF1hg; u=581243500; logintype=fast; lt=Ayd5JrDotdhlNGiIfWTz7wJ5SacAAAAARQUAAD_c6nyjbnfRbmXVUV4fddDvZUl6uEl7ce5_l0GW8AGXqS6mqsdeEqF4wZUjQNF1hg; n=uPe215985236; uuid=958be10c8e454c938bdf.1516441732.1.0.0; _lx_utm=utm_source%3Dbaidu%26utm_medium%3Dorganic%26utm_term%3D%25E7%25BE%258E%25E5%259B%25A2; unc=uPe215985236; _gat=1; __mta=209474221.1516369502302.1516369502302.1516441738075.2; terminal=i; w_visitid=4f436983-7172-45a7-8482-46cb500a6eab; wx_channel_id=0; w_addr=%E4%B8%8A%E6%B5%B7%E5%B8%82; w_latlng=31221140,121544090; wm_poi_view_id=325203032547253; poiid=325203032547253; JSESSIONID=1aabfwfwpa5ib19mp5i37rdm90; _lxsdk_s=16112f8931e-3b4-092-a4b%7C%7C7; __mta=209474221.1516369502302.1516441738075.1516441748971.3',
'DNT':'1',
'Host':'i.waimai.meituan.com',
'Origin':'http://i.waimai.meituan.com',
'Proxy-Connection':'keep-alive',
'Referer':'http://i.waimai.meituan.com/restaurant/325203032547253',
'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36',
'X-Requested-With':'XMLHttpRequest'
}

data={
'wmpoiid':'325203032547253',
'uuid':'0nShdQsAXv8AuOlxfuljJKLgJGTuYG7-4C4DVmAMz4qTM7xDWP5rD27jLkxSIrOW',
'platform':'3',
'partner':'4',
'userid':'581243500'
}

url='http://i.waimai.meituan.com/ajax/v6/poi/info?_token='
url=url+token

session=requests.session()
session.headers=headers
result=session.post(url,data=data)
print(result.text)