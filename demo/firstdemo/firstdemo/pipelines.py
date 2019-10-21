# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from scrapy.exporters import JsonItemExporter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
from scrapy.exceptions import DropItem
from pymongo import MongoClient
from gridfs import GridFS
import mimetypes
import requests

class FirstdemoPipeline(object):
    def process_item(self, item, spider):
        return item


class MongoDBPipeline(object):

    def __init__(self,mongo_uri, mongo_db,mongo_collection):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_collection=mongo_collection
        # conn = MongoClient('127.0.0.1', 27017)
        # db = conn.democls
        # self.my_spider = db.spider
        # self.my_spider.remove()

    @classmethod
    def from_crawler(cls,crawler):
        '''
        scrapy引擎无需对象实例化，便可调用该类的构造器
        :param crawler:
        :return:
        '''
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items'),
            mongo_collection=crawler.settings.get('MONGO_COLLECTION')
        )

    def open_spider(self, spider):
        self.client =MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.gridfs=GridFS(self.db)
    def close_spider(self,spider):
        #写入json结束标志
        # self.itemExporter.finish_exporting()     #  结束加上一行
        #文件关闭
        self.client.close()         # 关闭数据库

    def process_item(self,item,spider):
        #真实的item的输出
        self.db[self.mongo_collection].insert_one(dict(item))
        self._write_image(item['image_urls'])
        return item

    def _write_image(self,image_url):
        '''
        该方法用来将网络路径上的图片保存到DB里
        :return:
        '''
        if self.gridfs.exists(id=image_url) is False:
            #DB中不存在指定的这个url路径的时候进行图片的写入
            #image_url ->http://p1.meituan.net/movie/20803f59291c47e1e116c11963ce019e68711.jpg@160w_220h_1e_1c
            image_url=image_url.split('@')[0]
            mime_type=mimetypes.guess_type(image_url)[0] #会取出类似image/png这样的数据

            try:
                # 向image_url发送请求
                res = requests.get(image_url, stream=True, timeout=30)

                # os.path.basename:http://p1.meituan.net/movie/20803f59291c47e1e116c11963ce019e68711.jpg@160w_220h_1e_1c
                # 20803f59291c47e1e116c11963ce019e68711.jpg@160w_220h_1e_1c
                self.gridfs.put(res.raw, _id=image_url, content_type=mime_type, filename=os.path.basename(image_url))

            except Exception as exp:
                print(exp)


class MaoyanImagePipeline(ImagesPipeline):

    def get_media_requests(self,item,info):
        yield Request(item['image_urls'],meta={'film_name': item['file_name']})

    def item_completed(self, results, item, info):
        image_paths=[x['path']for ok,x in results if ok]
        if not image_paths:
            raise DropItem('Item contains no images')
        item['image_paths']=image_paths
        return item

    def file_path(self, request, response=None, info=None):

        file_name=request.meta['film_name']
        # images=request.url.split()
        #image_name=request.url.split('/')[-1]
        #image_name=image_name.split('@')[0]
        #print(image_name)
        return 'full/%s.jpg'%(file_name)


class JsonFilePipeline(object):
    def __init__(self):
        #os.path.realpath:当前文件的真实路径
        #os.path.dirnam：当前文件的父目录
        #os.path.join：连接两个字符串生成一个文件
        file=os.path.join(os.path.dirname(os.path.realpath(__file__)),'demo.json')
        self.p_file=open(file,'wb')
        # 生成一个Json
        self.itemExporter=JsonItemExporter(self.p_file,encoding='utf-8',ensure_ascii=False,indent=2)
        self.itemExporter.start_exporting()  # 开始加上一行

    @classmethod
    def from_crawler(cls,crawler):
        '''
        scrapy引擎无需对象实例化，便可调用该类的构造器
        :param crawler:
        :return:
        '''
        return cls()

    def close_spider(self,spider):
        #写入json结束标志
        self.itemExporter.finish_exporting()     #  结束加上一行
        #文件关闭
        self.p_file.close()         # 有开就有关

    def process_item(self,item,spider):
        #真实的item的输出
        self.itemExporter.export_item(item)
        return item