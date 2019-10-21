from bs4 import BeautifulSoup
import bs4
# html='''<!DOCTYPE html>
# <html>
# 	<head>
# 		<title>The Dormouse's story</title>
# 	</head>
# 	<body>
# 		<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# 		<p class="story">
# 			Once upon a time there were three little sisters; and their names were
# 			<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
# 			<a href="http://www.baidu.com/s?wd=Lacie" class="sister" id="link2">Lacie</a> and
# 			<a href="http://www.baidu.com/s?wd=Tillie" class="sister" id="link3">Tillie</a>;
# 			and they lived at the bottom of a well.
# 		</p>
# 		<p class="story">...</p>
# 	</body>
# </html>
# '''
html=open(r'D:\Documents\HBuilderProjects\myWeb\bf.html')#打开html文件并赋值给对象
soup=BeautifulSoup(html,'html5lib')     #先构造出BeautifulSoup对象，传入参数是待解析的内容和解析格式
# print('*-'*10+'将待解析的内容打印出来'+'*-'*20)
# print(soup.prettify())                  #将待解析的内容打印出来
# print()
#
# #BeautifulSoup对象名.html标签名-->得到该标签内容（只得到第一个）
# print('*-'*10+'得到该标签内容（只得到第一个）'+'*-'*20)
# print(soup.a)
# print(soup.title)
# print()
#
# #BeautifulSoup对象名.html标签名.attrs-->得到该标签内设置的属性，attrs是字典的形式
# print('*-'*10+'得到该标签内设置的属性，attrs是字典的形式'+'*-'*20)
# print(soup.p.attrs)
# print(soup.a.attrs)
# print()
#
# #访问某个标签属性的具体值时，用法与字典类似
# print('*-'*10+'访问某个标签属性的具体值时，用法与字典类似'+'*-'*20)
# print(soup.p['class'])                  #查询
# print(soup.p.get('class'))              #查询
# print(soup.a['href'])
# print(soup.a.get('class'))
# print()
#
# print('*-'*10+'修改(意义不大，不写回文件中)'+'*-'*20)
# soup.p['href']='http://www.baidu.com/s?wd=href'              #修改
# print(soup.p)
# print()
#
# print('*-'*10+'输出的是可遍历的字符串/获取标签注释文字'+'*-'*20)
# print('p标签内容：',soup.p.string,'\t类型：',type(soup.p.string))  #输出的是可遍历的字符串,是NavigableString类型
# print('a标签内容：',soup.a.string,'\t\t\t\t\t类型：',type(soup.a.string))   #获取标签注释文字的时候，输出的是comment类型
#
# print('*-'*40)
# if type(soup.a.string)==bs4.element.Comment:
#     print(soup.a.string)     #当标签下只有一个或没有子标签时可以用，多个子标签时显示的是None
#
# print('*-'*40)
# for child in soup.body.children:
#     print(child)
#
# print('子孙','*-'*40)
# for i in soup.body.descendants:
#     print('@'*40)
#     print(i)
#练习：获取以上网页内容中有效的超链接（包括超链接文字和地址）
# for i in soup.body.descendants:
#     if i.name=='a' and type(i.string)!=bs4.element.Comment:
#         print(i.get('href'),i.string)

# for i in soup.body.stripped_strings:         #strings打印多个标签里的字符串,stripped_strings表示跳过多余的空白
#     print(i,end='')

# content=soup.head.title.string
# for i in content.parents:
#     print(i.name)

# print(soup.p.next_sibling.next_sibling)

# print(soup.p.prev_silbing)

# for i in soup.a.next_siblings:
#     print(i.name)

# print(soup.p.next_element)
# print(soup.body.previous_element)

'''
练习;
1.找到第一个<a>标签，通过.next_sibling找到同级别所有<a>标签，并打印出其中超链接的地址
2.找到第一个<a>标签，通过.next_siblings找到同级别所有<a>标签，并打印出其中超链接的地址
3.找到第一个<a>标签，寻找其父节点，打印父节点下所有的文字
'''
print('练习1：'+'*'*30)
tag_a=soup.a
print(tag_a)
while True:
    tag_a=tag_a.next_sibling
    if type(tag_a)==bs4.element.Tag and type(tag_a)!=bs4.element.Comment:
        print(tag_a.get('href'))
    if tag_a.next_sibling==None:
        break
print('\n')

print('练习2：'+'*'*30)
tag_a=soup.a
print(tag_a)
for i in tag_a.next_siblings:
    if type(i)==bs4.element.Tag and type(tag_a)!=bs4.element.Comment:
        print(i.get('href'))
print('\n')

print('练习3：'+'*'*30)
tag_a=soup.a
print(tag_a)
text_p=tag_a.parent
print(text_p)
for i in text_p.stripped_strings:
    print(i,end=' ')
'''
作业：
1.预习正则表达式
2.百度爬虫检索，把超链接标题扒取下来（过滤）网址和文字
'''
html.close()#打开文件别忘记关闭文件