#coding:utf-8
"""
    action:撮单
"""

from    decimal import *

class TrustCoin(object):
    getcontext().prec = 8
    def __init__(self,from_coin_name,to_coin_name,buy_price,buy_number,buy_change,sell_price,sell_number,sell_change):
        self.from_coin_name = from_coin_name
        self.to_coin_name = to_coin_name
        self.bprice = Decimal(buy_price)
        self.bnum = Decimal(buy_number)
        self.bchange = Decimal(buy_change)
        self.sprice = Decimal(sell_price)
        self.snum = Decimal(sell_number)
        self.schange = Decimal(sell_change)

    def fromBuy_ToSell(self):
        if  self.bprice >= self.sprice:
            if  self.bnum > self.snum:
                # 买家扣除手续费
                __buy_change = self.snum * self.bchange
                #买家实际得到数量
                __buy_get_over = self.snum - __buy_change
                #买家冻结
                __buy_get_lock = self.bnum - self.snum
                #币成交量
                __turn_coin_num = self.snum * self.bprice
                #卖手续费
                __sell_change = __turn_coin_num * self.schange
                #卖家实际得到
                __sell_get_over = __turn_coin_num - __sell_change

                return {'代币成交量':self.snum+self.to_coin_name,
                        '买家扣除代币手续费':__buy_change+self.to_coin_name,
                        '买家获得代币数量':__buy_get_over+self.to_coin_name,
                        '买家冻结代币数量':__buy_get_lock+self.to_coin_name,
                        '成交量':__turn_coin_num+self.from_coin_name,
                        '卖家手续费':__sell_change+self.from_coin_name,
                        '卖家获得币种数量':__sell_get_over+self.from_coin_name}
            elif   self.bnum == self.snum:
                # 买家扣除手续费
                __buy_change = self.bnum * self.bchange
                # 买家实际得到数量
                __buy_get_over = self.bnum - __buy_change
                # 币成交量
                __turn_coin_num = self.bnum * self.bprice
                # 卖手续费
                __sell_change = __turn_coin_num * self.schange
                # 卖家实际得到
                __sell_get_over = __turn_coin_num - __sell_change

                return {'法币成交量': self.bnum + self.to_coin_name,
                        '买家扣除法币手续费': __buy_change + self.to_coin_name,
                        '买家获得法币数量': __buy_get_over + self.to_coin_name,
                        '代币成交量': __turn_coin_num + self.from_coin_name,
                        '卖家手续费': __sell_change + self.from_coin_name,
                        '卖家获得代币数量': __sell_get_over + self.from_coin_name}
            elif   self.bnum < self.snum:
                # 买家扣除手续费
                __buy_change = self.bnum * self.bchange
                # 买家实际得到数量
                __buy_get_over = self.bnum - __buy_change
                # 币成交量
                __turn_coin_num = self.bnum * self.bprice
                # 卖手续费
                __sell_change = __turn_coin_num * self.schange
                # 卖家实际得到
                __sell_get_over = __turn_coin_num - __sell_change
                # 卖家冻结
                __sell_get_lock = (self.snum - self.bnum)*self.sprice
                return {'法币成交量': self.bnum + self.to_coin_name,
                        '买家扣除法币手续费': __buy_change + self.to_coin_name,
                        '买家获得法币数量': __buy_get_over + self.to_coin_name,
                        '代币成交量': __turn_coin_num + self.from_coin_name,
                        '卖家手续费': __sell_change + self.from_coin_name,
                        '卖家获得代币数量': __sell_get_over + self.from_coin_name,
                        '卖家冻结代币数量':__sell_get_lock+self.from_coin_name}
        elif  self.bchange < self.sprice:
            return "不成交！！！"

    def fromsell_tobuy(self):
        if  self.sprice <= self.bprice:
            if  self.snum <= self.bnum:
                #成交量
                __turn_coin_num = self.snum * self.sprice
                #卖家手续费
                __sell_change = __turn_coin_num * self.schange
                #卖家实际得到数量
                __sell_get_over = __turn_coin_num - __sell_change
                #买家手续费
                __buy_change = self.snum * self.bprice
                #买家实际得到数量
                __buy_get_over = self.snum - __buy_change
                #买家返还数量
                __buy_re_num = (self.bprice - self.sprice)*self.snum
                #买家冻结代币数量
                __buy_get_lock = (self.bnum - self.snum) * self.bprice
                return {
                        '代币成交量': __turn_coin_num + self.from_coin_name,
                        '卖家手续费': __sell_change + self.from_coin_name,
                        '卖家获得币种数量': __sell_get_over + self.from_coin_name,
                        '法币成交量': self.bnum + self.to_coin_name,
                        '买家扣除法币手续费': __buy_change + self.to_coin_name,
                        '买家获得法币数量': __buy_get_over + self.to_coin_name,
                        '买家返还的法币数量':__buy_re_num + self.to_coin_name,
                        '买家冻结代币的数量':__buy_get_lock + self.to_coin_name
                }
            elif self.snum > self.bnum:
                #成交量
                __turn_coin_num = self.bnum * self.sprice
                #卖家代币手续费
                __sell_change = __turn_coin_num * self.schange
                #卖家实际收入代币数量
                __sell_get_over = __turn_coin_num - __sell_change
                #卖家的冻结法币的数量
                __sell_get_lock = self.snum - self.bnum
                #买家法币手续费
                __buy_change = self.bnum * self.bchange
                #买家实际得到法币数量
                __buy_get_over = self.bnum - __buy_change
                # 买家返还数量
                __buy_re_num = (self.bprice - self.sprice) * self.bnum
                return {
                        '代币成交量': __turn_coin_num + self.from_coin_name,
                        '卖家手续费': __sell_change + self.from_coin_name,
                        '卖家获得币种数量': __sell_get_over + self.from_coin_name,
                        '卖家冻结法币数量':__sell_get_lock + self.to_coin_name,
                        '法币成交量': self.bnum + self.to_coin_name,
                        '买家扣除法币手续费': __buy_change + self.to_coin_name,
                        '买家获得法币数量': __buy_get_over + self.to_coin_name,
                        '买家返还的法币数量':__buy_re_num + self.to_coin_name,
                }