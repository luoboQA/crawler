# Define here the models for your scraped items
# 定义爬取数据的模型
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field() # MongoDB中的唯一标识符主键
    url = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
