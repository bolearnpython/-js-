cmd
    scrapy startproject project
    cd project/project/spiders
    scrapy genspider -t crawl spider1 spider1.com
    scrapy crawl myspider -s LOG_FILE=scrapy.log
    scrapy shell <url>
    scrapy check -l
    scrapy list
    scrapy edit <spider>
    scrapy view <url>
    scrapy parse <url> [options]
        --spider=SPIDER: 跳过自动检测spider并强制使用特定的spider
        --a NAME=VALUE: 设置spider的参数(可能被重复)
        --callback or -c: spider中用于解析返回(response)的回调函数
        --pipelines: 在pipeline中处理item
        --rules or -r: 使用 CrawlSpider 规则来发现用来解析返回(response)的回调函数
        --noitems: 不显示爬取到的item
        --nolinks: 不显示提取到的链接
        --nocolour: 避免使用pygments对输出着色
        --depth or -d: 指定跟进链接请求的层次数(默认: 1)
        --verbose or -v: 显示每个请求的详细信息
    scrapy settings --get DOWNLOAD_DELAY
    scrapy runspider myspider.py
    scrapy bench

response-request
    FormRequest(url='http://www.viajanet.com.br/busca/resources/api/AvailabilityStatusAsync',formdata={})
    request.meta['proxy'] = "http://{}:{}@{}:{}".format(user,pass,'127.0.0.1','8118')
    meta = {'dont_redirect': True,'handle_httpstatus_list': [301,302]}
    dont_redirect
    dont_filter
    priority #此请求的优先级
    dont_retry
    handle_httpstatus_list
    dont_merge_cookies
    cookiejar
    redirect_urls
    bindaddress
    dont_obey_robotstxt
    download_timeout



LinkExtractor(allow=(), deny=(), allow_domains=(), deny_domains=(), restrict_xpaths=(), tags=('a', 'area'), attrs=('href',), canonicalize=False, unique=True, process_value=None, deny_extensions=None, restrict_css=(), strip=True)
allow (a regular expression (or list of))   – 必须要匹配这个正则表达式(或正则表达式列表)的URL才会被提取｡如果没有给出(或为空), 它会匹配所有的链接｡
deny (a regular expression (or list of))    – 与这个正则表达式(或正则表达式列表)的(绝对)不匹配的URL必须被排除在外(即不提取)｡它的优先级高于 allow 的参数｡如果没有给出(或None), 将不排除任何链接｡
allow_domains (str or list)                 – 单值或者包含字符串域的列表表示会被提取的链接的domains｡
deny_domains (str or list)                  – 单值或包含域名的字符串,将不考虑提取链接的domains｡
deny_extensions (list)                      – 应提取链接时,可以忽略扩展名的列表｡如果没有给出, 它会默认为 scrapy.linkextractor 模块中定义的 IGNORED_EXTENSIONS 列表｡
restrict_xpaths (str or list)               – 一个的XPath (或XPath的列表),它定义了链路应该从提取的响应内的区域｡如果给定的,只有那些XPath的选择的文本将被扫描的链接｡见下面的例子｡
tags (str or list)                          – 提取链接时要考虑的标记或标记列表｡默认为 ( 'a' , 'area') ｡
attrs (list)                                – 提取链接时应该寻找的attrbitues列表(仅在 tag 参数中指定的标签)｡默认为 ('href')｡
canonicalize (boolean)                      – 规范化每次提取的URL(使用scrapy.utils.url.canonicalize_url )｡默认为 True ｡
unique (boolean)                            – 重复过滤是否应适用于提取的链接｡
process_value (callable)                    – 它接收来自扫描标签和属性提取每个值, 可以修改该值, 并返回一个新的, 或返回 None 完全忽略链接的功能｡如果没有给出, process_value 默认是 lambda x: x
def process_value(value):
    m = re.search("javascript:goToPage\('(.*?)'", value)
    if m:
        return m.group(1)
Rule(link_extractor, callback=None, cb_kwargs=None, follow=None, process_links=None, process_request=None)
cb_kwargs 包含传递给回调函数的参数(keyword argument)的字典。
follow 是一个布尔(boolean)值，指定了根据该规则从response提取的链接是否需要跟进。 如果 callback 为None， follow 默认设置为 True ，否则默认为 False 。
process_links 是一个callable或string(该spider中同名的函数将会被调用)。 从link_extractor中获取到链接列表时将会调用该函数。该方法主要用来过滤。
process_request 是一个callable或string(该spider中同名的函数将会被调用)。 该规则提取到每个request时都会调用该函数。该函数必须返回一个request或者None。 (用来过滤request)








内存使用扩展(Memory usage extension)
    MEMDEBUG_ENABLED=False
    是否启用内存调试(memory debugging)
    MEMDEBUG_NOTIFY=[]
    如果该设置不为空like:['user@example.com']，当启用内存调试时将会发送一份内存报告到指定的地址；否则该报告将写到log中
    MEMUSAGE_LIMIT_MB=0
    在关闭Scrapy之前所允许的最大内存数
    MEMUSAGE_REPORT=False
    每个spider被关闭时是否发送内存使用报告。
    MEMUSAGE_WARNING_MB=0
    在发送警告email前所允许的最大内存数



