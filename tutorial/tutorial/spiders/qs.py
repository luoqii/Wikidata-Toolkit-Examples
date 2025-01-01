import scrapy
from pathlib import Path


class QsSpider(scrapy.Spider):
    name = "qs"
    allowed_domains = ["www.topuniversities.com"]
    start_urls = ["https://www.topuniversities.com/world-university-rankings"]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename=f"raw-{page}.html"
        Path(filename).write_bytes(response.body)
        rows = response.xpath('//div[contains(@class, "new-ranking-cards")]')
        print(len(rows))
        for row in rows:
            yield {
                "ranking": int(row.xpath('.//span[@class="rank-no"]/text()').get()),
                "universityName": row.xpath('.//div[@class="univ-names-text"]/a/text()').get().strip()
            }
        pass
