#coding:utf-8

from    setting.OpenBrowser import openBrowser
from    CommonLibraryApproach.ElementsIde import ElementsIde
class   CurrencyTrade():
    def __init__(self):
        self.driver =   openBrowser().driver

    def currency(self,currency):
        if  currency    ==  "":
            pass
        elif    currency    ==  "":
            pass
        elif    currency    ==  "":
            pass


class   CurrencyTradeValue():
    #最新交易动态
    def fl(self):
        try:
            __currencyDynamic   =   ElementsIde().elementXpath(".//*[@id='trendsCon']/div/div[1]").text
            return  __currencyDynamic
        except  Exception:
            return ("获取'币种'最新交易动态失败!")

    #最新价
    def NewPrice(self):
        try:
            __newPrice          =   ElementsIde().elementXpath(".//*[@id='trendsCon']/div/div[2]").text
            return  __newPrice
        except  Exception:
            return "获取最新价失败！"

    #最高价
    def HighPrice(self):
        try:
            __highprice         =   ElementsIde().elementXpath(".//*[@id='trendsCon']/div/div[3]").text
            return __highprice
        except  Exception:
            return "获取最高价失败！"

    #最低价
    def LowPrice(self):
        try:
            __lowPrice          =   ElementsIde().elementXpath(".//*[@id='trendsCon']/div/div[4]").text
            return  __lowPrice
        except  Exception:
            return "获取最低价失败！"

    #涨跌幅
    def chg(self):
        try:
            __chg               =   ElementsIde().elementXpath(".//*[@id='trendsCon']/div/div[5]").text
            return __chg
        except  Exception:
            return  "获取币种涨跌幅失败！"

    #24小时成交量
    def tradeNum(self):
        try:
            __tradeNum          =   ElementsIde().elementXpath(".//*[@id='trendsCon']/div/div[6]").text
            return __tradeNum
        except  Exception:
            return "获取24小时成交量失败！"

    #获取卖单列表
    def saleList(self):
        try:
            __salelist  =   ElementsIde().elementID("salelist").text
            return __salelist
        except  Exception:
            return "获取卖单列表失败！"

    # #获取买单列表
    # def
