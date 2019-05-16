from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random
base_url= "https://baike.baidu.com"
history = ["/item/%E8%9C%98%E8%9B%9B/8135707"]
url = base_url + history[-1]


html = urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html, features='lxml')
#find:找第一個
print(soup.find('h1').get_text(),'  url: ',history[-1])

#用inspect 找a的target or class
#target:浏览器将打开一个新的窗口，给这个窗口一个指定的标记，然后将新的文档载入那个窗口
#http://www.runoob.com/tags/att-a-target.html
#在網址中可能有其他內容>用正則
sub_urls = soup.find_all('a',{"target":"_blank","href":re.compile("/item/(%.{2})+$")})
##for i in range(20):
##    if len(sub_urls)!=0:
##        history.append(random.sample(sub_urls,1)[0]['href'])
##    else:
##         # no valid sub link found
##         history.pop()
##    print(history)

for i in range(20):
    #history第一筆紀錄最早的資料，最後一筆紀錄最新
    url = base_url + history[-1]

    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')
    print(i+1, soup.find('h1').get_text(), '\turl: ', history[-1])
    #print('\this: ', history)
    # find valid urls
    sub_urls = soup.find_all("a", {"target": "_blank", "href": re.compile("/item/(%.{2})+$")})

    if len(sub_urls) != 0:
        history.append(random.sample(sub_urls, 1)[0]['href'])
    else:
        # no valid sub link found
        #pop:移除最後一個list
        history.pop()
        #print('pop\n')
