# -*- coding: utf-8 -*-
import scrapy
# from firstdemo.items import FirstdemoItem
import json
import requests

class GameSpider(scrapy.Spider):
    name = 'game'
    allowed_domains = ['game.com']
    start_urls = ['https://c.y.qq.com/yanchu/cgi-bin/yanchu/mb_api/jsondata.fcg?g_tk=1378405071&cbk=callback&sCmd=citytype&IDS=0%2C0&page=1&_=1536061295413']

    def parse(self, response):
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        response=requests.get(r'https://c.y.qq.com/yanchu/cgi-bin/yanchu/mb_api/jsondata.fcg?g_tk=1378405071&cbk=callback&sCmd=citytype&IDS=0%2C0&page=1&_=1536061295413',headers=headers).content
        res=eval(response[9:-3])
        for i in res['data']['page_data']:
            images=i['star_logo']
            names=i['show_name']
            info=i['show_info']
            time=i['show_time']
            area=i['hall_name']
            money='%s~%s'%(i['max_price'],i['min_price'])

            print(images,names,info,time,area,money)
