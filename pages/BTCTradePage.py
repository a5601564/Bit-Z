#coding:utf-8
"""
btc交易页面
"""
from    setting.OpenBrowser import openBrowser
from    CommonLibraryApproach.ElementsIde import ElementsIde
from    tools.ReadData import ReadData
class   BTC_Data():
    trade_name_text     =   ReadData().getxml("BTC_Page.xml","Text","BtcTitleName")
    trade_name_element  =   ReadData().getxml("BTC_Page.xml","Element","BtcElementText")
    newPrice            =   ReadData().getxml("BTC_Page.xml","Element","newPrice")
    highPrice           =   ReadData().getxml("BTC_Page.xml","Element","highPrice")
    lowPrice            =   ReadData().getxml("BTC_Page.xml","Element","lowPrice")
    chg                 =   ReadData().getxml("BTC_Page.xml","Element","chg")
    tradeNum            =   ReadData().getxml("BTC_Page.xml","Element","tradeNum")
class   BTCTradePage():
    def __init__(self):
        self.driver =   openBrowser().driver

    #BTC页面顶部数据信息展示
    def title(self):
        #...最新交易动态
        try:
            __trade_name_element    =   ElementsIde().elementXpath(BTC_Data().trade_name_element)
            print   __trade_name_element
        except  Exception:
            print "获取比特币（BTC）最新交易动态失败！"
            #最新价
        try:
            __newPrice  =   ElementsIde().elementXpath(BTC_Data().newPrice)
            print   __newPrice
        except  Exception:
            print
            #最高价
            __highPrice =   ElementsIde().elementXpath(BTC_Data().highPrice)
            print   __highPrice


