"""需要滑屏。

欢迎页面
"""

import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "com.xxzb.fenwoo",
    "appActivity": "com.xxzb.fenwoo.activity.addition.WelcomeActivity",
    # "automationName": "UiAutomator2",
    "noReset": False
}

# 初始化客户端
driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4723/wd/hub',
    desired_capabilities=caps,
)


# swipe
# 屏幕，宽 800， 高 900
# 790, 450, 10, 450
# driver.swipe(790, 450, 10, 450)

# 问题在于我传的坐标到底应该是多少。
# 取决于屏幕的宽度
# 先获取屏幕宽度 width, height
# 向左滑，我的起始点 x 坐标， width * 0.9, height * 0.5    结束点 x 坐标， 0.1, height *0.5
# 结束点的 height 和 起始点保持一致。

# # 获取屏幕的宽度。
# size = driver.get_window_size()
# # 得到一个字典
# width = size["width"]
# height = size["height"]
# # 向左滑动
# # 这个就是滑动的标准操作
# driver.swipe(
#     start_x= width * 0.9,
#     start_y= height * 0.5,
#     end_x= width * 0.1,
#     end_y= height * 0.5
# )
#
# 二次封装 swipe
class BasePage():
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

    def swipe_left(self, duration=None):
        """向左边滑动"""
        size = self.driver.get_window_size()
        # 得到一个字典
        width = size["width"]
        height = size["height"]
        # 向左滑动
        # 这个就是滑动的标准操作
        self.driver.swipe(
            start_x=width * 0.9,
            start_y=height * 0.5,
            end_x=width * 0.1,
            end_y=height * 0.5,
            duration=duration
        )

    def swipe_right(self, duration=None):
        size = self.driver.get_window_size()
        # 得到一个字典
        width = size["width"]
        height = size["height"]
        # 向左滑动
        # 这个就是滑动的标准操作
        self.driver.swipe(
            start_x=width * 0.1,
            start_y=height * 0.5,
            end_x=width * 0.9,
            end_y=height * 0.5,
            duration=duration
        )

    def swipe_up(self, duration=None):
        size = self.driver.get_window_size()
        # 得到一个字典
        width = size["width"]
        height = size["height"]
        # 向左滑动
        # 这个就是滑动的标准操作
        self.driver.swipe(
            start_x=width * 0.5,
            start_y=height * 0.9,
            end_x=width * 0.5,
            end_y=height * 0.1,
            duration=duration
        )

    def swipe_down(self, duration=None):
        size = self.driver.get_window_size()
        # 得到一个字典
        width = size["width"]
        height = size["height"]
        # 向左滑动
        # 这个就是滑动的标准操作
        self.driver.swipe(
            start_x=width * 0.5,
            start_y=height * 0.1,
            end_x=width * 0.5,
            end_y=height * 0.9,
            duration=duration
        )

time.sleep(10)

BasePage(driver).swipe_left()


# 当执行完程序以后，一定要加上 quit()
# appium 本身自动退出session, 但是如果是自动退出，会非常不稳定，引发元素定位不成功等问题。
# TODO: 手工加上 driver.quit()
# 重启模拟器，或者重新加上quit() 以后，再次运行原来的脚本
driver.quit()


##