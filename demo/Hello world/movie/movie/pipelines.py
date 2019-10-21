# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from scrapy.exporters import JsonItemExporter

# class MoviePipeline(object):
#     def process_item(self, item, spider):
#         with open("my_meiju.txt",'a') as fp:
#             fp.write(item['name'].encode("utf8") + '\n')
#
class JsonFilePipline(object):
    def __init__(self):
        #os.path.realpath:当前文件的真实路径
        #os.path.dirnam：当前文件的父目录
        #os.path.join：连接两个字符串生成一个文件
        file=os.path.join(os.path.dirname(os.path.realpath(__file__)),'demo.json')
        self.p_file=open(file,'wb')
        # 生成一个Json
        self.itemExporter=JsonItemExporter(self.p_file,encoding='utf-8',ensure_ascii=True,indent=2)
        self.itemExporter.start_exporting()

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
        self.itemExporter.finish_exporting()
        #文件关闭
        self.p_file.close()

    def process_item(self,item,spider):
        #真实的item的输出
        self.itemExporter.export_item(item)
        return item

