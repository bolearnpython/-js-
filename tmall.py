import re
import json
import requests
from scrapy.loader.processors import SelectJmes
url = 'https://detail.m.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-14902430375.63.79a74ce1CfpmiQ&id=556955516923&rn=8ee79051f8726d88073713f6e0fafdd1&abbucket=13&sku_properties=1627207:28329'
session = requests.Session()
resp = session.get(url)
detail = re.findall('DATA_Detail.*?\n?({.*})', resp.text)[0]
mdskip = re.findall('DATA_Mdskip.*?\n?({.*})', resp.text)[0]
detail = json.loads(detail)
mdskip = json.loads(mdskip)
item = SelectJmes("item.[title,tmallDescUrl,subtitle,images,itemId]")
item = item(detail)
props = SelectJmes("props.groupProps")
props = props(detail)
skuBase = SelectJmes("skuBase.props[].[name,values]")
skuBase = skuBase(detail)
seller = SelectJmes("seller")
seller = seller(detail)

price = SelectJmes("price")
price = price(mdskip)
kuaidi = SelectJmes("delivery.[areaId,from,postage]")
kuaidi = kuaidi(mdskip)
sellCount = SelectJmes("item.sellCount")
sellCount = sellCount(mdskip)
print(item, props, skuBase, seller, price, kuaidi, sellCount)
