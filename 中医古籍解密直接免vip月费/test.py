import requests
headers = {'accept': 'application/json, text/javascript, */*; q=0.01',
           'accept-encoding': 'gzip, deflate, br',
           'accept-language': 'zh-CN,zh;q=0.9,ko;q=0.8',
           'dnt': '1',
           'referer': 'https://www.zk120.com/ji/read/499?nav=ahz&uid=None',
           'shtech_http_cache': 'nocache',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
           'x-requested-with': 'XMLHttpRequest'}
response = requests.get(
    'https://www.zk120.com/ji/content/499?uid=None', headers=headers, verify=False)
data = response.json()
response = requests.post('http://127.0.0.1:7788', data=data, timeout=4)
data = response.json()
import pymongo
client = pymongo.MongoClient()
db = client['book_zhongyao']
book_Item = db['book_Item']
book_Item.insert_one(dict(data))
import arrow
arrow.now().timestamp
