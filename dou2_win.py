# coding=cp936   

import urllib
import urllib2
import re
import time
import sys
import os


reload(sys)
sys.setdefaultencoding('utf-8')

print '#'*50
print '��������Ҫ�ɼ�����<�벻Ҫ����>С���ͼƬ'
print '#'*50
print '�ɼ�ǰ��Ҫ��������������ַ���������Է�ֹ����������.'
print '�Ƽ�һ�������ַ: http://cn-proxy.com/'
print 'ֻ��Ҫ�����������ַ�Լ��˿ںţ�����Ҫ����http'
print '����:127.0.0.1:8080'
print '#'*50
print 'By ���鹫��'
print '#'*50

proxy_input = raw_input("������ɼ����������:")
proxy_handler = urllib2.ProxyHandler({'http':'%s'%proxy_input})
opener = urllib2.build_opener(proxy_handler)
urllib2.install_opener(opener)

img_LuJ = raw_input("ͼƬ����·��:")
img_LuJ2 = os.path.abspath(img_LuJ)

def gethtml2(url2):
    html2 = urllib2.urlopen(url2).read().decode('utf-8')
    return  html2

def gettoimg(html2):
    reg2 = r'http://www.douban.com/group/topic/\d+'
    toplist = re.findall(reg2,html2)
    x = 0
    for topicurl in toplist:
        x+=1
    return topicurl

def download(topic_page):
    reg3 = r'http://img3.douban.com/view/group_topic/large/public/.+\.jpg'
    imglist = re.findall(reg3,topic_page)
    i = 1
    download_img = None
    for imgurl in imglist:
        img_numlist = re.findall(r'p\d{7}',imgurl)
        for img_num in img_numlist:
            download_img = urllib.urlretrieve(imgurl,img_LuJ2 + '/%s.jpg'%img_num)
            time.sleep(1)
            i+=1
            print (imgurl)
    return download_img

page_end = int(input('������ɼ�ҳ����:'))
num_end = page_end*25
num = 0
page_num = 1
while num<=num_end:
    html2 = gethtml2('http://www.douban.com/group/haixiuzu/discussion?start=%d'%num)
    topicurl = gettoimg(html2)
    topic_page = gethtml2(topicurl)
    download_img=download(topic_page)
    num = page_num*25
    page_num+=1

else:
    print("����ɼ����")
