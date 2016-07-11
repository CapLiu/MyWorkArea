#-*- coding=utf-8 -*-
import urllib,requests,urllib2,cookielib,re,datetime,time


class RenrenSpider:
    rtk=""
    requestToken=""
    headers={}
    file1=""
    starttime=""
    def __init__(self):
        self.headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        }
        try:
            cookie = cookielib.CookieJar()
            cookieProc = urllib2.HTTPCookieProcessor(cookie)
        except:
            raise
        else:
            opener=urllib2.build_opener(cookieProc)
            urllib2.install_opener(opener)

    def Logon(self):
        print 'Loging in……'
        # email = raw_input("请输入用户名：")
        # password = raw_input("请输入密码：")
        domain = 'renren.com'
        url = 'http://www.renren.com/PLogin.do'
        postdata = {
            'email': 'thecaption@21cn.com',
            'password': 'Cu2(OH)2CO3',
            'domain': domain
        }
        req = urllib2.Request(url, urllib.urlencode(postdata), headers=self.headers)
        myfile = urllib2.urlopen(req).read()
        request_pattern = re.compile(r"requestToken : '(-)?(\w)*'")
        rtk_pattern = re.compile(r"_rtk : '(\w)*'")
        requestToken = request_pattern.search(myfile).group(0).split("'")[1]
        rtk = rtk_pattern.search(myfile).group(0).split("'")[1]
        self.requestToken=requestToken
        self.rtk=rtk
        if requestToken=="":
            print "登录失败！"
            exit()
        else:
            print "登录成功！"

    def PublishStatus(self):
        self.starttime = datetime.datetime.now()
        time_cell=str(self.starttime).split(':')
        h=time_cell[0].split(' ')[1]
        m=time_cell[1]
        s=time_cell[2].split('.')[0]
        print h,m,s
        sendstatus_url = 'http://shell.renren.com/327473841/status'
        content=raw_input("请输入要发表的内容：")
        status_headers = {
            'channel': 'renren',
            'content': content +'  此状态发表于 [' +str(h)+':'+str(m)+':'+str(s)+'] ',
            'requestToken': self.requestToken,
            '_rtk': self.rtk
        }
        req=urllib2.Request(sendstatus_url,urllib.urlencode(status_headers))
        self.file1=urllib2.urlopen(req).read()
        print "发表成功！"


if __name__=="__main__":
    spider=RenrenSpider()
    spider.Logon()
    spider.PublishStatus()
    exit()