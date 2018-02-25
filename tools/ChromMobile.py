#coding:utf-8

"""
使用谷歌浏览器模拟手机适配
"""

from    selenium    import webdriver

class ChromeMobileEmulation():
    def __init__(self):
            self.__mobileEmulation   =   {
                'deviceName':'APPle iPhone 4',
                'deviceMetrics':{
                    'width':'320',   #宽度
                    'height':"640",   #高度
                    "pixelRation":'3.0'     #分辨率
                }
            }
            self.__options   =   webdriver.ChromeOptions()
            self.__options.add_experimental_option("mobileEmulation",self.__mobileEmulation)
            self.driver = webdriver.Chrome(chrome_options=self.__options)
            self.driver.get("")
            self.driver.close()
            """
            'deviceName':'Apple iphone 3GS',
            'deviceName':'Apple iPhone 4',
            'deviceName':'Apple iPhone 5',
            'deviceName':'Apple iPhone 6',
            'deviceName':'Apple iPhone 6 Plus',
            'deviceName':'Blackberry z10',
            'deviceName':'Blackberry z30',
            'deviceName':'Google Nexus 4',
            'deviceName':'Google Nexus 5',
            'deviceName':'Google Nexus s',
            
            """