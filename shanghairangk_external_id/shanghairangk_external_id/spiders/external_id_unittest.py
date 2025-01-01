
import unittest
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

class Scrapy_Xpath(unittest.TestCase):
    def test_uni_container(self):
        body='''
<div data-v-986658e4="" data-v-38621d54="" class="univ-container"><div data-v-986658e4="" class="school-msg"><div data-v-986658e4="" id="univ_info" class="univ-info"><img data-v-986658e4="" id="univ_logo" onerror="javascript:this.src='/images/default_logo.svg';" src="https://www.shanghairanking.cn/_uni/logo/032bd1b77.png" alt="" class="logo"> <div data-v-986658e4="" id="univ_name" class="univ-name"><span data-v-986658e4="" class="name-en">Harvard University</span></div></div> <div data-v-986658e4="" class="labels-head"><img data-v-986658e4="" src="/_nuxt/img/top_shadow.e09625f.png" alt=""></div> <div data-v-986658e4="" class="scroll-container"><div data-v-986658e4="" class="contact-msg"><div data-v-986658e4="" class="contact-item"><span data-v-986658e4="">Region:</span> <span data-v-986658e4="">Northern America</span></div> <div data-v-986658e4="" class="contact-item"><span data-v-986658e4="">Country/Region:</span> <span data-v-986658e4="">United States</span></div> <div data-v-986658e4="" class="contact-item"><span data-v-986658e4="">Found Year:</span> <span data-v-986658e4="">1636</span></div> <div data-v-986658e4="" class="contact-item"><span data-v-986658e4="">Address:</span> <span data-v-986658e4="">Harvard University, Cambridge, Massachusetts 02138-3800, United States of America</span></div> <div data-v-986658e4="" class="contact-item"><span data-v-986658e4="">Website:</span> <a data-v-986658e4="" href="http://www.harvard.edu" target="_blank" style="text-decoration: underline;">http://www.harvard.edu</a></div></div> <div data-v-986658e4="" id="univ_intro" class="school-introduction"><div data-v-986658e4="" class="title"><div data-v-986658e4="" class="info-tab"><span data-v-986658e4="" class="active">Introduction</span></div> <p data-v-986658e4="">Harvard University is devoted to excellence in teaching, learning, and research, and to developing leaders in many disciplines who make a difference globally. Harvard faculty are engaged with teaching and research to push the boundaries of human knowledge. For students who are excited to investigate the biggest issues of the 21st century, Harvard offers an unparalleled student experience and a generous financial aid program, with over $160 million awarded to more than 60% of our undergraduate students. The University has twelve degree-granting Schools in addition to the Radcliffe Institute for Advanced Study, offering a truly global education.
Established in 1636, Harvard is the oldest institution of higher education in the United States. The University, which is based in Cambridge and Boston, Massachusetts, has an enrollment of over 20,000 degree candidates, including undergraduate, graduate, and professional students. Harvard has more than 360,000 alumni around the world.</p> <div data-v-986658e4="" class="gradient-line"></div></div></div></div></div></div>        '''
        response = HtmlResponse(url="http://www.example.com", body=body, encoding='utf8')
        selector = Selector(response)
        name = selector.xpath('//div[@id="univ_name"]//span[@class="name-en"]/text()').get()
        regin = selector.xpath('//div[@class="contact-msg"]/div[1]/span[2]/text()').get()
        country = selector.xpath('//div[@class="contact-msg"]/div[2]/span[2]/text()').get()
        found_year = selector.xpath('//div[@class="contact-msg"]/div[3]/span[2]/text()').get()
        weburl = selector.xpath('//div[@class="contact-msg"]/div[5]/a/text()').get()

        self.assertEqual("Harvard University", name)
        self.assertEqual("Northern America", regin)
        self.assertEqual("United States", country)
        self.assertEqual("1636", found_year)
        self.assertEqual("http://www.harvard.edu", weburl)



if __name__ == '__main__':
    unittest.main()