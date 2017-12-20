# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field


class LianjiaItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # image=Field()
    name=Field()
    money=Field()
    url=Field()
    unit=Field()
    where=Field()
