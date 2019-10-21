import requests
import json
# response=requests.get('http://www.baidu.com')
# print(response.status_code)  #打印状态码
# print(response.url)          #打印请求url
# print(response.headers)      #打印头信息
# print(response.cookies)      #打印cookies信息
# print(response.text)         #以文本形式打印网页源代码
# print(response.content)      #以字节流形式打印
# print(response.encoding)
# print(response.apparent_encoding)

# response=requests.get('http://httpbin.org/get')
# print(response.text)
# print(response.json())
# json.loads(response.text)
# json.loads(response.content)

# response=requests.get('http://img.ivsky.com/img/tupian/pre/201803/24/shui_xiaodao-012.jpg')
# b=response.content
# with open('D://fengjing2.jpg','wb') as f:
#     f.write(b)

# response = requests.get('http://www.baidu.com')
# print(response.cookies)
# print(type(response.cookies))
# for k,v in response.cookies.items():
#     print(k+':'+v)


# data={'name':'tom','age':20}
# response=requests.get('http://httpbin.org/get?name=Bob&age=24')
# print(response.text)

# data={'name':'tom','age':20}
# response=requests.get('http://httpbin.org/get',params=data)
# print(response.text)

# data={'name':'tom','age':20}
# response=requests.post('http://httpbin.org/post',data=data)
# print(response.text)

# heads = {}
# heads['User-Agent'] = 'Mozilla/5.0 ' \
# '(Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 ' \
# '(KHTML, like Gecko) Version/5.1 Safari/534.50'
# response = requests.get('http://www.baidu.com',headers=heads)
# print(response.text)

# session=requests.Session()
# data={'name':'tom','password':'123456'}
# session.post('https://www.douban.com/accounts/login',data)   #模拟登录，提交用户名密码
# session.get('https://www.douban.com/accounts/login')         #会话保持，相当于去检查一下登录状态

# data={'name':'tom','age':20}
# rp=requests.get('http://www.baidu.com',params=data)
# print(rp.status_code)
# print(rp.url)
# print(rp.text)


# try:
#     rp = requests.get('http://www.baidu.com',timeout=0.1)
#     print(rp.status_code)
# except requests.exceptions.Timeout:
#     print('Timeout')

# response=requests.get('http://www.baidu.com/s?wd=爬虫')
# print(response.status_code)
# b=response.content
# with open('D:/a6.html','wb') as f:          #wb表示以二进制存储
#     f.write(b)

data={'wd':'爬虫'}
response=requests.get('http://www.baidu.com/s',params=data)
print(response.status_code)
b=response.content
with open('D:/a6.html','wb') as f:          #wb表示以二进制存储
    f.write(b)
