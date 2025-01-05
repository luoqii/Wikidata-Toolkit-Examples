import time
from pprint import pprint

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Demo:
    def __init__(self):
        self.timeout = 10
        # 启动 Chrome 浏览器
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(self.timeout)
        self.browser.set_page_load_timeout(self.timeout)
        self.wait = WebDriverWait(self.browser, self.timeout)

    def debug(self, message):
        print(message)

    def is_empty(sefl, text):
        if len(text) == 0:
            return True
        else:
            return False

    def main(self):
        page = 2
        try:
            # 打开目标网页
            self.browser.get("https://www.shanghairanking.cn/institution")

            # 等待页面加载完成，可以根据页面上的某个元素进行等待，这里假设等待页面标题出现
            # WebDriverWait(driver, 10).until(EC.title_contains("ShanghaiRanking"))
            print("sleep")
            time.sleep(5)
            print("sleep done")


            if page > 1:
                self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                input = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="ant-pagination-options-quick-jumper"]/input')))

                self.debug(f"clear:{page} {input}")
                input.clear()
                self.debug(f"input:{page}")
                input.send_keys(str(page))
                time.sleep(3)
                self.debug(f"ENTER:{page}")
                input.send_keys(Keys.ENTER)
                time.sleep(3)

            self.wait.until(EC.text_to_be_present_in_element((By.XPATH, '//li[contains(@class, "ant-pagination-item-active")]/a'), str(page)))

            urls = []
            link = None
            for index in range(1,31):
                print(f"index:{index}")
                max_loop = 4
                while True:
                    school_links = self.browser.find_elements(By.XPATH, "//div[@class=\"univ-container\"]")
                    print("len", len(school_links))

                    if index >= len(school_links):
                        print(f"index:{index} sleep")
                        self.browser.get("https://www.shanghairanking.cn/institution")
                        # time.sleep(5)
                        max_loop = max_loop - 1
                        if max_loop == 0:
                            break
                        continue
                    else:
                        link = school_links[index]
                        text = link.text
                        print(f"text:{text}")
                        if not self.is_empty(text):
                            break

                        print("not found university sleep")
                        time.sleep(1)

                print(f"link:{link}")
                pprint(link)
                # 点击链接
                link.click()
                print("wait 3")
                time.sleep(1)
                url = self.browser.current_url
                urls.append(url)
                print("url:", url)
                # 可以在这里添加对学校详情页面的处理逻辑，比如提取信息等
                # print(f"Clicked on link: {link.get_attribute('href ')}")

                # 等待一段时间，观察页面是否加载完成，可根据实际情况调整等待时间
                # driver.implicitly_wait(3)

                # 可以添加返回操作，假设点击浏览器的后退按钮
                print("back")
                self.browser.back()
                print("back done")
                # time.sleep(3)

            print("len:", len(urls))
            for url in urls:
                print("url:", url)


        except Exception as e:
            print(f"Error occurred: {e}")

        finally:
            # 关闭浏览器
            self.browser.quit()


if __name__ == "__main__":
    Demo().main()