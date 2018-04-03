import requests
url = 'https://movie.douban.com/subject/1295644/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
response = requests.get(url, headers=headers)
from bs4 import BeautifulSoup
bs = BeautifulSoup(response.text, 'lxml')
content = bs.find("div", id="content")

# 标题
item = {}
name_and_year = [item.get_text()
                 for item in content.find("h1").find_all("span")]
name, year = name_and_year if len(
    name_and_year) == 2 else (name_and_year[0], "")
item['url'], item['name'], item['year'] = [
    url, name.strip(), year.strip("()")]

# 左边
content_left = bs.find("div", class_="subject clearfix")

nbg_soup = content_left.find("a", class_="nbgnbg").find("img")
item['img'] = nbg_soup.get("src") if nbg_soup else ""

info = content_left.find("div", id="info").get_text()
item['movie_info'] = dict([line.strip().split(
    ":", 1) for line in info.strip().split("\n") if line.strip().find(":") > 0])

# 右边
content_right = bs.find("div", class_="rating_wrap clearbox")
if content_right:
    item['rate'] = content_right.find(
        "strong", class_="ll rating_num").get_text()

    rating_people = content_right.find("a", class_="rating_people")
    item['rate_people'] = rating_people.find(
        "span").get_text() if rating_people else ""

    item['rating_per_list'] = [item.get_text()
                               for item in content_right.find_all("span", class_="rating_per")]
else:
    item['rate'], item['rate_people'], item[
        'rating_per_list'] = ['', '', '']
print(item)
