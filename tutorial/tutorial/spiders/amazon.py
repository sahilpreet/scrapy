import scrapy


class AmazonSpider(scrapy.Spider):
    name = "amazon"
    start_urls = [
        'https://www.amazon.co.uk/product-reviews/B0042EU3A2/ref=cm_cr_othr_d_paging_btm_1?pageNumber=1',
    ]

    def parse(self, response):
        for i in range(10):
            yield {
                'rating': response.xpath('//div[@id="cm_cr-review_list"]/div/div/div/a/i/span/text()')[0::2][i].extract(),
                'date': response.xpath('//div[@id="cm_cr-review_list"]/div/div/div/span[@data-hook="review-date"]/text()')[i].extract(),
                'review': response.xpath('//div[@id="cm_cr-review_list"]/div/div/div/span[@data-hook="review-body"]/text()')[i].extract(),
                'link': response.xpath('//div[@id="cm_cr-review_list"]/div/div/div/a[@data-hook="review-title"]/@href')[i].extract()
            }

        for a in response.xpath('//li[@class="a-last"]/a'):
        	yield response.follow(a, callback=self.parse)