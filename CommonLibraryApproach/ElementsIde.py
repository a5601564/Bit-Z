#coding:utf-8

from API.APIMode import Bit_ZAPI
import time
path='/api_v1/tradeAdd'
secret ='a5ccc6b23756d49229844de248b2839c'
params = {}
params['api_key'] = '425c89d5d669ea4de9e20379604505e6'
params['timestamp'] = str(int(time.time()))
params['nonce'] = str(int(time.time() % 1000000))
# params['coin'] = str('atm_btc')
params['type'] = str('out')
params['price'] = str('0.00000734')
params['number'] = str('10')
params['coin'] = str('pok_btc')
params['tradepwd'] = str('qwerqwer')

print Bit_ZAPI().signature(Path=path,Secret=secret,Params=params)