#post :登入式，多帳號變化
#get  :
import requests
import webbrowser
'''
get:把查詢資訊放在URL
'''
#wd=查詢內容
param = {"wd": "莫烦Python"}  # 搜索的信息
r = requests.get('http://www.baidu.com/s', params=param)
print(r.url)
#開啟網頁
#webbrowser.open(r.url)

'''
post:由php中提取資料
'''
#form往上提交形式 method action->php
#input
#http://pythonscraping.com/pages/files/form.html
data = {'firstname': 'mmm', 'lastname': 'sss'}
r = requests.post('http://pythonscraping.com/pages/files/processing.php', data=data)
print(r.text)


#http://pythonscraping.com/files/form2.html
#file = {'uploadFile': open('./image.png', 'rb')}
#r = requests.post('http://pythonscraping.com/files/processing2.php', files=file)
#print(r.text)

#request不會記錄登入資料
#cookies可以記錄
payload = {'username': 'Morvan', 'password': 'password'}
r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
#成立cookies放入下次的訊息
print(r.cookies.get_dict())
# {'username': 'Morvan', 'loggedin': '1'}
r = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=r.cookies)
#print(r.text)
# Hey Morvan! Looks like you're still logged into the site!


#用session(連續對話)傳遞cookie
session = requests.Session()
payload = {'username': 'Morvan', 'password': 'password'}
r = session.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
print(r.cookies.get_dict())
# {'username': 'Morvan', 'loggedin': '1'}
r = session.get("http://pythonscraping.com/pages/cookies/profile.php")
#print(r.text)
# Hey Morvan! Looks like you're still logged into the site!
