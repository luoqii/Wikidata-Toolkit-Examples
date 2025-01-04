import scrapy


class ExternalIdCnSpider(scrapy.Spider):
    name = "external_id_cn"
    allowed_domains = ["www.shanghairanking.cn"]
    start_urls = ["https://www.shanghairanking.cn/institution/tsinghua-university"]

    def parse(self, response):
        pass
