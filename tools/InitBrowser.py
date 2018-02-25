#coding:utf-8
"""
    action：初始化浏览器
"""
from setting.Singleton import singletons
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@singletons
class InitBrowser(object):
    def __init__(self,url=None,browser=None):
        if browser == None or browser == "Firefox" or browser == "火狐":
            self.driver = webdriver.Firefox()
            self.driver.get(url=url)
            self.driver.maximize_window()
            WebDriverWait(self.driver, 20, 0.5)
        elif browser == "Chrome" or browser == "谷歌" or browser == "chrome":
            self.driver = webdriver.Chrome()
            self.driver.get(url=url)
            self.driver.maximize_window()
            WebDriverWait(self.driver, 20, 0.5)

