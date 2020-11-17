"""需要滑屏。

欢迎页面
"""

import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction

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

# 定位到 activity
driver.start_activity(
    app_package="com.xxzb.fenwoo",
    app_activity=".activity.user.CreateGesturePwdActivity"
)

time.sleep(1)
e = driver.find_element_by_id('com.xxzb.fenwoo:id/right_btn')
e.click()

## 九宫格的绘制
time.sleep(2)
e = driver.find_element_by_id("com.xxzb.fenwoo:id/gesturepwd_create_lockview")
size = e.rect

start_x = size["x"]
start_y = size["y"]
width = size["width"]
height = size["height"]

point_1 = {"x":start_x + width * 1 / 6 , "y": start_y + height * 1 /6}
point_2 = {"x":start_x + width * 3 / 6 , "y": start_y + height * 1 /6}
point_3 = {"x":start_x + width * 5 / 6 , "y": start_y + height * 1 /6}
point_4 = {"x":start_x + width * 1 / 6 , "y": start_y + height * 3 /6}
point_5 = {"x":start_x + width * 3 / 6 , "y": start_y + height * 3 /6}
point_6 = {"x":start_x + width * 5 / 6 , "y": start_y + height * 3 /6}
point_7 = {"x":start_x + width * 1 / 6 , "y": start_y + height * 5 /6}
point_8 = {"x":start_x + width * 3 / 6 , "y": start_y + height * 5 /6}
point_9 = {"x":start_x + width * 5 / 6 , "y": start_y + height * 5 /6}


action = TouchAction(driver)
action.press(**point_1).wait(200).\
    move_to(**point_2).wait(200).\
    move_to(**point_5).wait(200).\
    move_to(**point_8).wait(200).\
    move_to(**point_9).release().perform()


time.sleep(3)

driver.quit()

# driver.jiugongge([1,3,5,7,9])
# BasePage


