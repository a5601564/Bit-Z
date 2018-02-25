#coding:utf-8
"""
打开浏览器
"""

from selenium   import webdriver
from tools.ReadData import ReadData
from setting.Singleton import singletons
from selenium.webdriver.support.wait import WebDriverWait

class   getData():
    url = ReadData().getxml('OpenBrowser_Data.xml','URL',"url")

@singletons
class   openBrowser(object,getData):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get(getData.url)
        self.driver.maximize_window() #最大化窗口
        WebDriverWait(self.driver,20,0.5)
        # self.driver.set_page_load_timeout(20)




