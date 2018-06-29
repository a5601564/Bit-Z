import time

import hashlib
import requests
s = requests.session()
s.keep_alive = False
url = 'https://www.bit-z.com/api_v1/openOrders'
APIKey = "3923924c4007a3a995e3cf03548ef9de"
Secret = "c762ae4415a56d892ab5c4f58724e87b"
params = {}
params['api_key'] = APIKey
params['timestamp'] = str(int(time.time()))
params['nonce'] = str(int(time.time() % 1000000))

params['coin'] = str('atm_btc')

iniSign = ''
list=[]
for key in sorted(params.keys()):
    iniSign += key + '=' + str(params[key])+'&'
    signs = iniSign[:-1]
    list.append(signs)
sign = list[-1]
data = sign + Secret


params['sign'] = hashlib.md5(data.encode("utf8")).hexdigest().lower()
reValue = requests.post(url,params,timeout=30)
print( url,params)
print(reValue.json())