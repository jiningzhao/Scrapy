from bs4 import BeautifulSoup
from bs4.element import Tag,Comment
import requests
response=requests.get('http://www.baidu.com/s?wd=爬虫')
html=response.content
soup=BeautifulSoup(html,'html5lib')
for i in soup.descendants:
    if type(i)==Tag and i.name=='div' and i.get('class')==['result', 'c-container', '']:
        k=''
        for j in i.a.stripped_strings:
            k+=j
        print(i.a.get('href'),k)


