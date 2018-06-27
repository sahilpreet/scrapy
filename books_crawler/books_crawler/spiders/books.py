# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class BooksSpider(CrawlSpider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = (
        'http://books.toscrape.com/',
    )

    # rules = (Rule(LinkExtractor(deny_domains=('google.com')), callback='parse_page', follow=True),)
    rules = (Rule(LinkExtractor(allow=('music')), callback='parse_page', follow=True),)

    def parse_page(self, response):
        pass
