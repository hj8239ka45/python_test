from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

html = urlopen("https://morvanzhou.github.io/static/scraping/table.html").read().decode('utf-8')
soup = BeautifulSoup(html, features='lxml')
#用正則找.jpg檔--> .*?\.jpg 前面為任何形式後面為.jpg
img_links = soup.find_all("img", {'src': re.compile('.*?\.jpg')})
for link in img_links:
    print(link['src'])
    
href_links = soup.find_all("a", {'href': re.compile('https://*')})
for link2 in href_links:
    print(link2['href'])
