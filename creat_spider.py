#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-18 17:37:07
# @Author  : bo (bo17096701774@gmail.com)
# @Link    : https://github.com/bolearnpython
import os
import sys
now_path = sys.path[0]
print(now_path)


def creat_spider(templ, project_name, spider_names):
    creat = 'scrapy startproject {project_name} -s TEMPLATES_DIR={now_path}/templates'.format(
        project_name=project_name, now_path=now_path)
    cd_spider = '{project_name}/{project_name}/spiders'.format(
        project_name=project_name)
    if not os.path.isdir(project_name):
        os.system(creat)
    os.chdir(cd_spider)
    for spider_name in spider_names:
        if os.path.isfile('%s.py' % spider_name):
            print('存在spider')
            continue
        creat_spider = 'scrapy genspider -t {templ} {spider_name} {spider_name}.com -s TEMPLATES_DIR={now_path}/templates'.format(
            spider_name=spider_name, templ=templ, now_path=now_path)
        os.system(creat_spider)
if __name__ == '__main__':
    project_name = 'Test'  # 首字母大写
    spider_names = ['test']
    is_crawl = True
    templ = 'crawl'if is_crawl else'basic'
    creat_spider(templ, project_name, spider_names)
