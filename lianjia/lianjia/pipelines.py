# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import codecs

class LianjiaPipeline(object):
	def __init__(self):
		self.csv_file = open("lianjia_gz_20171219.csv","wb+")
		self.csv_file.write(codecs.BOM_UTF8)
		self.csv_writer = csv.writer(self.csv_file, delimiter=',')
        
	def process_item(self, item, spider):
		if(item['money']==[]):
			item['money']=["unknown"]
			unit = item['unit'][0]
		else:
			unit = item['unit'][1]
		name = item['name'][0].decode('utf-8')
		url = "https://gz.fang.lianjia.com"+item['url'][0]
		money = item['money'][0]
		unit = unit.replace('\t','').replace('\n','').replace(' ','').decode('utf-8')
		content = name + ':_￥' + money +unit
		areaCode = "020"
		if item['where'][0].find("禅城") != -1 or item['where'][0].find("佛山") != -1 or item['where'][0].find("顺德") != -1:
			areaCode = "0757"
		self.csv_writer.writerow([name, money, content, url, areaCode,""])
		return item
