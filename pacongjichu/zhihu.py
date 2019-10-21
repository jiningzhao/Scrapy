import bs4
from bs4 import BeautifulSoup
import requests
heads={}
heads['User-Agent']='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
response=requests.get('https://www.zhihu.com',headers=heads)
html=response.content
soup=BeautifulSoup(html,'html5lib')
# print(soup.prettify())
for i in soup.descendants:
    if i.name=='a':
        print(i.get('href'),i.string)
print(response.status_code)
