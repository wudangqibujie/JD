# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

class JingDongPipeline(object):
    #先初始化要操作的文件
    def __init__(self):
        self.file = codecs.open('JD.json','w',encoding="utf-8")

    #存储数据，把item实例作为json数据写入到文件中
    def process_item(self, item, spider):
        lines = json.dumps(dict(item),ensure_ascii = False)+'\n'
        self.file.write(lines)
        return item

    def close_spider(self,spider):
        self.file.close()
