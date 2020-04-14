#!/usr/bin/env python3
# coding:utf8
import re
import time
import requests
import json

session = requests.session()
name = 'Peter'
age = 23

print('%s is %d years old' % (name, age))
print('{} is {} years old'.format(name, age))
#print(f'{name} is {age} years old') #python3.6

#rn为请求的时间戳。 
#    上证指数：s_sh000001
#    深证成指：s_sz399001
#    创业板指：s_sz399006

#t = int(time.time() * 1000)
#print(t)


#http://img1.money.126.net/data/hs/kline/day/history/2020/0000001.json

def stock_api() -> str:
    a = '2016-11-04 15:29:58'
    t = time.mktime(time.strptime(a, "%Y-%m-%d %H:%M:%S")) #time string to time

    #return f"http://hq.sinajs.cn/rn={int(time.time() * 1000)}&list="
    #return "http://hq.sinajs.cn/rn={}&list=".format(int(time.time() * 1000))
    #return "http://hq.sinajs.cn/rn={}&list=".format(1522736353052)
    #return "http://hq.sinajs.cn/rn={}&list=".format(t*1000)
    return "http://web.ifzq.gtimg.cn/appstock/app/hkfqkline/get?_var=kline_dayqfq&param="

def url_126(year=2020,code='0000001') -> str:
    return "http://img1.money.126.net/data/hs/kline/day/history/{}/{}.json".format(year,code)

def url_sohu(code=cn_300228,start=20130930,end=20131231) -> str:
    return "http://q.stock.sohu.com/hisHq?code={}&start={}&end={}&stat=1&order=D&period=d&callback=historySearchHandler&rt=jsonp".format(code,start,end)

headers = {
    "Accept-Encoding": "gzip, deflate, sdch",
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/54.0.2840.100 "
        "Safari/537.36"
    ),
}

def get_resp():
    params= '00001'
    print(stock_api())
    r = session.get(stock_api() + params, headers=headers)
    print(r.text)

def get_json():
    data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
    json_string = json.dumps(data)
    print(json_string,type(json_string))
    jsonx = json.loads(json_string)
    print(jsonx,type(jsonx))

def get_126data(year = 2020,code = '0000001'):
    r = session.get(url_126(year,code), headers=headers)
    print(r.text)
    data = json.loads(r.text)
    return data['data']

def get_sohu_data():
    r = session.get(url_sohu(), headers=headers)

get_data()
