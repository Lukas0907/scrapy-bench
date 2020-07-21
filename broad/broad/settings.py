from __future__ import absolute_import

BOT_NAME = 'broadspider'

SPIDER_MODULES = ['broad.spiders']
NEWSPIDER_MODULE = 'broad.spiders'

CLOSESPIDER_ITEMCOUNT = 800
RETRY_ENABLED = False
COOKIES_ENABLED = True

LOGSTATS_INTERVAL = 3
LOG_LEVEL = 'INFO'
MEMDEBUG_ENABLED = True
CONCURRENT_REQUESTS = 120

AUTOTHROTTLE_ENABLED = True
REACTOR_THREADPOOL_MAXSIZE = 20

SCHEDULER_PRIORITY_QUEUE = 'scrapy.pqueues.DownloaderAwarePriorityQueue'

SCRAPY_BENCH_COOKIE_SIZE = None

DOWNLOADER_MIDDLEWARES = {
    'broad.middlewares.CookieSizeMiddleware': 701,
}

try:
    from .local_settings import *
except ImportError:
    pass
