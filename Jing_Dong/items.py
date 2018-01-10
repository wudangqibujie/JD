# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JingDongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    comment_count = scrapy.Field()
    goods_url = scrapy.Field()
    shop_url = scrapy.Field()
    goods_id = scrapy.Field()
    price = scrapy.Field()
    # person_number = scrapy.Field()

