import bs4
from bs4.element import Tag,Comment
from bs4 import BeautifulSoup
import re
import requests
# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """
html=open(r'E:\HBuilder\PChong\pachong.html')#打开html文件并赋值给对象
'''
练习1：
1.找到body下所有的p标签
2.找到body下所有p标签和a标签
3.找到整个文档中含有字母l的标签
4.找到整个文档中标签属性有href的标签
'''
soup=BeautifulSoup(html,'html5lib')
for i in soup.find_all('p'):
    print(i)
print('*-'*50)

for i in soup.find_all(['p','a']):
    print(i)
print('*-'*50)

for tag in soup.find_all(re.compile('l')):
    print(tag.name)
print('*-'*50)

def has_href(tag):
    return tag.has_attr('href')
for i in soup.find_all(has_href):
    print(i)

print('*-'*50)
print(soup.find_all(href=re.compile('la'),id='link2'))

print('*-'*50)
print(soup.find_all('a',class_='sister',id='link1'))

print('*-$-'*50)
'''
练习2：
1.查找标签属性中class='story'的标签
2.查找标签属性中name以dr开头的标签
'''
for i in soup.find_all(class_='story'):
    print(i.name)
print('*-'*50)


for i in soup.find_all(attrs={'name':re.compile('^dr')}):     # 当name与参数名name重名时，用attrs={:}的形式
    print(i.name)
print('*-'*50)
#text参数搜索文档中内容
print(soup.find_all(text=' Elsie '))# 注释也可以找，前后各加一个空格
print(soup.find_all(text=[' Elsie ','Tillie','Lacie']))# 也可以搜索列表
print(soup.find_all(text=re.compile('sister')))# 可以搜索正则表达式
print(soup.find_all(text=True)) # 输出所有文本
print('*-'*50)
#limit限制显示的数量
print(soup.find_all(text=True,limit=3)) # 输出符合条件的前三个文本
#recursive限制检索范围=False时只检索直接子节点，=True时检索所有子孙节点
for i in soup.body.find_all(text=re.compile('La'),recursive=False):
    print(i)
print('*-'*50)
#find_parent()找到当前节点的直接父节点
print(soup.a.find_parent().name)
print('*-'*50)
#find_parents()找到当前节点的父辈节点
for i in soup.a.find_parents():
    print(i.name)
print('*-'*50)
'''
练习3：
1.找到内容中以字母T开头的元素
2.在该元素的所有父节点中，找到标签为p的节点
3.在第2步的基础上，寻找其后面的所有class='story'的节点
4.在<body>范围内，查找所有的a标签和b标签，并打印其父节点的class属性值
'''
#1.找到内容中以字母T开头的元素
list1=soup.find_all(text=re.compile('^T'))
print(list1)
print('*-'*50)
#2.在该元素的所有父节点中，找到标签为p的节点
list2=list1[2].find_parents('p')
print(list2)
print('*-'*50)
#3.在第2步的基础上，寻找其后面的所有class='story'的节点,不限于兄弟节点
list3=list2[0].find_all_next(class_='story')
print(list3)
# for i in list2[0].find_all_next(class_='story'):
#     print(i)
print('*-'*50)
#4.在<body>范围内，查找所有的a标签和b标签，并打印其父节点的class属性值
for i in soup.body.find_all(['a','b']):
    print(i.parent.get('class'))
    # print(i.find_parent().get('class'))

print('*-'*60)
print(soup.select('.sister'))
print(soup.select('#link1'))
print(soup.select('p #link1'))               # 空格表示从属关系
print(soup.select('head > title'))
print(soup.select('a[class="sister"]'))      # a标签的属性class="sister"
print(soup.select('p .sister'))              # p标签的子节点里，找class="sister"
print(soup.select('a .sister'))              # 得到[]
print(soup.find_all('a',class_='sister'))    #
print(soup.select('p a[href="http://example.com/lacie"]'))
print('*-'*60)
print(type(soup.select('title')))
print(soup.select('title')[0].get_text())    # .text，.string 效果相同
print(soup.select('title')[0].text)
print(soup.select('title')[0].string)

'''
练习4：
1.找到body下所有的p标签
2.找到body下所有p标签和a标签
3.查找标签属性中class='story'的所有标签
'''
print('*-'*60)
print(soup.select('body p'))
print('*-'*60)
print(soup.select('body p,a'))
print('*-'*60)
print(soup.select('[class="story"]'))