关闭spider扩展
    CLOSESPIDER_TIMEOUT = 82800
    CLOSESPIDER_ITEMCOUNT
    CLOSESPIDER_PAGECOUNT
    CLOSESPIDER_ERRORCOUNT
关闭spider
    scrapy.exceptions.CloseSpider(reason='cancelled')
    def parse_page(self, response):
        if 'Bandwidth exceeded' in response.body:
            raise CloseSpider('bandwidth_exceeded')



邮件
    from scrapy.mail import MailSender
    mailer = MailSender()
    或
    mailer = MailSender.from_settings(settings)
发送email
    mailer.send(to=["someone@example.com"], subject="Some subject", body="Some body", cc=["another@example.com"])
    MAIL_FROM='scrapy@localhost'
    用于发送email的地址(address)(填入 ``From:``) 。
    MAIL_HOST='localhost'
    发用邮件的SMTP主机
    MAIL_PORT=25
    发用邮件的SMTP端口
    MAIL_USER=None
    MAIL_PASS=None
    用于SMTP认证，与 :setting:`MAIL_USER` 配套的密码。
    MAIL_TLS=False
    强制使用STARTTLS。STARTTLS能使得在已经存在的不安全连接上，通过使用SSL/TLS来实现安全连接。
    MAIL_SSL=False
    强制使用SSL加密连接。





单spider追踪多cookie session
    for i, url in enumerate(urls):
        yield scrapy.Request("http://www.example.com", meta={'cookiejar': i},
            callback=self.parse_page)
    def parse_page(self, response):
        return scrapy.Request("http://www.example.com/otherpage",
            meta={'cookiejar': response.meta['cookiejar']},
            callback=self.parse_other_page)





缓存
    Dummy策略(默认值)
    RFC2616策略
    HTTPCACHE_ENABLED = False
    HTTPCACHE_DIR = 'httpcache'
    HTTPCACHE_IGNORE_MISSING = False
    HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
    HTTPCACHE_EXPIRATION_SECS = 0
    HTTPCACHE_ALWAYS_STORE = False
    HTTPCACHE_IGNORE_HTTP_CODES = []
    HTTPCACHE_IGNORE_SCHEMES = ['file']
    HTTPCACHE_IGNORE_RESPONSE_CACHE_CONTROLS = []
    HTTPCACHE_DBM_MODULE = 'anydbm' if six.PY2 else 'dbm'
    HTTPCACHE_POLICY = 'scrapy.extensions.httpcache.DummyPolicy'
    HTTPCACHE_GZIP = False




增加全局并发数::
    CONCURRENT_REQUESTS = 100
    Item Processor(即 Item Pipeline) 同时处理(每个response的)item的最大值。
    CONCURRENT_ITEMS = 100
    Scrapy downloader 并发请求(concurrent requests)的最大值。
    CONCURRENT_REQUESTS = 16
    对单个网站进行并发请求的最大值。
    CONCURRENT_REQUESTS_PER_DOMAIN = 8
    对单个IP进行并发请求的最大值。如果非0，则忽略 CONCURRENT_REQUESTS_PER_DOMAIN 设定， 使用该设定。 也就是说，并发限制将针对IP，而不是网站。
    该设定也影响 DOWNLOAD_DELAY: 如果 CONCURRENT_REQUESTS_PER_IP 非0，下载延迟应用在IP而不是网站上。
    CONCURRENT_REQUESTS_PER_IP = 0



设置Log级别:
    LOG_ENABLED = true
    LOG_ENCODING = "utf-8"
    LOG_FILE = "log/spider.log"
    LOG_FORMAT = "%(asctime)s [%(name)s] %(levelname)s: %(message)s"
    LOG_DATEFORMAT = "%Y-%m-%d %H:%M:%S"
    LOG_LEVEL = 'INFO'#默认'debug'
    LOG_ENCODING#logging使用的编码
    LOG_STDOUT  #为 ``True``,进程所有的标准输出(及错误)将会被重定向到log中
    #spider
    self.logger.info('Parse function called on %s', response.url)
    自定义logger
    import logging
    logger = logging.getLogger('zhangsan')
    logger.info('Parse function called on %s', response.url)
禁止cookies::
    COOKIES_ENABLED = False
    COOKIES_DEBUG
timeout
    DOWNLOAD_TIMEOUT = 10      # 3mins
robots
    ROBOTSTXT_OBEY = False
爬取URL的最大长度
    URLLENGTH_LIMIT = 2083
禁止重试::
    RETRY_ENABLED = False
    RETRY_TIMES=2
    RETRY_HTTP_CODES=[500, 502, 503, 504, 400, 408]
    [500, 503, 504, 400, 403, 404, 408]

