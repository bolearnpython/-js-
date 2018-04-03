from mitmproxy import http
import re
from mitmproxy import flowfilter
filter_url = flowfilter.parse('~u icanhazip.com/')
filter_url1 = flowfilter.parse('~u baidu.com/')


def request(flow: http.HTTPFlow) -> None:
    '''
    演示request事件效果, 请求的时候输出提示
    :param flow:
    :return:
    '''
    if flowfilter.match(filter_url, flow):
        print(flow.request.headers)
        print(u'ip')
    if flowfilter.match(filter_url1, flow):
        print(u'baidu')


def response(flow: http.HTTPFlow) -> None:
    if flowfilter.match(filter_url, flow):
        flow.response.headers["server"] = "ip_nginx"
        flow.response.headers["newheader"] = "88888"
        reflector = b""
        flow.response.content = flow.response.content.replace(
            b"debugger", reflector)
        print(flow.response.content)
    if flowfilter.match(filter_url1, flow):
        flow.response.headers["server"] = "nginx"
        flow.response.headers["newheader"] = "99999"
        reflector = b""
        flow.response.content = flow.response.content.replace(
            b"debugger", reflector)
        # print(flow.response.content)
# mitmdump -s p.py
