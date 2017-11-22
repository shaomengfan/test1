# -*- coding:utf-8 -*-  
import urllib2  
import re  
  
  
class QIUSHI(object):  
    def __init__(self):  
        self.page = 1  
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
        self.headers = {'User-Agent': self.user_agent}  
        self.stories = []  
        self.enable = False  
  
    def get_page(self, page):  
        try:  
            url = 'http://www.qiushibaike.com/hot/page/' + str(page)  
            request = urllib2.Request(url, headers=self.headers)  
            response = urllib2.urlopen(request)  
            page_code = response.read().decode('utf-8')  
            return page_code  
        except urllib2.URLError, e:  
            if hasattr(e, "code"):  
                print e.code  
            if hasattr(e, "reason"):  
                print e.reason  
            return None  
  
    def get_stories(self, page):  
        page_stories = []  
        page_content = self.get_page(page)  
        if not page_content:  
            print u'页面加载失败...'  
            return None  
        pattern = re.compile(r'<div.*?author.*?<h2>(.*?)</h2>.*?<div.*?>' +  
                             '(.*?)</div>.*?<i.*?>(\d*?)</i>.*?' +  
                             '<i.*?>(\d*?)</i>', re.S)  
        items = re.findall(pattern, page_content)  
        for item in items:  
            replaceBR = re.compile(r'<br/>')  
            text = re.sub(replaceBR, '\n', item[1])  
            page_stories.append([item[0], text, item[2], item[3]])  
        return page_stories  
  
    def load_page(self):  
        if len(self.stories) < 2:  
            page_stories = self.get_stories(self.page)  
            if page_stories:  
                self.stories.append(page_stories)  
                self.page += 1  
  
    def get_one_story(self, page_stories, nowpage):  
        print u'输入回车获得段子，Q表示退出'  
        for item in page_stories:  
            recive = raw_input('')  
            self.load_page()  
            if recive == 'Q':  
                self.enable = False  
                return  
            print '-' * 25  
            print u'第%s页  作者：%s%s\n好笑：%s  评论：%s\n' % \
                  (nowpage, item[0], item[1], item[2], item[3])  
  
    def start(self):  
        self.enable = True  
        self.load_page()  
        nowpage = 0  
        while self.enable:  
            page_stories = self.stories.pop(0)  
            nowpage += 1  
            self.get_one_story(page_stories, nowpage)  
  
spider = QIUSHI()  
spider.start()  
