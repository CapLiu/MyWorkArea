# -*- coding=utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time

CHROMEDRIVER_PATH='D:\\WebDrivers\\chromedriver_win32\\chromedriver.exe'
PHANTOMJS_PATH='D:\\WebDrivers\\phantomjs\\bin\\phantomjs.exe'
class NovelSpider():
    url=""
    driver=None
    content=""
    chapter_title=""
    novel_file=None
    def __init__(self):
        self.url="http://www.kanunu8.com/book4/10613/"
        self.driver=webdriver.PhantomJS(executable_path=PHANTOMJS_PATH)
        self.novel_file=open('novel.txt','a')
    def GetContent(self):
        print "请稍后……"
        for page in range(187164,187226):
            temp_url=self.url+str(page)+".html"
            time.sleep(0.5)
            self.driver.get(temp_url)
            self.chapter_title=self.driver.find_element_by_tag_name('h2').text
            print "正在获取"+self.chapter_title+"的内容……"
            self.content=self.driver.find_element_by_tag_name('p').text
            self.novel_file.write('\n'+self.chapter_title+'\n')
            self.novel_file.write(self.content)
        print "小说内容已存储在novel.txt文件中。"
        self.driver.close()

if __name__=="__main__":
    spider=NovelSpider()
    spider.GetContent()
    exit()