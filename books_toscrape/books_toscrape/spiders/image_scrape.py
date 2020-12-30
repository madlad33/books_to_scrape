import scrapy


class ImageScrapeSpider(scrapy.Spider):
    name = 'image_scrape'
    allowed_domains = ['bookstoscrape.com']
    start_urls = ['http://bookstoscrape.com/']

    def parse(self, response):
        pass
