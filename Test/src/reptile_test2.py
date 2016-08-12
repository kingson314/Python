#-*-coding:utf-8-*-    
import urllib2  
import random  
from wsgiref.headers import Headers
import cookielib
import socket
from test.test_inspect import attrs_wo_objs
from sgmllib import SGMLParser
from HTMLParser import HTMLParser
import time 
from bs4 import BeautifulSoup
from bs4.builder import HTML
import re
import codecs    #这个模块可以实现。
from asyncore import write
import MySQLdb
import os 

#首页   
#url="http://www.court.gov.cn/wenshu.html"  
#下一页 
url="http://cpquery.sipo.gov.cn/txnQueryJsbgDetail.do?select-key:rid=102008404697&select-key:shenqingh=2014107120466"
#url="http://wenshu.court.gov.cn/List/ListContent"
#详细
#url="http://www.court.gov.cn/wenshu/xiangqing-11268.html" ?page=74   

  
my_headers=["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",  
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",  
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"  
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",  
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"       
] 

user_agents = [
'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
'Opera/9.25 (Windows NT 5.1; U; en)',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",
]      

#count=requests.get(url).content

#cj=cookielib.CookieJar()
#opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#urllib2.install_opener(opener)
#agent = random.choice(user_agents)
#opener.addheaders = [("User-agent",agent),("Accept","*/*"),('Referer',url)]
addheaders = {('Accept','*/*'),
('Accept-Encoding','gzip, deflate, sdch'),
('Accept-Language','zh-CN,zh;q=0.8'),
('Connection','keep-alive'),
#('Content-Length','153'),
#('Content-Type','application/x-www-form-urlencoded; charset=UTF-8'),
('Host','www.cpes-sipo.net'),
('Cookie','GFAsession=cpes; GFA_nav1=1%3dopen%262%3dbuttons%263%3dright%264%3dclosed%265%3dbe67b7cb%26eoc; JSESSIONID=AD58E9D5F00E8D33EDD11721D924C710; GFAsession=cpes+be67b7cc_574080788ee839fd16b30ee23396ff7d'),
('Referer','https://www.cpes-sipo.net/txnCaseListPage.do'),
('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'),
('X-Requested-With','XMLHttpRequest')}
Response3=urllib2.urlopen(url)

print Response3.read() 

            