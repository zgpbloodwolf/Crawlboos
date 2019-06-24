# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TxzpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #职位名
    posiname=scrapy.Field()
    #职位薪资
    posimoney=scrapy.Field()
    #职位地点
    posiadd=scrapy.Field()
    #公司
    posicom=scrapy.Field()
    #公司种类
    comkind= scrapy.Field()
    #人员
    releaseman = scrapy.Field()
    #职位链接
    posilink=scrapy.Field()

    
    
    # pass
