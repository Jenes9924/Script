import time

text = '''Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
Content-Length: 98
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: JSESSIONID=3151695E295BF334F126DF445DEAC8A2; happygoal_visit=1752810#20a90c83412859c30c60af6d82965321
DNT: 1
Host: navigator.happygoal.com
Origin: https://navigator.happygoal.com
Referer: https://navigator.happygoal.com/happygoal/Register.jsp?stuid=65&stuname=%25E6%259D%258E%25E6%2598%2582%25E4%25BF%25A1%2520Lily
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36
X-Requested-With: XMLHttpRequest'''

lines = text.split("\n")
for line in lines:
    words = line.split(":")
    if len(words) > 2:
        print('"' + words[0].strip() + '":"' + words[1].strip() + words[2].strip() + '",')
        continue
    print('"' + words[0].strip() + '":"' + words[1].strip() + '",')

# timestamp = int(time.time()*1000)
# print(timestamp)
