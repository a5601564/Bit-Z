#coding:utf-8

"""
首页
"""

from setting.OpenBrowser  import openBrowser
from tools.ReadData import ReadData
from CommonLibraryApproach.ElementsIde import ElementsIde
from selenium.webdriver.support.ui import WebDriverWait

class   HomeData():
    slideshow_1     =   ReadData().getxml("Home_Data.xml","slideshow","slideshow_01")
    slideshow_2     =   ReadData().getxml("Home_Data.xml","slideshow","slideshow_02")
    currency_1      =   ReadData().getxml("Home_Data.xml","currency","currency_01")
    currency_2      =   ReadData().getxml("Home_Data.xml","currency","currency_02")
    trade_BTC_name  =   ReadData().getxml("Home_Data.xml","currency","trade_btc_name")  #场外交易
    trade_BTC_value =   ReadData().getxml("Home_Data.xml","currency","trade_btc_value") #场外交易最高价
    currency_data   =   ReadData().getxml("Home_Data.xml","currency","hq_item_title")   #最新币种信息
    price_new       =   ReadData().getxml("Home_Data.xml","currency","price_new")   #币种最新价格
    mzc_curData     =   ReadData().getxml("Home_Data.xml","currency","mzc_data")    #mzc信息名字
    mzc_price       =   ReadData().getxml("Home_Data.xml","currency","mzc_price")   #mzc币种价格
    btcTrade_button =   ReadData().getxml("Home_Data.xml","currency","BTC_tap")     #首页BTC场外交易按钮
    act_Trade_Page  =   ReadData().getxml("Trade_BTC_Page.xml","My_order","act_my_order")  #获取场外交易页面数据  My Order
    curr1_NewPrice  =   ReadData().getxml("Home_Data.xml","currency","curr1_NewPrice")  #点击首页中间币种1，实现页面跳转
    curr2_NewPrice  =   ReadData().getxml("Home_Data.xml","currency","curr2_NewPrice")


class   HomePage(HomeData):

    def __init__(self):
         self.driver = openBrowser().driver

    #轮播图
    def slideshow(self):
        ElementsIde().elementXpath(HomeData().slideshow_1).click()
        try:
            ElementsIde().elementXpath(HomeData().slideshow_1).click()
        except Exception:
            print "没有找到轮播图1!"
        try:
            ElementsIde().elementXpath(HomeData().slideshow_2).click()
        except  Exception:
            print "没有找到轮播图2!"

    #获取场外交易BTC最新价格
    def get_trade_BTCCurrency(self):
        try:
            __currencyNew   =   ElementsIde().elementXpath(HomeData().trade_BTC_name).tex
            __curNewNum     =   ElementsIde().elementXpath(HomeData.trade_BTC_value).text
            return __currencyNew+__curNewNum
        except  Exception:
            return "获取场外交易BTC最新价失败！"

    #获取涨币最新价格
    def get_AppreCurrency_data(self):
        try:
            __LSKDtat   =   ElementsIde().elementXpath(HomeData().currency_data).text
            __LSKprice  =   ElementsIde().elementXpath(HomeData().price_new).text
            return  __LSKDtat+__LSKprice
        except Exception:
            return "获取涨币最新价格失败！"

    #获取跌币最新价格
    def get_currrncy_data(self):
        try:
            __MZCdata   =   ElementsIde().elementXpath(HomeData().mzc_curData).text
            __MZCprice  =   ElementsIde().elementXpath(HomeData().mzc_price).text
            return __MZCdata+__MZCprice
        except  Exception:
            return "获取跌币最新价格失败！"

    #点击btcTap，页面跳转到场外交易页面
    def click_BTCtap_To_Trade(self):
        try:
            ElementsIde().elementXpath(HomeData().btcTrade_button).click()
            __expect_value =    "My Order"
            ___act_value   =    ElementsIde().elementXpath(HomeData().act_Trade_Page)
            if  __expect_value == ___act_value:
                return "页面跳转到场外交易成功！"
        except  Exception:
            return "页面跳转到场外交易页面失败！"

    # #点击币1最新价格
    # def click_curr1NewPrice(self):
    #     try:
    #         ElementsIde().elementXpath()




if  __name__=="__main__":
    HomePage().slideshow()






