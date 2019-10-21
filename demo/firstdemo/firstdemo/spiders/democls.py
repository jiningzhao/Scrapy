# -*- coding: utf-8 -*-
import scrapy
from firstdemo.items import FirstdemoItem
import json


class DemoclsSpider(scrapy.Spider):
    name = 'democls'
    allowed_domains = ['democls.com']
    start_urls = ['http://httpbin.org/get']

    def parse(self, response):
        # with open('meiju.txt','w') as file:
        #     file.write(str(response.body))

        # body_as_unicode:返回unicode格式的字符串
        data=json.loads(response.body_as_unicode())   # 返回可观看的字符串

        item=FirstdemoItem()
        item['args']=data['args']
        item['headers']=data['headers']
        item['origin']=data['origin']
        item['url']=data['url']
        yield item
