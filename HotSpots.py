#!Users/HXL/Desktop
#-*- coding: UTF-8 -*-
'''
import re #主要包含了正则表达式
import urllib2
import os
import sys
import random
import string
import  shelve #读写



_metaclass_ = type

class Person:
    def setName(setName,name):
        setName.name = name

    def getName(self):
        return self,name

    def greet(self):
        print "Hello,world! I'm %s" %self.name

huhu = Person()
huhu.setName('liming')
huhu.greet()

'''
'''
name = os.getlogin()
print "neme is",name

paths = sys.path
for path in paths:
    print "path :",path
print "\n"

modules = sys.modules
for module in modules:
    print "module :",module
print "\n"
'''
#help()
'''
#生成随机验证码
checkcode=''
for i in range(5):
    current = random.randrange(0,5)
    if current == i:
        tmp = chr(random.randint(65,90))#chr是ascii码表,65,90是（A-Z）
    else:
        tmp = random.randint(0,9)
    checkcode +=str(tmp)
print(checkcode)

print(''.join(random.sample(string.ascii_lowercase+string.digits,5)))#随机验证码可用（5位含数字和密码）

#打印a-z
print(string.ascii_lowercase)#一
#打印A-Z
print(string.ascii_letters)#二


#读写
d = shelve.open('shelve_test')
    #写
sname = {"zhangsan","lisi","wanger"}
sinfo = {"age":25,"job":"IT"}
d["name"]  = sname
d["info"] = sinfo
d.close()
#写完以后，它会自动生成三个文件，.dat和.dir和.bak

#读
print(d.get("sname"))
print(d.get("sinfo"))


'''
'''
url="http://www.163.com" #网页地址
wp=urllib.urlopen(url) #打开连接
content=wp.read() #获取页面内容
wordList = re.findall(re.compile(word), html) #正则findall 查找所有的单词
print len(wordList) #个数
'''

'''
import urllib2 #　Urllib 模块提供了读取web页面数据的接口
import httplib2
from lxml import etree

def main():
    
    http = httplib2.Http()
    response,content = http.request("http://www.baidu.com",'GET')
    print "response:",response
    print "content:",content
    tree = etree.HTML(content)

    hyperlinks = tree.xpath(u'//p[@id="nv"]/a/@href')
    print "hyperlinks:",hyperlinks
    for hyperlink in hyperlinks:
        print "hyperlink:",hyperlink

    a_nodes = tree.xpath(u'//p[@id="nv"]/a')
    print "a_nodes_length:",len(a_nodes)
    for a_node in a_nodes:
        print "<a>",a_node.text,a_node.attrib['href']
    print "\n"

    name_flag='<p id="nv">(.+?)</p>'
    name_re=re.compile(name_flag, re.S)
    name_regx=name_re.search(content)
    print name_regx
    name=name_regx.group(1)
    print "name:",name

if __name__ == "__main__":
    main()
'''

'''
import urllib2

req = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(req)
the_page = response.read()
print the_page
'''

'''
    #post提交表单
import urllib
import urllib2

url = "http://www.someserver.com/register.cgi"
values = {'name' : 'WHY',
    'location' : 'SDU',
    'language' : 'Python'}
data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()
'''

'''
#get传送数据
import urllib2
import urllib

data = {}
data['name'] = 'WHY'
data['location'] = 'SDU'
data['language'] = 'Python'
url_values = urllib.urlencode(data)
print url_values
name = someBody+Here&language=Python&location=Northampton
url = 'http://www.example.com/example.cgi'
full_url = url + '?' + url_values
data = urllib2.open(full_url)
'''

'''
#header头请求
import urllib
import urllib2
url = 'http://www.someserver.com/cgi-bin/register.cgi'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'name' : 'WHY',
'location' : 'SDU',
'language' : 'Python' }
headers = { 'User-Agent' : user_agent }
data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
the_page = response.read()
'''

'''
import urllib2
from sgmllib import SGMLParser

class ListName(SGMLParser):
    def __init__(self):
        SGMLParser.__init__(self)
        self.is_a = ""
        self.name = []
    def start_a(self, attrs):
        self.is_a = 1
    def end_a(self):
        self.is_a = ""
    def handle_data(self, text):
        if self.is_a == 1:
            self.name.append(text)

content = urllib2.urlopen('http://list.taobao.com/browse/cat-0.htm').read()

listname = ListName()
listname.feed(content)
#for item in listname.name:
#    print item.decode('gbk').encode('utf8')
for item in listname.name:
    print "item:",item

'''

'''
import urllib2
import datetime
from sgmllib import SGMLParser

class GetIdList(SGMLParser):
    def reset(self):
        self.IDlist = []
        self.flag = False
        self.getdata = False
        self.verbatim = 0
        SGMLParser.reset(self)

    def start_ul(self, attrs):
        if self.flag == True:
            self.verbatim += 1
            return
        for k,v in attrs:
            if k == 'class' and v == 'cityList clearfix':
                self.flag = True
                return

    def end_ul(self):
        if self.verbatim == 0:
            self.flag = False
        if self.flag == True:
            self.verbatim -= 1

    def start_li(self,attrs):
        if self.flag == False:
            return
        self.getdata = True

    def end_li(self):
        if self.getdata:
            self.getdata = False

    def handle_data(self, text):
        if self.flag:
            self.IDlist.append(text)

    def printID(self):
        for i in self.IDlist:
            print i

strUrl = 'http://place.qyer.com/thailand/citylist-0-0-1/'
req = urllib2.Request(strUrl)#通过网络获取网页
response = urllib2.urlopen(req)
the_page = response.read()

lister = GetIdList()
lister.feed(the_page)
lister.printID()
'''

#抓取列车表http://blog.csdn.net/baalhuo/article/details/51987202
from html.parser import HTMLParser
import re
import urllib.request

liststr = list()

class MyHTMLParser(HTMLParser):
    tempstr = str()
    def handle_starttag(self, tag, attrs):
        if tag == 'tr':
            self.tempstr = ''

    def handle_endtag(self, tag):
        if tag == 'tr':
            matchObj = re.match(r'G|D|K|T|Z\d',self.tempstr)
            if matchObj:
                liststr.append(self.tempstr)

    def handle_data(self, data):
        if data.isspace() == False:
            self.tempstr += data + '\t'


url = 'http://qq.ip138.com/train/anhui/HeFei.htm'
data = urllib.request.urlopen(url).read()
data = data.decode('gb2312') #根据抓取页面设置数据编码
par = MyHTMLParser()
par.feed(data)
for value in liststr:
    print(value)
print(liststr.__len__())
