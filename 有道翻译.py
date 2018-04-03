import time
import hashlib
import requests
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'


def createData(transStr):
    '''
    待翻译的内容
    :param transStr:
    :return: dict
    '''
    salt = str(int(time.time() * 1000))
    client = 'fanyideskweb'
    a = "rY0D^0'nM0}g5Mm1z%1G4"
    md5 = hashlib.md5()
    digStr = client + transStr + salt + a
    md5.update(digStr.encode())
    sign = md5.hexdigest()

    data = {
        'i': transStr,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CL1CKBUTTON',
        'typoResult': 'false'
    }
    return data
data = createData('大家好')

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,ko;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': '209',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'OUTFOX_SEARCH_USER_ID=-1942619238@115.55.248.2; OUTFOX_SEARCH_USER_ID_NCOO=1319658639.7881432; JSESSIONID=aaa9mDspuF4EV4QZks5hw; ___rl__test__cookies=1520305768752',
    'DNT': '1',
    'Host': 'fanyi.youdao.com',
    'Origin': 'http://fanyi.youdao.com',
    'Referer': 'http://fanyi.youdao.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
r = requests.post(url, data=data, headers=headers)
print(r.text)
