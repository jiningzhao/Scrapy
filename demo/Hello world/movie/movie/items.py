# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    arges=scrapy.Field()    #参数项目
    hearders=scrapy.Field()  #头信息项目
    origin=scrapy.Field()# 原始ip项目
    url=scrapy.Field()# 访问网站项目
