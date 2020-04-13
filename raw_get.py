#!/usr/bin/env python3
# coding:utf8
import re
import time
import requests

session = requests.session()
name = 'Peter'
age = 23

print('%s is %d years old' % (name, age))
print('{} is {} years old'.format(name, age))
#print(f'{name} is {age} years old')

#rn为请求的时间戳。 
#    上证指数：s_sh000001
#    深证成指：s_sz399001
#    创业板指：s_sz399006
t = int(time.time() * 1000)
print(t)

a = '2016-11-04 15:29:58'
t = time.mktime(time.strptime(a, "%Y-%m-%d %H:%M:%S"))

def stock_api() -> str:
    #return f"http://hq.sinajs.cn/rn={int(time.time() * 1000)}&list="
    #return "http://hq.sinajs.cn/rn={}&list=".format(int(time.time() * 1000))
    #return "http://hq.sinajs.cn/rn={}&list=".format(1522736353052)
    #return "http://hq.sinajs.cn/rn={}&list=".format(t*1000)
    return "http://web.ifzq.gtimg.cn/appstock/app/hkfqkline/get?_var=kline_dayqfq&param="

headers = {
    "Accept-Encoding": "gzip, deflate, sdch",
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/54.0.2840.100 "
        "Safari/537.36"
    ),
}
params= '00001'
print(stock_api())
r = session.get(stock_api() + params, headers=headers)
print(r.text)
