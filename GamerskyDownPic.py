# -*- coding=utf-8 -*-
from bs4 import BeautifulSoup
import requests
import urllib
import sitecustomize
import os


os.popen('CHCP 65001')
base_url=raw_input(unicode("请输入第一页网址：\n"))
print unicode("请输入页码：\n")
pageNum=input()
urlList=range(1,pageNum+1)
print unicode("请稍后")
x=0
for no in urlList:
    if no==1:
        url=str(base_url)
    else:
        url=base_url[:len(base_url)-6]+'_'+str(no)+'.shtml'
    wb_data=requests.get(url)
    soup=BeautifulSoup(wb_data.text,'lxml')
    imgsList=soup.select('body > div.Mid > div.Mid2 > div.Mid2_L > div.Mid2L_ctt.block > div.Mid2L_con > p > a')
    
    for img_s in imgsList:
        index=img_s.get('href').find('?')
        true_url=img_s.get('href')[index+1:]
        urllib.urlretrieve(true_url,'D:\\TestData\\Girl\\'+str(x)+'.jpg')
        x+=1
print "下载完成！共有"+str(x)+"个图片已下载！"

