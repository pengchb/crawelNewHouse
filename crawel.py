#-*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from urlparse import urljoin
import requests
import csv

url_root = "https://gz.fang.lianjia.com"
url_lianjia = "https://gz.fang.lianjia.com/loupan/pg{page}"

#已完成的页数序号，初时为0
page = 0

csv_file = open("lianjia_gz_20171217.csv","wb")
csv_writer = csv.writer(csv_file, delimiter=',')

exitPCB = 0

while True:
    page += 1
    print "fetch: ", url_lianjia.format(page=page)
    response = requests.get(url_lianjia.format(page=page))
    #print "response.text:", response.text
    html = BeautifulSoup(response.text, "html.parser")
    # print "heml:", html
    house_list = html.select(".house-lst > li")

    # 循环在读不到新的房源时结束
    if exitPCB > 0:
        break

    num = 0
    # 循环在读不到新的房源时结束
    for house in house_list:
        #print "num:", num
        areaCode = "020"
        tmpPCB = house.select("h2")
        if not tmpPCB:
            exitPCB = 1
            break
        h2_text = house.select("h2")[0].select("a")[0]
        # print h2_text
        url = (url_root + h2_text.get("href")).encode("utf8")
        #print url
        name = h2_text.text.encode("utf8")
        # print "name:", name
        where = house.select(".region")[0].string.encode("utf8")
        # print "where:", where
        if where.find("禅城") != -1 or where.find("佛山") != -1 or where.find("顺德") != -1:
            areaCode = "0757"
        areaCode = areaCode.encode("utf8")
        money = house.select(".num")
        if money:
            money = money[0].string.encode("utf8")
        else:
            money = "unsure"
        # print "money:", money
        content = name + '_￥' + money
        # print "content:", content
        num += 1
        csv_writer.writerow([name, money, content, url, areaCode, ""])

csv_file.close()