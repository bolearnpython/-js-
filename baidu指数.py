import requests
import arrow
startdate = arrow.now().shift(days=-7).format('YYYYMMDD')
enddate = arrow.utcnow().shift(days=-1).format('YYYYMMDD')
url = "http://index.baidu.com/Interface/Newwordgraph/getIndex"
querystring = {"region": "0", "startdate": startdate,
               "enddate": enddate, "wordlist[0]": "python"}
headers = {
    'accept': "application/json, text/plain, */*",
    'x-requested-with': "XMLHttpRequest",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
    'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
    'dnt': "1",
    'referer': "http://index.baidu.com/baidu-index-mobile/",
    'accept-encoding': "gzip, deflate",
    'accept-language': "zh-CN,zh;q=0.9,ko;q=0.8",
    'cookie': "BDUSS=xoV3J4Q1dKWTI2NTcycnNEVGdack43eFlWZ3hGamRrdFlkMTI5cUtvNGdDdUJhQVFBQUFBJCQAAAAAAAAAAAEAAACJv9I5zrnQodDExMQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACB9uFogfbhaSG",
    'cache-control': "no-cache",
}
response = requests.request("GET", url, headers=headers, params=querystring)
data = response.json()['data'][0]['index'][0]
_all, _pc, _wise = data['_all'], data['_pc'], data['_wise']
uniqid = response.json()['uniqid']
url_pwd = 'http://index.baidu.com/Interface/api/ptbk?uniqid=%s' % uniqid
response = requests.request("GET", url_pwd, headers=headers)
arr = response.json()['data']


objPass = {}
for i in range(len(arr) // 2):
    objPass[arr[i]] = arr[len(arr) // 2 + i]
allArr = []
pcArr = []
wiseArr = []
for j in range(len(_all)):
    if j < len(_all):
        allArr.append(objPass[_all[j]])
    if j < len(_pc):
        pcArr.append(objPass[_pc[j]])
    if j < len(_wise):
        wiseArr.append(objPass[_wise[j]])
allArr = ''.join(allArr).split(',')
pcArr = ''.join(pcArr).split(',')
wiseArr = ''.join(wiseArr).split(',')
print(allArr, pcArr, wiseArr)
