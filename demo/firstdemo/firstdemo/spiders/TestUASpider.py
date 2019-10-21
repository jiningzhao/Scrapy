# -*- coding: utf-8 -*-
import scrapy


class TestuaspiderSpider(scrapy.Spider):
    name = 'TestUASpider'
    allowed_domains = ['httpbin.org']
    #起始url的地址的设定方法一：定义start_urls的属性
    # start_urls = ['http://httpbin.org/get']
    def start_requests(self):
        """
        定义起始url的方法二：通过start_requests函数定义自己的起始url
        :return:
        """
        # start_url = ['http://httpbin.org/get?param=%s']
        # for i in range(10):
        #     start_url='http://httpbin.org/get?param=%s'%i
        #     yield scrapy.Request(start_url)
        yield scrapy.Request('http://httpbin.org/get')

    def parse(self, response):
        # print(response.request.headers['User-Agent'])
        print(response.body_as_unicode())

