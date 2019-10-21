# -*- coding: utf-8 -*-
import scrapy
from movie.items import MovieItem
import json


class MeijuSpider(scrapy.Spider):
    name = "meiju"
    allowed_domains = ["httpbin.com"]
    start_urls = ['http://httpbin.org/get']

    def parse(self, response):

        with open('meiju.txt','w') as file:
            file.write(str(response.body))
        data=json.loads(response.body_as_unicode())

        item=MovieItem()
        item['args']=data['args']
        item['headers']=data['headers']
        item['origin']=data['origin']
        item['url']=data['url']
        yield item

        # movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        # for each_movie in movies:
        #     item = MovieItem()
        #     item['name'] = each_movie.xpath('./h5/a/@title').extract()[0]
        #     yield item