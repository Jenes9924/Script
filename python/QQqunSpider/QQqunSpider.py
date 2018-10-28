import requests
from bs4 import BeautifulSoup
import json
import time

session = requests.session()
session.headers = {
    "accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "cookie": "pgv_pvid=6808715940; pac_uid=0_bc35438b40014; pgv_pvi=3141793792; pgv_si=s7252698112; _qpsvr_localtk=0.8649908330317522; pt2gguin=o0QQ号码; ptisp=ctc; RK=JYqEt2DURS; ptcz=c8b8d8a41c6168a652cd5fb1dabbaf2222c07e89a6a78f08373acaa1dd617577; pgv_info=ssid=s1497002432; __Q_w_s_hat_seed=1; zzpaneluin=; zzpanelkey=; uin=o0QQ号码; skey=@YqUgh5MfA; p_uin=o0QQ号码; pt4_token=0Kd-hlx2jxP7cMUaCyJhHX87w5hhIRXsvWxqGcllZNQ_; p_skey=dapSlkl*GO-ZLatPywRHmxQ9enKpbfV-GbalOly9Ckg_; rv2=80F74F4955FB4D7F1032B13051C955B8B8E101D67AEA5F8930; property20=1F9728DFD8A83425C5E57E9B5D1C4FA85209653813E2BBFF1E403C8E1DC8A74A138F6EBA7F97C66A",
    "dnt": "1",
    "referer": "https//h5.qzone.qq.com/groupphoto/index?inqq=3&groupId=302765357",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}

params = {
    "g_tk":"753926225",
"qzonetoken":"8170e3a82383231a2a4ce7de3e9473c2fa5cb3d6bc92c9a1969cf6b001aad9a39e88d839cbea0236c1040c6a38f112ee3d64",
"callback":"shine2_Callback",
"t":"169297195",
"uin":"QQ号码",
"platform":"qzone",
"inCharset":"utf-8",
"outCharset":"utf-8",
"source":"qzone",
"curreuestinfo":"offset=10&total=1120&basetime=1532941561",
"getcnt":"10",
"type":"1",
"gid":"302765357",
"callbackFun":"shine2",
"_":"1533381390685"

}
all_info = []
count = 2;
shine = 'shine' + str(count)
shine_callback = shine + '_Callback'
count_N = 0
params['callback'] = shine_callback
params['callbackFun'] = shine
params['_'] = int(time.time()*1000)
index_html = session.get(
    'https://h5.qzone.qq.com/proxy/domain/r.qzone.qq.com/cgi-bin/user/group_feeds_get.cgi', params=params)
count = count + 1
print(index_html.text)
if index_html =="":
    print("ERROR    :   返回数据为空")
    exit(3)
data = index_html.text
data = str(data).replace(shine + '_Callback(', '')
data = str(data).replace(');', '')
json_data = json.loads(data)
# 参数curreuestinfo
curreuestinfo = json_data['data']['curreuestinfo']
# 参数
has_more = json_data['data']['has_more']
# 参数
all_info.append(json_data)

while bool(has_more):
    params['curreuestinfo'] = curreuestinfo
    shine = 'shine' + str(count)
    shine_callback = shine + '_Callback'
    params['callback'] = shine_callback
    params['callbackFun'] = shine
    index_html = session.get(
        'https://h5.qzone.qq.com/proxy/domain/r.qzone.qq.com/cgi-bin/user/group_feeds_get.cgi', params=params)
    count = count + 1
    # print(index_html.text)
    data = index_html.text
    data = str(data).replace(shine + '_Callback(', '')
    data = str(data).replace(');', '')
    json_data = json.loads(data)
    print(str(count_N) + "    :   " + str(json_data))
    count_N = count_N + 1
    # 参数curreuestinfo
    curreuestinfo = json_data['data']['curreuestinfo']
    # 参数
    has_more = json_data['data']['has_more']
    all_info.append(json_data)

time.sleep(60)
# 写入文件
file = open('QQAlbum.json', 'w',encoding='utf-8')
# print(str(all_info))
file.write(str(all_info))
file.close()
