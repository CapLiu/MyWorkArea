# coding=utf-8
from selenium import webdriver
import time,datetime
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ErrorInResponseException
from selenium.common.exceptions import NoSuchElementException
from matplotlib import pyplot as pl
CHROMEDRIVER_PATH='D:\\WebDrivers\\chromedriver_win32\\chromedriver.exe'
PHANTOMJS_PATH='D:\\WebDrivers\\phantomjs\\bin\\phantomjs.exe'
time_axis=[9,10,11,12,13,14,15,16]
tempture_axis=[27,27,26,28,30,30,30,28]
def GetWeatherData():
    global time_axis,tempture_axis
    url='http://www.weather.com.cn/weather1d/101010100.shtml'
    driver=webdriver.PhantomJS(executable_path=PHANTOMJS_PATH)
    driver.get(url)
    time.sleep(3)
    try:
        temperture=driver.find_element_by_xpath('//*[@id="today"]/div[1]/div/div[4]/span').text
    except NoSuchElementException,e:
        time.sleep(10)
        driver.refresh()
        time.sleep(3)
        temperture = driver.find_element_by_xpath('//*[@id="today"]/div[1]/div/div[4]/span').text
    h=str(datetime.datetime.now()).split(':')[0].split(' ')[1]
    time_axis.append(int(h))
    print time_axis
    print temperture
    tempture_axis.append(temperture)
    driver.close()
def GetGraph():
    global time_axis,tempture_axis
    pl.xlabel('时间',fontproperties='SimHei')
    pl.ylabel('温度('+u'\u2103'+')',fontproperties='SimHei')
    pl.plot(time_axis,tempture_axis,'ro-',lw=2.5)
    pl.xlim(7.0,18.0)
    pl.ylim(20.0,40.0)
    for i in range(0,len(time_axis)):
        pl.text(int(time_axis[i]),tempture_axis[i],str(tempture_axis[i]))
    date_time=str(datetime.datetime.now()).split(':')[0].split(':')[0]
    pl.savefig(date_time+'.png')
    print '图表绘制完毕！'


if __name__=="__main__":
    print datetime.datetime.now()
    try:
        while True:
            try:
                GetWeatherData()
            except TimeoutException,e:
                print e
                GetWeatherData()
            if len(tempture_axis)==9:
                break
            time.sleep(3600)
    except TimeoutException,e:
        print e
        time.sleep(30)
        GetWeatherData()
    except ErrorInResponseException,e1:
        print e1
    finally:
        GetGraph()
