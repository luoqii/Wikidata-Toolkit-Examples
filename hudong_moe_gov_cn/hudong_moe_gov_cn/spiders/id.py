from pprint import pprint
from typing import Iterable

from scrapy import Request
from scrapy.spiders import XMLFeedSpider


class IdSpider(XMLFeedSpider):
    name = "id"
    allowed_domains = ["hudong.moe.gov.cn"]
    start_urls = ["https://hudong.moe.gov.cn/school/wcmdata/getDataIndex.jsp?listid=10000101&page=11&keyword="]
    iterator = "iternodes"  # you can change this; see the docs
    itertag = "tr"  # change it accordingly

    def start_requests(self):
        for page in range(self.settings.get('MAX_PAGES')):
            yield Request(
                url=f"https://hudong.moe.gov.cn/school/wcmdata/getDataIndex.jsp?listid=10000101&page={page}&keyword=",
                dont_filter=True)

    def parse_node(self, response, selector):
        pprint(response)
        pprint(selector)
        # item = {}
        #item["url"] = selector.select("url").get()
        #item["name"] = selector.select("name").get()
        #item["description"] = selector.select("description").get()
        # return item
        trList = response.xpath('//tr')
        for tr in trList:
            yield {
                "seq"     : tr.xpath(".//td[1]/text()").get(),
                "name"    : tr.xpath(".//td[2]/text()").get(),
                "id"      : tr.xpath(".//td[3]/text()").get(),
                "owner"   : tr.xpath(".//td[4]/text()").get(),
                "location": tr.xpath(".//td[5]/text()").get(),
                "level"   : tr.xpath(".//td[6]/text()").get(),
                "note"    : tr.xpath(".//td[7]/text()").get(),
            }
