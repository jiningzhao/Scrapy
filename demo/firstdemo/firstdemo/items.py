# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstdemoItem(scrapy.Item):
    # define the fields for your item here like:

    args = scrapy.Field()  # 参数项目
    headers = scrapy.Field()  # 头信息项目
    origin = scrapy.Field()  # 原始ip项目
    url = scrapy.Field()  # 访问网站项目

class KugouItem(scrapy.Item):
    number = scrapy.Field()
    name = scrapy.Field()
    image = scrapy.Field()
    change=scrapy.Field()

class MaoyanImageItem(scrapy.Item):
    image_urls=scrapy.Field()         #图片的路径项目
    images=scrapy.Field()             #管道中会临时用到的一个项目值
    image_paths=scrapy.Field()        #图片保存在磁盘中的路径
    file_name=scrapy.Field()        #图片保存在磁盘中的路径

class MaoyanItem(scrapy.Item):
    ranking=scrapy.Field()
    file_name=scrapy.Field()
    image_urls = scrapy.Field()
    zhuyan=scrapy.Field()
    time=scrapy.Field()
    score=scrapy.Field()
    images = scrapy.Field()  # 管道中会临时用到的一个项目值
    image_paths = scrapy.Field()  # 图片保存在磁盘中的路径

class QQItem(scrapy.Item):
    image_urls=scrapy.Field()
    names = scrapy.Field()
    info = scrapy.Field()
    time = scrapy.Field()
    area = scrapy.Field()
    money = scrapy.Field()
    images = scrapy.Field()  # 管道中会临时用到的一个项目值
class xiciItem(scrapy.Item):
    IP = scrapy.Field()
    Duankou = scrapy.Field()
    Sever_area = scrapy.Field()
    Niming = scrapy.Field()
    Type = scrapy.Field()
    connect_speed = scrapy.Field()
    connect_time = scrapy.Field()
    save_time = scrapy.Field()
    yanzheng_time = scrapy.Field()
class MaoyanCrawlItem(scrapy.Item):
    movie_name = scrapy.Field()
    movie_type = scrapy.Field()
    movie_longer = scrapy.Field()



