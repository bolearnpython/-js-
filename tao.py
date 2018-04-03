#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-19 18:44:56
# @Author  : bo (bo17096701774@gmail.com)
# @Link    : https://github.com/bolearnpython
import time
import json
import requests
from scrapy.loader.processors import SelectJmes
url = "http://h5api.m.taobao.com/h5/mtop.taobao.detail.getdetail/6.0/"
time_string = int(time.time() * 1000)
itemId = '560129744052'
querystring = {"jsv": "2.4.3", "appKey": "12574478", "t": time_string, "api": "mtop.taobao.detail.getdetail", "v": "6.0", "ttid": "2016@taobao_h5_2.0.0", "isSec": "0", "ecode": "0", "AntiFlood": "true",
               "AntiCreep": "true", "H5Request": "true", "type": "jsonp", "dataType": "jsonp", "callback": "mtopjsonp1", "data": "{\"exParams\":\"{\\\"id\\\":\\\"560129744052\\\",\"itemNumId\":\"560129744052\"}"}
headers = {
    'cache-control': "no-cache",
}
response = requests.request("GET", url, headers=headers, params=querystring)
data = json.loads(response.text.replace('mtopjsonp1(', '').rstrip(')'))['data']
skuBase = SelectJmes("skuBase.props")
skuBase = skuBase(data)
props = SelectJmes("props")
props = props(data)
seller = SelectJmes("seller")
seller = seller(data)
item = SelectJmes("item.[title,tmallDescUrl,subtitle,images,itemId]")
item = item(data)
apiStack = SelectJmes("apiStack[].value")
apiStack = json.loads(apiStack(data)[0])
kuaidi = SelectJmes("delivery.[areaId,from,postage]")
kuaidi = kuaidi(apiStack)
price = SelectJmes("price")
price = price(apiStack)
sellCount = SelectJmes("item.sellCount")
sellCount = sellCount(apiStack)
print(item, props, skuBase, seller, price, kuaidi, sellCount)
