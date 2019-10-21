# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from firstdemo.items import MaoyanItem


class CrawldemospiderSpider(CrawlSpider):

    #指示爬虫的唯一标识
    name = 'CrawlDemoSpider'
    #域名
    allowed_domains = ['maoyan.com']
    #初始地址
    start_urls = ['http://maoyan.com/board/4']
    #定义了一个规则的集合
    rules = (
        Rule(
            #链接的解析器
            LinkExtractor(
                allow=(r'\?offset=\d*$'),        #允许提取连接的一个规则
                # deny='',                #与allow相对，不允许提取连接的一个规则
                allow_domains='maoyan.com',       # 允许域的一个规则
                # deny_domains='',        #不允许域的一个规则
                # deny_extensions='',     #不允许的扩展名
                restrict_xpaths='//*[@id="app"]/div/div/div[2]/ul',     #用来缩小范围，在指定的某个xpath区域内提取咱们allow中定义的链接
                # restrict_css='',        #用来缩小范围，在指定的某个css区域内提取咱们allow中定义的链接

            ),
            callback='parse_item',             # 绝对不可定义成parse
            follow=True                        #需要跟进flag
        ),
    )

    def parse_item(self, response):
        details = response.xpath('//*[@id="app"]/div/div/div[1]/dl/dd[*]')
        for detail in details:

            # 排名: //*[@id="app"]/div/div/div[1]/dl/dd[1]/i
            ranking = detail.xpath('i/text()').extract_first()
            # 图片：//*[@id="app"]/div/div/div[1]/dl/dd[1]/a/img[2]
            image = detail.xpath('a/img[2]/@data-src').extract_first()
            # 名字：//*[@id="app"]/div/div/div[1]/dl/dd[1]/div/div/div[1]/p[1]/a
            file_name = detail.xpath('div/div/div[1]/p[1]/a/text()').extract_first()
            # 主演：//*[@id="app"]/div/div/div[1]/dl/dd[1]/div/div/div[1]/p[2]
            zhuyan = detail.xpath('div/div/div[1]/p[2]/text()').extract_first()
            # 上映时间：//*[@id="app"]/div/div/div[1]/dl/dd[1]/div/div/div[1]/p[3]
            time = detail.xpath('div/div/div[1]/p[3]/text()').extract_first()
            # 评分：//*[@id="app"]/div/div/div[1]/dl/dd[1]/div/div/div[2]/p/i[1]
            score_1 = detail.xpath('div/div/div[2]/p/i[1]/text()').extract_first()
            # //*[@id="app"]/div/div/div[1]/dl/dd[1]/div/div/div[2]/p/i[2]
            score_2 = detail.xpath('div/div/div[2]/p/i[2]/text()').extract_first()

            print('ranking:%s' % ranking)
            print('image:%s' % image)
            print('file_name:%s' % file_name)
            print('zhuyan:%s' % zhuyan)
            print('time:%s' % time)
            print('score:%s%s' % (score_1, score_2))
            print('==' * 80)

            item = MaoyanItem()
            item['ranking'] = ranking
            item['file_name'] = file_name
            item['image_urls'] = image
            item['zhuyan'] = zhuyan
            item['time'] = time
            item['score'] = score_1 + score_2
            yield item
