import bs4
from bs4.element import Tag, Comment
from bs4 import BeautifulSoup
import re
import requests

'''
作业：
1.爬虫爬取京东搜索‘手表’的网页
2.从中提取出所有的品牌
3.找到当前页中所有‘自营’商品的名称和价格
'''

response=requests.get('https://search.jd.com/Search?keyword=%E6%89%8B%E8%A1%A8&enc=utf-8&suggest=1.rem.0.0&wq=%E6%89%8B%E8%A1%A8&pvid=2bcc470225a64ea4b45cb68f8f17b390')
html=response.content

soup=BeautifulSoup(html,'html5lib')
for i in soup.find_all(id=re.compile('brand')):
    print(i.a.get('title'))
n=0
for j in soup.find_all(class_=['goods-icons', 'J-picon-tips', 'J-picon-fix']):
    n+=1
    name_1=j.find_parents('div')[1].find_all(class_=['p-name', 'p-name-type-2'])[0].a.get('title')
    price_1=j.find_parents('div')[1].find_all(class_=['p-price'])[0].i.string
    print(n,':',name_1,price_1+'￥')