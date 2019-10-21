'''
作业：
http://maoyan.com/board/4
抓取时需要填header
抓取内容：电影排名+电影名称+评分+图片（图片命名为“排名_电影名.jpg”）
1.爬取第一页内容
2.爬取top100所有的内容
3.把信息存入数据库
'''
from bs4 import BeautifulSoup
from pymongo import MongoClient
from bs4.element import Tag,Comment
import requests
import re
conn=MongoClient('127.0.0.1',27017)
db=conn.maoyan
my_jpg=db.jpg

heads={}
heads['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
def maoyan():
    string_1='?offset='
    list_1=[]
    for address in range(0,101,10):
        address_1='http://maoyan.com/board/4'+string_1+str(address)
        list_1.append(address_1)
    return list_1
# response1 = requests.get(r'http://maoyan.com/board/4', headers=heads)
address_2=maoyan()
my_jpg.remove()
for page in address_2:
    response=requests.get(page, headers=heads)
    html=response.content
    soup=BeautifulSoup(html,'html5lib')
    for name_1 in soup.select('dd'):
        one = name_1.i.text
        two = name_1.select('p[class="name"]')[0].a.get('title')
        three = name_1.select('p[class="score"]')[0].get_text()
        four = name_1.select('p[class="star"]')[0].get_text()
        five = name_1.select('.board-img')[0].get('data-src')
        # jpg_1=requests.get('{}'.format(five))
        # jpg_1_1=jpg_1.content
        # with open(r'D://JPG/{}_{}.jpg'.format(one,two),'wb') as f:
        #     f.write(jpg_1_1)
        winner={'电影排名':one,'电影名称':two,'电影评分':three,'演员':four}
        my_jpg.insert(winner)
        print(one, two, three, '\n', four, five)




