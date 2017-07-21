# -*- coding: UTF-8 -*-

import MySQLdb
import re #主要包含了正则表达式
import urllib #　Urllib 模块提供了读取web页面数据的接口

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getCountries(html):

    conn = MySQLdb.connect(host='localhost', user='root', passwd='000000', db='python',charset='utf8')
    cursor = conn.cursor()

    reg = r'<a href="(http://place.qyer.com/.*/)" data-bn-ipg="place-index-countrylist-\d+">\r\n +([\s\S]*?) \r\n +<span class="en">([\s\S]*?)<\/span>\r\n +<\/a>'

    countryre = re.compile(reg)#re.compile(pattern[, flags])将reg转化成正则表达式对象
    countrylist = re.findall(countryre,html)
    for country in countrylist:
        link = country[0];
        name = country[1];
        enname = country[2];

#        print link; print name; print enname;
        sql_select = "select * from Country where country_name = '%s'" % (name)

        sql_insert = "insert into Country(country_name,country_en, country_url) values('%s', '%s', '%s')" % (name, enname, link)
        try:
            cursor.execute(sql_select)
            if cursor.rowcount == 0:
            
                sql_value = False
                cursor.execute(sql_insert)

            else:
                sql_value = True
        
            print sql_value

            conn.commit()

        except Exception as e:
            conn.rollback()
            raise e

    cursor.close();
    conn.close();

city = getHtml("http://place.qyer.com")
getCountries(city)

