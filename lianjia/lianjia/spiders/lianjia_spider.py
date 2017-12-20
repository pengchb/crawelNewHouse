# -*- coding: utf-8 -*-
import scrapy
from lianjia.items import LianjiaItem
import json
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class LianjiaSpider(scrapy.Spider):
    name = "lianjia"
    start_urls = [
        "https://gz.fang.lianjia.com/loupan/pg"
    ]

    def parse(self, response):

        pageNumList = response.xpath('//div[@class="page-box house-lst-page-box"]/@page-data').extract()
        pageNumJson = json.loads(pageNumList[0])
        pageNum = pageNumJson['totalPage']
        for num in range(pageNum-1):
            url = response.urljoin("https://gz.fang.lianjia.com/loupan/pg"+str(num+1))
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        
        for sel in response.xpath('//ul[@class="house-lst"]/li'):
            item=LianjiaItem()
            item['name']=sel.xpath('div/div[@class="col-1"]/h2/a/text()').extract()
            item['url']=sel.xpath('div/div[@class="col-1"]/h2/a/@href').extract()
            item['money']=sel.xpath('div/div[@class="col-2"]/div/div[@class="average"]/span/text()').extract()
            item['unit']=sel.xpath('div/div[@class="col-2"]/div/div[@class="average"]/text()').extract()
            item['where']=sel.xpath('div/div[@class="col-1"]/div/span/text()').extract()
            
            yield item
