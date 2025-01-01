
import unittest
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

class Scrapy_Xpath(unittest.TestCase):
    def test_find_input(self):
        body='''
<li class="ant-pagination-options"><div class="ant-pagination-options-quick-jumper">跳至<input type="text">页</div></li>
        '''
        response = HtmlResponse(url="http://www.example.com", body=body, encoding='utf8')
        selector = Selector(response)
        input = selector.xpath('//div/input[@type="text"]').get()
        self.assertIsNotNone(input)

    def test_selected_page(self):
        body = '''
        <ul unselectable="unselectable" class="ant-pagination" data-v-752aabd6="" data-v-aa4df456=""><li title="上一页" class=" ant-pagination-prev" tabindex="0"><a class="ant-pagination-item-link"><i aria-label="图标: left" class="anticon anticon-left"><svg viewBox="64 64 896 896" data-icon="left" width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class=""><path d="M724 218.3V141c0-6.7-7.7-10.4-12.9-6.3L260.3 486.8a31.86 31.86 0 0 0 0 50.3l450.8 352.1c5.3 4.1 12.9.4 12.9-6.3v-77.3c0-4.9-2.3-9.6-6.1-12.6l-360-281 360-281.1c3.8-3 6.1-7.7 6.1-12.6z"></path></svg></i></a></li><li title="1" tabindex="0" class="ant-pagination-item ant-pagination-item-1"><a>1</a></li><li title="2" tabindex="0" class="ant-pagination-item ant-pagination-item-2"><a>2</a></li><li title="3" tabindex="0" class="ant-pagination-item ant-pagination-item-3 ant-pagination-item-active"><a>3</a></li><li title="4" tabindex="0" class="ant-pagination-item ant-pagination-item-4"><a>4</a></li><li title="5" tabindex="0" class="ant-pagination-item ant-pagination-item-5 ant-pagination-item-before-jump-next"><a>5</a></li><li title="向后 5 页" tabindex="0" class="ant-pagination-jump-next ant-pagination-jump-next-custom-icon"><a class="ant-pagination-item-link"><div class="ant-pagination-item-container"><i aria-label="图标: double-right" class="anticon anticon-double-right ant-pagination-item-link-icon"><svg viewBox="64 64 896 896" data-icon="double-right" width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class=""><path d="M533.2 492.3L277.9 166.1c-3-3.9-7.7-6.1-12.6-6.1H188c-6.7 0-10.4 7.7-6.3 12.9L447.1 512 181.7 851.1A7.98 7.98 0 0 0 188 864h77.3c4.9 0 9.6-2.3 12.6-6.1l255.3-326.1c9.1-11.7 9.1-27.9 0-39.5zm304 0L581.9 166.1c-3-3.9-7.7-6.1-12.6-6.1H492c-6.7 0-10.4 7.7-6.3 12.9L751.1 512 485.7 851.1A7.98 7.98 0 0 0 492 864h77.3c4.9 0 9.6-2.3 12.6-6.1l255.3-326.1c9.1-11.7 9.1-27.9 0-39.5z"></path></svg></i><span class="ant-pagination-item-ellipsis">•••</span></div></a></li><li title="34" tabindex="0" class="ant-pagination-item ant-pagination-item-34"><a>34</a></li><li title="下一页" tabindex="0" class=" ant-pagination-next"><a class="ant-pagination-item-link"><i aria-label="图标: right" class="anticon anticon-right"><svg viewBox="64 64 896 896" data-icon="right" width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class=""><path d="M765.7 486.8L314.9 134.7A7.97 7.97 0 0 0 302 141v77.3c0 4.9 2.3 9.6 6.1 12.6l360 281.1-360 281.1c-3.9 3-6.1 7.7-6.1 12.6V883c0 6.7 7.7 10.4 12.9 6.3l450.8-352.1a31.96 31.96 0 0 0 0-50.4z"></path></svg></i></a></li><li class="ant-pagination-options"><div class="ant-pagination-options-quick-jumper">跳至<input type="text">页</div></li></ul>
        '''
        response = HtmlResponse(url="http://www.example.com", body=body, encoding='utf8')
        selector = Selector(response)
        self.assertEqual(3, int(selector.xpath('//li[contains(@class, "ant-pagination-item-active")]/a/text()').get().strip()))

    def test_tr(self):
        body='''
        <tr data-v-389300f0=""><td data-v-389300f0="" class=""><div class="ranking top1" data-v-389300f0="">
                            1
                        </div></td><td class="align-left" data-v-389300f0=""><div class="global-univ" data-v-389300f0=""><div class="logo" data-v-389300f0=""><img alt="哈佛大学" onerror="this.src=&quot;/images/blank.svg&quot;" src="https://www.shanghairanking.cn/_uni/logo/032bd1b77.png" class="univ-logo" data-v-389300f0=""></div> <div class="tooltip" data-v-1098afc9="" data-v-389300f0=""><div class="link-container" style="width:190px" data-v-1098afc9=""><span class="univ-name univ-link" data-v-1098afc9="">
            哈佛大学
        </span></div> <!----></div> <!----></div></td><td data-v-389300f0="" class="">
                        美国
                        <!----></td><td data-v-389300f0="" class="">
                        1
                        <!----></td><td data-v-389300f0="" class="">
                        100.0
                    </td><td data-v-389300f0="" class="">100.0</td></tr>
        '''
        response = HtmlResponse(url="http://www.example.com", body=body, encoding='utf8')
        selector = Selector(response)
        self.assertEqual(1, int(selector.xpath('//tr/td/div/text()').get().strip()))
        self.assertEqual(1, int(selector.xpath('//tr/*/div/text()').get().strip()))
        self.assertEqual(1, int(selector.xpath('//div[1]/text()').get().strip()))

        self.assertEqual('哈佛大学', selector.xpath('//td[2]//span/text()').get().strip())


if __name__ == '__main__':
    unittest.main()