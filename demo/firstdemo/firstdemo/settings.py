# -*- coding: utf-8 -*-

# Scrapy settings for firstdemo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'firstdemo'

SPIDER_MODULES = ['firstdemo.spiders']
NEWSPIDER_MODULE = 'firstdemo.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'firstdemo (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'en',
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'firstdemo.middlewares.FirstdemoSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':None,
#    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware':None,
#    'firstdemo.middlewares.RandomUAMiddleware': 500,
#    'firstdemo.middlewares.RandomProxyMiddleware': 510,
#    'firstdemo.middlewares.FirstdemoDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'scrapy_redis.pipelines.RedisPipeline':400
   # 'firstdemo.pipelines.MongoDBPipeline': 280,
   # 'firstdemo.pipelines.JsonFilePipeline': 290F,
   # 'firstdemo.pipelines.MaoyanImagePipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#对应于图片管道所需要设定的一些参数
IMAGES_STORE='D:/JPG/three'     #文件保存的场所
# IMAGES_EXPIRES= 30        #失效的一个日期
# IMAGES_WIDTH=100
# IMAGES_HEIGHT=100

# MONGO_URI='mongodb://127.0.0.1:27017/%admin'
# MONGO_DATABASE='xicidaili'
# MONGO_COLLECTION='daili'
# MONGO_URI='mongodb://127.0.0.1:27017/%admin'
# MONGO_DATABASE='MaoYanCrawl'
# MONGO_COLLECTION='list_1'

DOWNLOAD_TIMEOUT=5
#以下4步是redis必需的
#1.设置scrapy_redis调度器
SCHEDULER="scrapy_redis.scheduler.Scheduler"

#2.设置redis数据库的去重
DUPEFILTER_CLASS="scrapy_redis.dupefilter.RFPDupeFilter"

#3.设置是否清理Redis队列
# 如果这一项为True，那么在Redis总的url不会被Scrapy_redis清理
#这样的好处是：爬虫停止了再重新启动，他会从上次展厅的地方开始继续爬取
# 但是它的弊端也很明显，如果有多个爬虫都要从这里读取URL，需要另外写一段代码来防止重复爬取
SCHEDULER_PERSIST=True

#4.启用本地redis
#启用远程redis:REDIS_URL='redis://[远程URL]：6379'
REDIS_URL="redis://127.0.0.1:6379"



#如果Redis有密码设定的话，需要进行密码设定
# REDIS_PARAMS={
#    'password':'123456'
# }

#以utf-8格式保存到Redis
REDIS_ENCODING='utf-8'