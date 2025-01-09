
import unittest
from unittest.mock import Mock

from scrapy.selector import Selector
from scrapy.http import HtmlResponse

from qschina.spiders.ranking import RankingSpider, KEY_URL


class Scrapy_Xpath(unittest.TestCase):
    def test_uni_name(self):
        body='''
        <div class="header_righ"><h1><a href="http://www.clarkson.edu" target="_blank">Clarkson University</a></h1><p class="location_txt"><i class="fal fa-map-marker-alt"></i><span class="testt">8 Clarkson Avenue, Potsdam</span></p></div>
        '''

        response = HtmlResponse(url="http://www.example.com", body=body, encoding='utf8')

        name = response.xpath('//div[@class="header_righ"]/h1/a/text()')
        self.assertIsNotNone(name)
        self.assertEqual("Clarkson University", name.get())

    def test_uni_container(self):
        body='''
          <div id="rankingsTab" class="tab-content margin-top-40px margin-top-24-md">
    <div class="left">
      <div class="tit-list">
        <h4 class="rt">QS World University Rankings</h4>
        <ul class="nav nav-pills quicktabs-tabs no-margin chart-tabs">
          <li class="nav-item first active">
            <a class="nav-link active" href="#rank-graph" data-toggle="tab" class="graph_tab">Chart</a>
          </li>
          <li class="nav-item last">
            <a class="nav-link" href="#rank-data" data-toggle="tab" class="data_tab">Data</a>
          </li>
        </ul>
      </div>
            <div class="block-university-highlights">
        <div class="history">
          <div class="tab-content">
            <div class="rank tab-pane active no-padding-0" id="rank-graph">
              <div class="chartwp">
                <div id="rankingsChart"></div>
              </div>
            </div>
            <div class="rank tab-pane no-padding-0" id="rank-data">
              <ul><li>2012<div class="d-rank-res"> #1</div></li><li>2014<div class="d-rank-res"> #1</div></li><li>2015<div class="d-rank-res"> #1</div></li><li>2016<div class="d-rank-res"> #1</div></li><li>2017<div class="d-rank-res"> #1</div></li><li>2018<div class="d-rank-res"> #1</div></li><li>2019<div class="d-rank-res"> #1</div></li><li>2020<div class="d-rank-res"> #1</div></li><li>2021<div class="d-rank-res"> #1</div></li><li>2022<div class="d-rank-res"> #1</div></li><li>2023<div class="d-rank-res"> #1</div></li><li>2024<div class="d-rank-res"> #1</div></li><li>2025<div class="d-rank-res"> #1</div></li></ul>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="right">
      <div class="bar-chart">
                <div class="criteria-wrap">
        
        </div>
      </div>
      <div class="ranking_full_table margin-top-24px">
        <a class="white-blue-brand active" target="_blank" href="/world-university-rankings">
          <img fetchpriority="low" loading="lazy" src="/themes/custom/tu_d8/images/ranking-bars.svg" class="active-img" />View all rankings data
        </a>
      </div>
    </div>
  </div>
        '''

        response = HtmlResponse(url="http://www.example.com", body=body, encoding='utf8')

        ranking_tab = response.xpath('//div[@id="rankingsTab"]')
        self.assertIsNotNone(ranking_tab)
        ranking_class = ranking_tab.xpath('.//div[@class="tit-list"]//h4[@class="rt"]/text()')
        self.assertIsNotNone(ranking_class)
        list = ranking_tab.xpath('//div[@id="rank-data"]//li')
        self.assertIsNotNone(list)
        self.assertEqual(13, len(list))

        it = list[0]
        self.assertIsNotNone(it)
        self.assertEqual("2012", it.xpath('./text()').get())
        self.assertEqual(" #1", it.xpath('./div/text()').get())

        spider = RankingSpider(Mock())
        item = spider.parse_item(response)
        self.assertIsNotNone(item)
        self.assertEqual("http://www.example.com", item[KEY_URL])
        # self.assertEqual("", item[KEY_NAME])

if __name__ == '__main__':
    unittest.main()