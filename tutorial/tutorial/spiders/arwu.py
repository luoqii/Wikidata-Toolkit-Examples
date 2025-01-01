from typing import Iterable

import scrapy
from scrapy import Request


class ArwuSpider(scrapy.Spider):
    name = "arwu"
    allowed_domains = ["www.shanghairanking.cn"]
    start_urls = ["https://www.shanghairanking.cn/rankings/arwu/"]

    def start_requests(self):
        for year in range(2003, 2005):
            for page in range(self.settings.get('MAX_PAGES')):
                yield Request(url=self.start_urls[0], meta={ "year": year, "page": page + 1,}, dont_filter=True)

    def parse(self, response):
        #//*[@id="content-box"]/div[2]/table/tbody
        rows = response.xpath('//tbody/tr')
        print(rows)
        for r in rows:
            yield {
                "rank": (r.xpath('.//td/div/text()').get().strip()),
                "universityName": r.xpath('.//td[2]//span/text()').get().strip(),
                "year": response.meta["year"]
            }
        pass
