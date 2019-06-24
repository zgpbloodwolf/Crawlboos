# -*- coding: utf-8 -*-
import scrapy
from txzp.items import TxzpItem
import time


class TxzpinfoSpider(scrapy.Spider):
    name = 'txzpinfo'
    allowed_domains = ['zhipin.com']
    # bpth_url="https://www.zhipin.com/c101010100-p100109/?page=1&ka=page-1"
    #城市
    # country='101010100'
    #职业
    # zy = '100109'
    #页数
    # pages='1'
    # start_urls = ['https://www.zhipin.com/c%s-p%s/?page=%s&ka=page-%s'%(country,zy,pages,pages)]
    print(1)
    start_urls = ['https://www.zhipin.com/c101010100-p100109/?page=1&ka=page-1']
    print(2)
    def parse(self, response):
        print('3')
        informationlist= response.xpath('//div[@class="job-primary"]')
        print('4')
        # inlist=[]
        for infor in informationlist:
            print('5')
    
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
            print(123)
            time.sleep(1)
            nextlink ="https://www.zhipin.com/" + response.xpath('//a[@class="next"]/@href').extract()[0]
            yield scrapy.Request(nextlink, callback = self.parse)



