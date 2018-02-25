#coding:utf-8
"""
BTC行情
"""
import  requests
import json
from API.requestDate import GET
class BitcQuo(object):
    def __init__(self):
        self.coins=['bch_btc','eth_btc','gxs_btc','ltc_btc','btx_btc','fct_btc','lsk_btc','nuls_btc','mzc_btc','dash_btc',
               'omg_btc','game_btc','qtum_btc','hsr_btc','xas_btc','pay_btc','voise_btc','ppc_btc','eos_btc',
               'ybct_btc','blk_btc','xpm_btc','bcd_btc','btg_btc','viu_btc','sss_btc','part_btc','doge_btc',
               'dgb_btc','ark_btc','leo_btc','otn_btc']

    #获取卖一价
    def GETSELLFIRST(self,coin=None):
        if  coin == None:
            for coin in self.coins:
                Url="https://www.bit-z.com/api_v1/ticker?coin="+coin
                date=GET(Url)
                __sellfrist=date['data']['sell']  #卖一价
                __SELLF=str(__sellfrist)
                print coin+'-[卖一价]:'+__SELLF
        else:
            Url="https://www.bit-z.com/api_v1/ticker?coin="+coin
            date = GET(Url)
            __sellfrist = date['data']['sell']  # 卖一价
            __SELLF = str(__sellfrist)
            print coin + '[卖一价]:' + __SELLF

    #获取买一价
    def GETBUYFIRST(self):
        for coin in self.coins:
            Url="https://www.bit-z.com/api_v1/ticker?coin="+coin
            date=GET(Url)
            __buyfrist=date['data']['buy']  #卖一价
            __BUYF=str(__buyfrist)
            print coin+'[买一价]:'+__BUYF