关闭重定向::
    REDIRECT_ENABLED = False
    REDIRECT_MAX_TIMES=20
    单个request被重定向的最大次数。
    REDIRECT_MAX_METAREFRESH_DELAY=100
    有些网站使用 meta-refresh 重定向到session超时页面，
    因此我们限制自动重定向到最大延迟(秒)。
    REDIRECT_PRIORITY_ADJUST
    默认: ``+2``
    修改重定向请求相对于原始请求的优先级。
    负数意味着更多优先级。
自动限速
    AUTOTHROTTLE_ENABLED=False
    AUTOTHROTTLE_START_DELAY=5.0
    AUTOTHROTTLE_MAX_DELAY=60
    AUTOTHROTTLE_DEBUG=False
depth防止死循环
    爬取网站最大允许的深度(depth)值。如果为0，则没有限制。
    DEPTH_LIMIT = 0
    整数值。用于根据深度调整request优先级。
    如果为0，则不根据深度进行优先级调整。
    DEPTH_PRIORITY = 0
广度优先顺序
    DEPTH_PRIORITY = 1
    SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
    SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'
error
    HTTPERROR_ALLOWED_CODES=[]
    忽略该列表中所有非200状态码的response。
    HTTPERROR_ALLOW_ALL=Flase
    忽略所有response，不管其状态值。
telnet
    TELNETCONSOLE_ENABLED=True
    telnet 终端是否启用。
    TELNETCONSOLE_PORT
    默认: ``[6023, 6073]``
EDITOR
    默认: depends on the environment
    执行 edit 命令编辑spider时使用的编辑器。 其默认为 EDITOR 环境变量。如果该变量未设置，其默认为 vi (Unix系统) 或者 IDLE编辑器(Windows)。
USER_AGENT = 'Scrapy/'



DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
}
ITEM_PIPELINES = {
   'mybot.pipelines.validate.ValidateMyItem': 300,
   'mybot.pipelines.validate.StoreMyItem': 800,
}
将原先的配置进行覆盖
class MySpider(scrapy.Spider):
    name = 'myspider'
    custom_settings = {
        'DOWNLOAD_DELAY': 1,
        'RANDOMIZE_DOWNLOAD_DELAY': False,
        'CONCURRENT_REQUESTS_PER_IP': 1,
    }

class MyExtension(object):
    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        if settings['LOG_ENABLED']:
            print "log is enabled!"



DNSCACHE_ENABLED
默认: ``True``
DUPEFILTER_CLASS
默认: ``'scrapy.dupefilter.RFPDupeFilter'``
DUPEFILTER_DEBUG
默认: ``False``
SCHEDULER
默认: ``'scrapy.core.scheduler.Scheduler'``



scrapyd
    pip install scrapyd-client
    拷贝scrapyd-deploy工具到爬虫目录下
    Ubuntu/Windows:
    [deploy:tutorial_deploy]
    url = http://192.168.17.129:6800/
    project = tutorial
    username = enlong
    password = test
    Windows:
        python c:\Python27\Scripts\scrapyd-deploy
    Ubuntu:
        scrapyd-deploy tutorial_deploy -p tutorial
    python scrapyd-deploy -l
    scrapyd-deploy <target> -p <project> --version <version>
    python scrapyd-deploy 127 -p projectccp --version ver20160702



1、获取状态
http://127.0.0.1:6800/daemonstatus.json
2、获取项目列表
http://127.0.0.1:6800/listprojects.json
3、获取项目下已发布的爬虫列表
http://127.0.0.1:6800/listspiders.json?project=myproject
4、获取项目下已发布的爬虫版本列表
http://127.0.0.1:6800/listversions.json?project=myproject
5、获取爬虫运行状态
http://127.0.0.1:6800/listjobs.json?project=myproject
6、启动服务器上某一爬虫（必须是已发布到服务器的爬虫）
http://localhost:6800/schedule.json （post方式，data={"project":myproject,"spider":myspider}）
7、删除某一版本爬虫
http://127.0.0.1:6800/delversion.json （post方式，data={"project":myproject,"version":myversion}）
8、删除某一工程，包括该工程下的各版本爬虫
http://127.0.0.1:6800/delproject.json（post方式，data={"project":myproject}）



错误
    TypeError
    表现形式:TypeError: ‘float’ object is not iterable
    相关搜索:https://github.com/scrapy/scrapy/issues/2461
    解决方法:sudo pip install -U Twisted==16.6.0
    ERROR: Unable to read the instance data ,giving up
    表现形式: 直接error 报错，拿不到数据
    相关搜索: 无
    解决方法: 回调函数中，必须返回 Request 对象 或者Item对象 ，可以直接返回这种类型的数据就可以了
    Library not loaded: /opt/local/lib/libssl.1.0.0.dylib (LoadError)
    解决方法: brew remove openssl 先卸载，然后 brew install openssl
    unknown command: crawl error
    表现形式: 无法使用crawl 命令
    相关搜索 : unknown-command-crawl-error
    解决方法 : 切换到有scrapy.cfg文件下，然后使用命令



