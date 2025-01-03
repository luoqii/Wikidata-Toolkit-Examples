import unittest

import scrapy
from scrapy import Request, Selector
from scrapy.http import HtmlResponse


class Scrapy_Xpath(unittest.TestCase):
    def test_find_input(self):
        body='''
        <div class="page mhide" id="_page">







<a onclick="pageForm(1)" href="javascript:void(0);">首页</a>&nbsp;<a onclick="pageForm(1)" href="javascript:void(0);">&lt;上一页</a>  <a onclick="pageForm(1)" href="javascript:void(0);">1</a> <span>2</span> <a onclick="pageForm(3)" href="javascript:void(0);">3</a> <a onclick="pageForm(4)" href="javascript:void(0);">4</a> <a onclick="pageForm(5)" href="javascript:void(0);">5</a> <a onclick="pageForm(5)" href="javascript:void(0);">...</a> <a onclick="pageForm(3)" href="javascript:void(0);">下一页&gt;</a>&nbsp;<a onclick="pageForm(144)" href="javascript:void(0);">末页</a><i>共144页，2868条数据，</i><i style="margin-left: 0px;">到第 <input type="text" id="tz" value="">页 <input class="submit" onclick="tzpageForm()" type="submit" id="" name="" value="确定"></i>

</div>
'''
        response = HtmlResponse(url="http://www.example.com", body=body, encoding='utf8')
        selector = Selector(response)
        input = selector.xpath('//i/input').get()
        self.assertIsNotNone(input)

        enter = selector.xpath('//input[@value="确定"]').get()
        self.assertIsNotNone(enter)

        select_page = selector.xpath('//div[@class="page mhide"]/span').get()
        self.assertIsNotNone(select_page)

    def test_item(self):
        body='''
        <tr class="bgcolor"><td>21</td><td>北京协和医学院</td><td>4111010023</td><td>国家卫生健康委员会</td><td>北京市</td><td>本科</td><td></td></tr>
        '''
        response = HtmlResponse(url="http://www.example.com", body=body, encoding='utf8')
        selector = Selector(response)

        self.assertEqual("21", selector.xpath('//td[1]/text()').get())

if __name__ == '__main__':
    unittest.main()