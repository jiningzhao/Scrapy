# -*- coding: utf-8 -*-
import scrapy
from firstdemo.items import QQItem
from scrapy.http import Request
import json
import requests

class GameSpider(scrapy.Spider):

    name = 'QQ'
    allowed_domains = ['c.y.qq.com']
    start_urls = ['https://c.y.qq.com/yanchu/cgi-bin/yanchu/mb_api/jsondata.fcg?g_tk=1378405071&cbk=callback&sCmd=citytype&IDS=0%2C0&page=0&_=1536061295413']
    cur_page = 0
    # headers = {}
    # headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    # response = requests.get(r'https://c.y.qq.com/yanchu/cgi-bin/yanchu/mb_api/jsondata.fcg?g_tk=1378405071&cbk=callback&sCmd=citytype&IDS=0%2C0&page=0&_=1536061295413',headers=headers).content
    def parse(self, response):
        res=eval(response.body_as_unicode()[9:-3])
        for i in res['data']['page_data']:
            images=i['star_logo']
            names=i['show_name']
            info=i['show_info']
            time=i['show_time']
            area=i['hall_name']
            money='%s~%s'%(i['max_price']/100,i['min_price']/100)

            print(images,names,info,time,area,money)
            item=QQItem()

            item['image_urls'] =images
            item['names'] =names
            item['info'] =info
            item['time'] =time
            item['area'] =area
            item['money'] =money
            yield item
        if self.cur_page < 123:
            url = 'https://c.y.qq.com/yanchu/cgi-bin/yanchu/mb_api/jsondata.fcg?g_tk=1378405071&cbk=callback&sCmd=citytype&IDS=0%2C0&page={}&_=1536061295413'.format(self.cur_page+1)
            yield self.next_request(url)
        self.cur_page+=1

    def next_request(self,url):
        return Request(url)


