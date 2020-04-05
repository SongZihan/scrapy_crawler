# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CoupangItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    # 单位价格
    single_price = scrapy.Field()
    comment_number = scrapy.Field()
    comment_star = scrapy.Field()
    # 其他信息
    other_info = scrapy.Field()


