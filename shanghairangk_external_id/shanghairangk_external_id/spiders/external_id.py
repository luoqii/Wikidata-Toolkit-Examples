import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ExternalIdSpider(CrawlSpider):
    name = "external_id"
    allowed_domains = [
                       "www.shanghairanking.com"
                       ]
    start_urls = [
        "https://www.shanghairanking.com/institution/king-saud-university"
                  ]

    rules = (Rule(LinkExtractor(
                    allow=r"/institution/"),
                  callback="parse_item",
                  follow=True),)

    def parse_item(self, response):
        self.logger.debug(f"url:{response.url}")
        name = response.xpath('//div[@id="univ_name"]//span[@class="name-en"]/text()').get()
        regin = response.xpath('//div[@class="contact-msg"]/div[1]/span[2]/text()').get()
        country = response.xpath('//div[@class="contact-msg"]/div[2]/span[2]/text()').get()
        found_year = response.xpath('//div[@class="contact-msg"]/div[3]/span[2]/text()').get()
        weburl = response.xpath('//div[@class="contact-msg"]/div[5]/a/text()').get()
        item = {}
        item["name"] = name
        item["regin"] = regin
        item["country"] = country
        item["found_year"] = found_year
        item["weburl"] = weburl
        item["url"] = response.url

        return item
