# -*- coding: utf-8 -*-
import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['newyork.craigslist.org']
    start_urls = ('https://newyork.craigslist.org/d/architect-engineer-cad/search/egr',)

    def parse(self, response):
        listings = response.xpath('//li[@class="result-row"]')
        for listing in listings:
            date = listing.xpath('.//*[@class="result-date"]/@datetime').extract_first()
            link = listing.xpath('.//a[@class="result-title hdrlnk"]/@href').extract_first()
            text = listing.xpath('.//a[@class="result-title hdrlnk"]/text()').extract_first()

        # packing the values using meta method for later unpacking
        # process next page
            yield scrapy.http.Request(link, 
                                      callback=self.parse_listing,
                                      meta={'date': date,
                                            'link': link,
                                            'text': text})

        next_page_url = response.xpath('//a[text()="next > "]/@href').extract_first()
        if next_page_url:
            yield scrapy.http.Request(response.urljoin(next_page_url), callback=self.parse)


    def parse_listing(self, response):
        date = response.meta['date']
        link = response.meta['link']
        text = response.meta['text']

        compensation = response.xpath('//*[@class="attrgroup"]/span[1]/b/text()').extract_first()
        compensation_type = response.xpath('//*[@class="attrgroup"]/span[2]/b/text()').extract_first()

        address = response.xpath('//*[@id="postingbody"]/text()').extract()
        yield {'date': date,
               'link': link,
               'text': text,
               'compensation': compensation,
               'compensation_type': compensation_type,
               'address': address
               }

