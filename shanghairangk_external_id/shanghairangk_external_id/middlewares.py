# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

from itemadapter import is_item, ItemAdapter
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
import time

class ArwuMiddleware:
    def __init__(self):
        self.timeout = 10
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(10)
        self.browser.set_window_size(1200, 4000)
        self.browser.set_page_load_timeout(self.timeout)
        self.wait = WebDriverWait(self.browser, self.timeout)

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        return s

    def process_request(self, request, spider):
        print("url:", request.url)
        if request.url.endswith("robots.txt"):
            return None
        # if request.url.contains("institution"):
        #     return None

        year = request.meta.get('year')
        page = request.meta.get('page', 1)
        # page =4
        print('page:', page)
        spider.logger.debug(f"page:{page}")
        try:
            self.browser.get(f"{request.url}")
            # self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

            # if page > 1:
            #     input = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content-box"]/ul/li/div/input')))
            #
            #     spider.logger.debug(f"clear:{page} {input}")
            #     input.clear()
            #     spider.logger.debug(f"input:{page}")
            #     input.send_keys(str(page))
            #     time.sleep(3)
            #     spider.logger.debug(f"ENTER:{page}")
            #     input.send_keys(Keys.ENTER)
            #     time.sleep(3)
            #
            # self.wait.until(EC.text_to_be_present_in_element((By.XPATH, '//li[contains(@class, "ant-pagination-item-active")]/a'), str(page)))

            # self.browser.implicitly_wait(30)
            new_response = HtmlResponse(url=request.url,
                                        body=self.browser.page_source,
                                        # meta={ "year": year},
                                        request=request,
                                        encoding='utf-8',
                                        status = 200)

            current_page = new_response.xpath('//li[contains(@class, "ant-pagination-item-active")]/a')
            print("current_page", current_page)
            spider.logger.debug(f"current:{current_page}")

            return new_response
        except TimeoutException:
           return None

class ShanghairangkExternalIdSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class ShanghairangkExternalIdDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)
