# -*- coding: UTF-8 -*-
import urllib2
import urllib
import re
headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
url = 'http://www.xxsy.net/chapter/7887125.html'
url2='http://www.xxsy.net/chapter/7887126.html'
try:
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    html = response.read().decode('UTF-8')
    html = html.replace('<p>','    ')
    html = html.replace('    ','\n')
    html = html.replace('</p>','\n')
except urllib2.URLError, e:
    if hasattr(e,"code"):
       print e.code
    if hasattr(e,"reason"):
       print e.reason
content_pattern = re.compile('div class="chapter-main".*?>(.*?)</div>',re.S)
content_list = re.findall(content_pattern, html)
for item in content_list:
    print item
    
    print u'正在读取，回车查看'
    input = raw_input()

try:
    request = urllib2.Request(url2,headers=headers)
    response = urllib2.urlopen(request)
    html = response.read().decode('UTF-8')
    html = html.replace('<p>','    ')
    html = html.replace('    ','\n')
    html = html.replace('</p>','\n')
except urllib2.URLError, e:
    if hasattr(e,"code"):
       print e.code
    if hasattr(e,"reason"):
       print e.reason
content_pattern = re.compile('div class="chapter-main".*?>(.*?)</div>',re.S)
content_list = re.findall(content_pattern, html)
for item in content_list:
    print item


