import os
from datetime import datetime

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import config
from middleware.handler import Handler




class BasePage:
    title = None

    def __init__(self, driver):
        self.driver = driver
        # self.title = None
        try:
            WebDriverWait(self.driver, 20).until(
                expected_conditions.title_contains(self.title)
            )
        except:

            print("你的操作可能没有进入对应的页面，可能会引发异常{}".format(self.title))


    def find_element(self, locator):
        """查找元素"""
        try:
            el = self.driver.find_element(*locator)
            return el
        except:
            # 如果找不到元素，截图
            self.screen_shot()
            Handler.logger.error("元素找不到{}".format(locator))

    def screen_shot(self):
        """截图"""
        # logs/img/screenshot-2020-08-01-12-12-23.png
        path = config.IMG_PATH
        ts = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        filename = os.path.join(path, ts + ".png")
        self.driver.save_screenshot(filename)


    def wait_element_visible(self, locator, timeout=20, poll=0.5):
        """等待某个元素可见"""
        try:
            el = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
                expected_conditions.visibility_of_element_located(locator)
            )
            return el
        except:
            self.screen_shot()
            Handler.logger.error("元素找不到{}".format(locator))

    def wait_element_clickable(self, locator, timeout=20, poll=0.5):
        """邓艾某个元素可以被点击"""
        try:
            el = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
                expected_conditions.element_to_be_clickable(locator)
            )
            return el
        except:
            self.screen_shot()
            Handler.logger.error("元素找不到{}".format(locator))

    def wait_element_presence(self, locator, timeout=20, poll=0.5):
        try:
            el = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
                expected_conditions.presence_of_element_located(locator)
            )
            return el
        except:
            self.screen_shot()
            Handler.logger.error("元素找不到{}".format(locator))

    def click(self, locator):
        """点击某个元素"""
        self.wait_element_clickable(locator).click()
        return self

    def write(self, locator, value=''):
        """输入信息"""
        self.wait_element_presence(locator).send_keys(value)
        return self

    def scroll(self, height=None, width=None):
        """窗口滚动"""
        if not height:
            height = 0
        if not width:
            width = 0
        js_code = "window.scrollTo({}, {});".format(width, height)
        self.driver.execute_script(js_code)
        return self

    def move_to(self, locator):
        """移动到某个元素"""
        el = self.driver.find_element(*locator)
        ActionChains(self.driver).move_to_element(el).perform()
        return self

    def switch_frame(self, locator, timeout=20):
        """切换到frame"""
        WebDriverWait(self.driver, timeout=timeout).until(
            expected_conditions.frame_to_be_available_and_switch_to_it(locator)
        )
        return self

    """双击，拓转，窗口切换， alert, select, 文件上传"""

    def swipe(self):
        """app滑动操作"""
