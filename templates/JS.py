from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import logging
logger = logging.getLogger(__name__)
logger.info('JSMiddleware called')


class JSMiddleware(object):
    def __init__(self):
        dcaps = dict(DesiredCapabilities.PHANTOMJS)
        service = ['--ignore-ssl-errors=true',
                   '--ssl-protocol=any',
                   '--web-security=false']
        dcaps = {'handlesAlerts': False,
                 'javascriptEnabled': True,
                 'takesScreenshot': False}
        dcaps["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36")
        self.driver = webdriver.PhantomJS(
            desired_capabilities=dcaps, service_args=service)
        self.driver.set_window_size(1120, 550)
        self.driver.set_page_load_timeout(15)

    def ajax_complete(self, driver):
        jquery = False
        jscomplete = False
        try:
            jquery = (0 == driver.execute_script("return jQuery.active"))
        except WebDriverException:
            pass

        try:
            if driver.execute_script("return document.readyState") == "complete":
                jscomplete = True
        except WebDriverException:
            pass
        return jquery & jscomplete

    def process_request(self, request, spider):
        if 'PhantomJS' not in request.meta:
            return
        self.driver.get(request.url)
        WebDriverWait(self.driver, 20).until(
            self.ajax_complete, "Wait till loaded")
        body = self.driver.page_source.encode('utf-8')
        response = HtmlResponse(self.driver.current_url,
                                body=body, encoding='utf-8', request=request)
        return response
