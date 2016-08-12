#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib 

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

url="http://cpquery.sipo.gov.cn/txnQueryBibliographicData.do?select-key:shenqingh=2014107120466"
html = getHtml(url)

soup = BeautifulSoup(html)
print soup.find_all('td') 