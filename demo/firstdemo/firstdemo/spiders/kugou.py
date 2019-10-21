'''
作业：
http://www.kugou.com/yy/html/singer.html
爬取酷狗音乐中的歌手排行榜，以json格式输出到文件当中
'''
import scrapy
from firstdemo.items import KugouItem

class KugouSpider(scrapy.Spider):
    name = 'kugou'
    start_urls=['http://www.kugou.com/yy/html/singer.html']
    page=2
    page2=5
    def parse(self, response):
        details=response.xpath('//*[@id="list_head"]/li[*]')
        for detail in details:
            #排名：//*[@id="list_head"]/li[1]/a/i
            ranging=detail.xpath('a/i/text()').extract_first()
            #姓名：//*[@id="list_head"]/li[1]/strong/a
            name_1= detail.xpath('strong/a/text()').extract_first()
            #图片：//*[@id="list_head"]/li[1]/a/img
            image = detail.xpath('a/img/@_src').extract_first()
            print('排名：%s'%ranging)
            print('歌手：%s'%name_1)
            print('图片：%s'%image)
            print('=='*80)
            item = KugouItem()
            item['number'] = ranging
            item['name'] = name_1
            item['image'] = image
            yield item
        details_1 = response.xpath('//*[@id="list1"]/ul[*]')
        for detail in details_1:
            details_2 = detail.xpath('li[*]')
            for i in details_2:
                # 排名：//*[@id="list1"]/ul[1]/li[1]/span[1]
                ranging_1 = i.xpath('span[1]/text()').extract_first()
                # 姓名：//*[@id="list1"]/ul[1]/li[1]/a
                name_2 = i.xpath('a/text()').extract_first()
                # 排名变动：//*[@id="list1"]/ul[1]/li[1]/span[2]
                change_1 = i.xpath('span[2]/@title').extract_first()
                print('排名：%s' % ranging_1)
                print('歌手：%s' % name_2)
                print('排名变动：%s'%change_1)
                print('==' * 80)

                item = KugouItem()
                item['number'] = ranging_1
                item['name'] = name_2
                item['change']=change_1
                yield item
        if self.page <= self.page2:
            url='http://www.kugou.com/yy/singer/index/%s-all-1.html'%self.page
            yield self.next_request(url)
        self.page+=1
    def next_request(self,url):
        return scrapy.http.Request(url)





