import requests

r = requests.get(
    'https://m.ctrip.com/webapp/hotel/contents/api/cas/gk/0?cb=____casf1&')
data = r.json()
key = requests.post('http://127.0.0.1:8080', data=data, timeout=4).text
print(key)
