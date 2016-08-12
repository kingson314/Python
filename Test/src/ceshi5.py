#-*-coding:utf-8-*- 
'''
@author: huangwenbin
'''
import urllib2 
from urllib import urlencode

url="http://cpquery.sipo.gov.cn/txnQueryJsbgDetail.do"
addheaders = {'Accept':'*/*',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-CN,zh;q=0.8',
'Connection':'keep-alive',
'Host':'www.cpes-sipo.net',
'Cookie':'GFAsession=cpes; GFA_nav1=1%3dopen%262%3dbuttons%263%3dright%264%3dclosed%265%3dbe67b7cb%26eoc; JSESSIONID=AD58E9D5F00E8D33EDD11721D924C710; GFAsession=cpes+be67b7cc_574080788ee839fd16b30ee23396ff7d',
'Referer':'https://www.cpes-sipo.net/txnCaseListPage.do',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
'X-Requested-With':'XMLHttpRequest'}

data={'select-key:rid':'102008404697',
      'select-key:shenqingh':'2014107120466'}
postdata=urlencode(data)
req=urllib2.Request(url,postdata,addheaders)
html=urllib2.urlopen(req).read()
print html