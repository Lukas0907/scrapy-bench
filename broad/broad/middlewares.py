class CookieSizeMiddleware:
    def __init__(self, size):
        self.size = size

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getint('SCRAPY_BENCH_COOKIE_SIZE'))

    def process_request(self, request, spider):
        if not self.size:
            return

        request.headers['Cookie'] = self.size * 'x'
