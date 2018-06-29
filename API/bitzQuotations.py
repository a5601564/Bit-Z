#coding:utf-8
"""
BTC行情
"""
import  requests
import json
from API.requestDate import GET
class BitcQuo(object):
    def __init__(self):
        self.coins=['btc_usdt']

    #获取卖一价
    def GETSELLFIRST(self,coin=None):
        if  coin == None:
            for coin in self.coins:
                Url="https://www.bit-z.com/api_v1/ticker?coin="+coin
                date=GET(Url)
                __sellfrist=date['data']['sell']  #卖一价
                __SELLF=str(__sellfrist)
                print( coin+'-[卖一价]:'+__SELLF)
        else:
            Url="https://www.bit-z.com/api_v1/ticker?coin="+coin
            date = GET(Url)
            __sellfrist = date['data']['sell']  # 卖一价
            __SELLF = str(__sellfrist)
            print( coin+'-[卖一价]:'+__SELLF)

    #获取买一价
    def GETBUYFIRST(self):
        for coin in self.coins:
            GET('https://api.bit-z.com/api_v1/tickerall')
            Url="https://www.bit-z.com/api_v1/ticker?coin="+coin
            date=GET(Url)
            __buyfrist=date['data']['buy']  #卖一价
            __BUYF=str(__buyfrist)
            print( coin+'[买一价]:'+__BUYF)


bitcQuo=BitcQuo().GETBUYFIRST()

