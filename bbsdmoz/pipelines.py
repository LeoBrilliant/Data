# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
from scrapy import log
from bbsdmoz.items import BbsdmozItem
from twisted.enterprise import adbapi
from scrapy.contrib.exporter import XmlItemExporter


class BbsdmozPipeline(object):
    def __init__(self):
        pass 
    
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        
        return pipeline
    
    def spider_opened(self, spider):
        self.file = open('bbsData.xml', 'wb')
        self.exporter = XmlItemExporter(self.file)
        self.exporter.start_exporting()
        
    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
        
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
