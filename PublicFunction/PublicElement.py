#coding:utf-8

"""
    action:元素识别
"""

from tools.ConnectionMySQL import ConnectionMySQL
from tools.InitBrowser import InitBrowser

class PublicElement(object):

    def __init__(self):
        self.driver = InitBrowser().driver

    def getElement(self,element):
        if  element == 'id':
            self.driver.find_element_by_id()
        elif element == 'class_name':
            self.driver.find_element_by_class_name()
        elif element == 'text':
            self.driver.find_element_by_link_text()
        elif element == 'css':
            self.driver.find_element_by_css_selector()
        elif element == 'name':
            self.driver.find_element_by_name()
        elif element == 'xpath':
            self.driver.find_element_by_xpath()

    def getElements(self,element):
        pass



