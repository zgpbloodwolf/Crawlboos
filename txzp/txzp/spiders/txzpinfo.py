# -*- coding: utf-8 -*-
import scrapy
from txzp.items import TxzpItem
import time
import json
from collections import deque


class TxzpinfoSpider(scrapy.Spider):
    name = 'txzpinfo'
    allowed_domains = ['zhipin.com']
    addque = deque()
    majorque = deque()
    with open('address.json','r') as f:
        addresslist = json.loads(f.read())["address"]
    with open('major.json','r') as f:
        majorlist = json.loads(f.read())["major"]
    for address in addresslist:
        addque.append(address)
    for major in majorlist:
        majorque.append(major)
    
    #城市
    # country='101010100'
    #职业
    # zy = '100109'
    #页数
    # pages='1'
    # start_urls = ['https://www.zhipin.com/c%s-p%s/?page=%s&ka=page-%s'%(country,zy,pages,pages)]
    start_urls = ['https://www.zhipin.com/c101010100-p100109/?page=1&ka=page-1']
    def parse(self, response):
        informationlist= response.xpath('//div[@class="job-primary"]')
        # inlist=[]
        for infor in informationlist:
            item = TxzpItem()
        	#职位
            item['posiname'] = infor.xpath('./div[@class="info-primary"]/h3/a/div/text()').extract()[0]
        	#薪资
            item['posimoney'] = infor.xpath('./div[@class="info-primary"]/h3/a/span/text()').extract()[0]
        	#地点
            item['posiadd'] = infor.xpath('./div[@class="info-primary"]/p/text()').extract()[0]
        	#公司名称
            item['posicom'] = infor.xpath('./div[@class="info-company"]/div/h3/a/text()').extract()[0]
        	#公司种类
            item['comkind'] = infor.xpath('./div[@class="info-company"]/div/p/text()').extract()[0]
        	#人员
            item['releaseman']=infor.xpath('./div[@class="info-publis"]/h3/text()').extract()[0]
        	#链接
            item['posilink'] = 'https://www.zhipin.com/'+infor.xpath('./div[@class="info-primary"]/h3/a/@href').extract()[0]
        	# item['posilink']=posilink
        	# inlist.append(item)
            yield item
        if response.xpath('//a[@class="next"]'):
            time.sleep(1)
            nextlink ="https://www.zhipin.com/" + response.xpath('//a[@class="next"]/@href').extract()[0]
            yield scrapy.Request(nextlink, callback = self.parse)
        else :
            #如果职业不为空换职业爬取
            if len(self.majorque)!=0:
                maj = str(self.majorque.popleft())
                majlink = "https://www.zhipin.com/c101010100-p"+maj+"/?page=1&ka=page-1"
                yield scrapy.Request(majlink, callback = self.parse)
            #如果职业为空，换地址换职业
            else:
                add = str(self.addque.popleft())
                for major in self.majorlist:
                    self.majorque.append(major)
                maj = str(self.majorque.popleft())
                newurl = "https://www.zhipin.com/c"+add+"-p"+maj+"/?page=1&ka=page-1"
                yield scrapy.Request(nextlink, callback = self.parse)




