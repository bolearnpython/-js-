# url= "https://lf.snssdk.com/api/news/feed/v79/?category=ugc_video_food&iid=26837766237"
# url= "https://lf.snssdk.com/api/news/feed/v79/?category=hotsoon_video&iid=26837766237"
# url= "https://lf.snssdk.com/api/news/feed/v79/?category=ugc_video_life&iid=26837766237"
import requests
import json
url = "https://lf.snssdk.com/api/news/feed/v79/?category=ugc_video_beauty&iid=26837766237"
r = requests.get(url)
data = r.json()['data'][0]['content']
title = json.loads(data)['raw_data']['title']
video_url = json.loads(data)['raw_data']['video'][
    'download_addr']['url_list'][0]
print(title, video_url)
