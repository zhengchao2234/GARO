# -*- coding: cp936 -*-
#�ҳ����굱ǰҳ���������鼮
from bs4 import BeautifulSoup
from urllib2 import urlopen
html=urlopen('https://book.douban.com/tag/%E5%8E%86%E5%8F%B2')
book=BeautifulSoup(html,"html5lib")
for each in book.findAll('div'):      #��Ϣ����div��               
    if each.findChild(class_='star clearfix'):  #�����Ǽ���ĳ��div�ӱ�ǩ�£��ҵ����иñ�ǩ��div
        a=each.findChild(class_='star clearfix') 
        if a.findChild('span',class_='allstar50'):
            print each.h2.get_text(strip=True)
    
   
