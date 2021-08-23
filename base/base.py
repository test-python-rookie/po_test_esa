import time
from selenium.webdriver.support.wait import WebDriverWait
class Base:
    # 初始化
    def __init__(self, driver):
        self.driver = driver

    # 查找元素方法（提供：点击、输入、获取文本）使用
    def base_find_element(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    def base_find_elements(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_elements(*loc))

    # 点击方法
    def base_click(self, loc, num=None):
        if num is None:
            self.base_find_element(loc).click()
        else:
            self.base_find_elements(loc)[num].click()

    # 输入方法
    def base_input(self, loc, value, num=None):
        if num is None:
            el = self.base_find_element(loc)
        else:
            el = self.base_find_elements(loc)[num]
        # 清空
        el.clear()
        el.send_keys(*value)

    # 获取文本方法
    def base_get_text(self, loc, num=None):
        if num is None:
            return self.base_find_element(loc).text
        else:
            return self.base_find_elements(loc)[num].text


    # 获取当前页面url，用于断言
    def base_get_url(self):
        return self.driver.current_url

    # 截图方法
    def base_get_image(self):
        self.driver.get_screenshot_as_file('../image/error_{}.png'.format(time.strftime('%Y%m%d%H%M%S')))