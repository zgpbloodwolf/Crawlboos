# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

class TxzpPipeline(object):
	def __init__(self):
		self.f = codecs.open('zpinfo.json','w','utf-8')
	def process_item(self, item, spider):
		con = json.dumps(dict(item),ensure_ascii=False)+",\n"
		self.f.write(con)
		return item

	def close_spider(self,spider):
		self.f.close()

