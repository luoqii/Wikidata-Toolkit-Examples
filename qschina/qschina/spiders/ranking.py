import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

KEY_RANKING_CLASS = "ranking_class"

KEY_NAME = "name"
KEY_URL = "url"

class RankingSpider(CrawlSpider):
    name = "ranking"
    allowed_domains = ["www.qschina.cn"]
    start_urls = [
                  "https://www.qschina.cn/en/universities/massachusetts-institute-technology-mit",
                  # "https://www.qschina.cn/en/university-rankings/world-university-rankings/2024",
                  ]
    rules = (Rule(LinkExtractor(allow=r"en/universities/[a-zA-Z0-9_-]+$", deny=r"universities/[^/]*/[^/].*"),
                  callback="parse_item",
                  follow=False),)

    def parse_item(self, response):
        item = {}
        item[KEY_URL] = response.url

        try:
            name_element = response.xpath('//div[@class="header_righ"]/h1/text()')
            if name_element is None:
                name_element = response.xpath('//div[@class="header_righ"]//a/text()')

            item[KEY_NAME] = name_element.get().strip()

            item[KEY_RANKING_CLASS] = []
            ranking_tab = response.xpath('//div[@id="rankingsTab"]')
            if ranking_tab is not None:
                for c in ranking_tab:
                    try:
                        item[KEY_RANKING_CLASS].append(self.parse_rankings(c))
                    except Exception as e:
                        self.logger.debug(f"parse_ranking exceptipn {e}")
                        pass
        except Exception as e:
            self.logger.debug(f"parse_item exceptipn {e}")
            pass

        return item

    def parse_rankings(self, ranking_tab):
        item = {}
        if ranking_tab is not None:
            ranking_class = ranking_tab.xpath('//div[@id="rankingsTab"]//div[@class="tit-list"]/h4[@class="rt"]/text()')
            if not ranking_class is None:
                item["ranking_name"] = ranking_class.get().strip()
                list = ranking_tab.xpath('//div[@id="rankingsTab"]//div[@id="rank-data"]//li')
                if list is not None:
                    item["rankings"] = []
                    for li in list:
                        year = li.xpath('./text()').get().strip()
                        ranking = li.xpath('.//div/text()').get().strip()
                        item["rankings"].append({"year":year, "ranking": ranking})
                else:
                    self.logger.debug(f"no found li")
            else:
                self.logger.debug(f"not found ranking class")
                return
        else:
            self.logger.debug(f"not found rankingTab")
            return

        # item["name"] = response.xpath('//div[@id="name"]').get()
        # item["description"] = response.xpath('//div[@id="description"]').get()
        return item