# -*- coding: cp936 -*-
#找出豆瓣当前页五心评价书籍
from bs4 import BeautifulSoup
from urllib2 import urlopen
html=urlopen('https://book.douban.com/tag/%E5%8E%86%E5%8F%B2')
book=BeautifulSoup(html,"html5lib")
for each in book.findAll('div'):      #信息都在div内               
    if each.findChild(class_='star clearfix'):  #评价星级在某个div子标签下，找到含有该标签的div
        a=each.findChild(class_='star clearfix') 
        if a.findChild('span',class_='allstar50'):
            print each.h2.get_text(strip=True)
    
   
