# -*- coding: utf-8 -*-
import scrapy
import requests
from firstdemo.items import xiciItem

class XicidailiSpider(scrapy.Spider):
    name = 'xicidaili'
    allowed_domains = ['www.xicidaili.com']
    start_urls = ['http://www.xicidaili.com/nn/1']
    cur_page=1


    def parse(self, response):
        details=response.xpath('//*[@id="ip_list"]/tr')
        for detail in details:
            # print(1)
            # if detail.xpath('/@class').extract_first()=='subtitle':
            #     pass
            #IP://*[@id="ip_list"]/tbody/tr[3]/td[2]
            IP=detail.xpath('td[2]/text()').extract_first()
            #端口：//*[@id="ip_list"]/tbody/tr[3]/td[3]
            Duankou=detail.xpath('td[3]/text()').extract_first()
            #服务器地址：//*[@id="ip_list"]/tbody/tr[3]/td[4]
            Sever_area=detail.xpath('td[4]/a/text()').extract_first()
            #是否匿名：//*[@id="ip_list"]/tbody/tr[3]/td[5]
            Niming=detail.xpath('td[5]/text()').extract_first()
            #类型：//*[@id="ip_list"]/tbody/tr[3]/td[6]
            Type=detail.xpath('td[6]/text()').extract_first()
            #连接速度：//*[@id="ip_list"]/tbody/tr[35]/td[7]/div
            connect_speed=detail.xpath('td[7]/div/@title').extract_first()
            #连接时间：//*[@id="ip_list"]/tbody/tr[3]/td[8]
            connect_time=detail.xpath('td[8]/div/@title').extract_first()
            #存活时间：//*[@id="ip_list"]/tbody/tr[2]/td[9]
            save_time = detail.xpath('td[9]/text()').extract_first()
            #验证时间：//*[@id="ip_list"]/tbody/tr[2]/td[10]
            yanzheng_time = detail.xpath('td[10]/text()').extract_first()
            print(IP,Duankou,Sever_area,Niming,Type,connect_speed,connect_time,save_time,yanzheng_time)

            item=xiciItem()
            item['IP']=IP
            item['Duankou'] =Duankou
            item['Sever_area'] =Sever_area
            item['Niming'] =Niming
            item['Type'] =Type
            item['connect_speed'] =connect_speed
            item['connect_time'] =connect_time
            item['save_time'] =save_time
            item['yanzheng_time'] =yanzheng_time
            yield item

        if self.cur_page < 100:
            url = 'http://www.xicidaili.com/nn/{}'.format (self.cur_page+1)
            yield self.next_request(url)
        self.cur_page +=1

    def next_request(self, url):
        return scrapy.http.Request(url)


