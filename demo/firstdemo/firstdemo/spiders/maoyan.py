import scrapy
from scrapy.http import Request
from firstdemo.items import MaoyanImageItem
from firstdemo.items import MaoyanItem
from gridfs import GridFS
class MaoyanSpider(scrapy.Spider):
    '''
    猫眼的爬虫
    '''

    name='maoyan'
    start_urls=['http://maoyan.com/board/4']
    cur_page=1
    total_page=10

    custom_settings = {
        'MONGO_URI':'mongodb://127.0.0.1:27017/%admin',
        'MONGO_DATABASE':'scrapy',
        'MONGO_COLLECTION':'scrapy_collection'
    }

    def parse(self,response):
        details=response.xpath('//*[@id="app"]/div/div/div[1]/dl/dd[*]')

        # if 'aa' in response.request.meta:
        #     print(response.request.meta['aa'])

        for detail in details:
            # 排名: //*[@id="app"]/div/div/div[1]/dl/dd[1]/i
            ranking=detail.xpath('i/text()').extract_first()
            #图片：//*[@id="app"]/div/div/div[1]/dl/dd[1]/a/img[2]
            image = detail.xpath('a/img[2]/@data-src').extract_first()
            #名字：//*[@id="app"]/div/div/div[1]/dl/dd[1]/div/div/div[1]/p[1]/a
            file_name = detail.xpath('div/div/div[1]/p[1]/a/text()').extract_first()
            #主演：//*[@id="app"]/div/div/div[1]/dl/dd[1]/div/div/div[1]/p[2]
            zhuyan = detail.xpath('div/div/div[1]/p[2]/text()').extract_first()
            #上映时间：//*[@id="app"]/div/div/div[1]/dl/dd[1]/div/div/div[1]/p[3]
            time=detail.xpath('div/div/div[1]/p[3]/text()').extract_first()
            #评分：//*[@id="app"]/div/div/div[1]/dl/dd[1]/div/div/div[2]/p/i[1]
            score_1 = detail.xpath('div/div/div[2]/p/i[1]/text()').extract_first()
            #//*[@id="app"]/div/div/div[1]/dl/dd[1]/div/div/div[2]/p/i[2]
            score_2=detail.xpath('div/div/div[2]/p/i[2]/text()').extract_first()



            print('ranking:%s'%ranking)
            print('image:%s' % image)
            print('file_name:%s' % file_name)
            print('zhuyan:%s' % zhuyan)
            print('time:%s' % time)
            print('score:%s%s' % (score_1,score_2))
            print('=='*80)


            item=MaoyanItem()
            item['ranking']=ranking
            item['file_name'] =file_name
            item['image_urls'] =image
            item['zhuyan'] =zhuyan
            item['time'] =time
            item['score'] =score_1+score_2
            yield item






        if self.cur_page <  self.total_page:
            url='http://maoyan.com/board/4?offset=%s'%(self.cur_page*10)
            yield self.next_request(url)
        self.cur_page+=1

    def next_request(self,url):
        """
        做分页请求
        :param url:
        :return:
        """
        return scrapy.http.Request(url)
