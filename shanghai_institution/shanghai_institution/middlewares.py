# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
from pprint import pprint

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.signals import item_scraped

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
import time

MAX_ITEM_COUNT = 31

class UniversityMiddleware:
    def __init__(self):
        self.timeout = 10
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(10)
        self.browser.set_window_size(1000, 4000)
        self.browser.set_page_load_timeout(self.timeout)
        self.wait = WebDriverWait(self.browser, self.timeout)

    def is_empty(sefl, text):
        if len(text) == 0:
            return True
        else:
            return False

    def sleep(self, duration):
        print(f"sleep:{duration}s")
        time.sleep(duration)
        print(f"sleep:{duration}s done")

    def debug(self, spider, message):
        spider.logger.debug(message)
        print(message)

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        return s

    def process_request(self, request, spider):
        self.debug(spider,f"process_request url:{request.url}")
        if request.url.endswith("robots.txt"):
            return None
        if not request.url.endswith("/institution"):
            return None

        page = request.meta.get('page', 1)
        # page =4
        self.debug(spider,f"page:{page}")
        try:
            self.debug(spider,f"load page:{request.url}")
            self.browser.get(f"{request.url}")
            self.sleep(3)
            if page == 1:
                self.sleep(2)

            urls = []
            try:
                if page > 1:
                    self.debug(spider, f"scroll to bottom")
                    self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    self.sleep(2)
                    self.debug(spider, f"find input")
                    input = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="ant-pagination-options-quick-jumper"]/input')))

                    self.debug(spider, f"clear:{page} {input}")
                    input.clear()
                    self.debug(spider, f"input:{page}")
                    input.send_keys(str(page))
                    time.sleep(1)
                    self.debug(spider, f"ENTER:{page}")
                    input.send_keys(Keys.ENTER)
                    time.sleep(2)
                    self.debug(spider, f"scroll to top")
                    self.browser.execute_script("window.scrollTo(0, 0);")
                    self.sleep(2)

                    self.wait.until(EC.text_to_be_present_in_element((By.XPATH, '//li[contains(@class, "ant-pagination-item-active")]/a'), str(page)))

                link = None
                for index in range(1, MAX_ITEM_COUNT):
                    self.debug(spider,f"index:{index}")
                    max_loop = 4
                    while True:
                        self.debug(spider,"find element")
                        school_links = self.browser.find_elements(By.XPATH, "//div[@class=\"univ-container\"]")
                        self.debug(spider,"find element done")
                        self.debug(spider,f"len:{len(school_links)}")

                        if index >= len(school_links):
                            self.debug(spider,f"index:{index} sleep")
                            self.browser.get("https://www.shanghairanking.cn/institution")
                            # sleep(5)
                            if max_loop == 0:
                                break
                            max_loop = max_loop - 1
                            continue
                        else:
                            link = school_links[index]
                            text = link.text
                            self.debug(spider,f"text:{text}")
                            if not self.is_empty(text):
                                break

                            self.debug(spider,"not found university sleep")
                            self.sleep(1)

                    # pprint(link)
                    # 点击链接
                    link.click()
                    self.debug(spider,"wait 3")
                    self.sleep(1)
                    url = self.browser.current_url
                    self.debug(spider,f"current_url url:{url}")

                    wait_url_loop = 3
                    while True:
                        if url.endswith("/institution"):
                            if wait_url_loop == 0:
                                break
                            wait_url_loop = wait_url_loop - 1
                            self.debug(spider,f"wait true url. current:{url}")
                            self.sleep(1)
                            url = self.browser.current_url
                        else:
                            break
                    if not url.endswith("/institution"):
                        self.debug(spider,f"add url to queue:{url}")
                        urls.append(url)

                    self.debug(spider,"back")
                    self.browser.back()
                    self.debug(spider,"back done")
            except TimeoutException as e:
                self.debug(spider, f"exception:{e}")

            self.debug(spider,f"collected len:{len(urls)}")
            for url in urls:
                self.debug(spider,f"collected url:{url}")

            request.meta["urls"] = urls

            # self.browser.implicitly_wait(30)
            new_response = HtmlResponse(url=request.url,
                                        body=self.browser.page_source,
                                        # meta={ "year": year},
                                        request=request,
                                        encoding='utf-8',
                                        status = 200)

            return new_response
        except TimeoutException as e:
            self.debug(spider,f"exception:{e}")

        return None

class ShanghaiInstitutionSpiderMiddleware:
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


class ShanghaiInstitutionDownloaderMiddleware:
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
