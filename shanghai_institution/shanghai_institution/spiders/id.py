from pprint import pprint

import scrapy
import re
from scrapy import Request
from pathlib import Path

from selenium.common import TimeoutException

class IdSpider(scrapy.Spider):
    name = "id"
    allowed_domains = ["www.shanghairanking.cn"]
    start_urls = ["https://www.shanghairanking.cn/institution"]

    def debug(self, message):
        print(message)

    def start_requests(self):
        for page in range(self.settings.get('MAX_PAGES')):
            yield Request(url=self.start_urls[0],
                          meta={"page": page + 1, },
                          priority = 0,
                          dont_filter=True)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename=f"raw-{page}.html"
        # Path(filename).write_bytes(response.body)

        self.logger.debug(f"response:{response}")
        self.debug(f"response:{response}")
        try:
            urls = response.request.meta["urls"]
            self.logger.debug(f"len:{len(urls)}")
            self.debug(f"len:{len(urls)}")
            pprint(urls)
            for url in urls:
                self.logger.debug(f"yield url:{url["url"]}")
                self.debug(f"yield url:{url["url"]}")
                yield Request(
                    url=url["url"],
                    meta={"coord":url["coord"]},
                    priority=1000,
                    callback=self.parse_detail,
                    dont_filter=True)
            self.logger.debug(f"yield done")
            self.debug(f"yield done")

        except TimeoutException as e:
            self.debug(f"exception: {e}")

        # js_data = response.body.decode('utf-8')
        # # self.logger.debug(f"js_data:{js_data}")
        # up_values = re.findall(r'up="([^"]+)"', js_data)
        # self.logger.debug(f"size:{len(up_values)}")
        # for value in up_values:
        #     self.debug(value)
        #     # yield Request(url=f"https://www.shanghairanking.cn/institution/{value}", callback=self.parse_university)
        #     # # break
        pass

    def parse_detail(self, response):
        yield {
            "name_cn" : response.xpath('//div[@id="univ_name"]/span[@class="name-cn"]/text()').get(),
            "name_en" : response.xpath('//div[@id="univ_name"]/span[@class="name-en"]/text()').get(),
            "location": response.xpath('//div[@id="univ_addr"]//div[@class="school-name"]/span/text()').get(),
            "weburl"  : response.xpath('//div[@id="univ_addr"]//div[@class="school-website"]/span/text()').get(),
            "email"   : response.xpath('//div[@id="univ_addr"]//div[@class="school-email"]/span/text()').get(),
            "url"     : response.url,
            "coord"   : response.meta["coord"]

        }
