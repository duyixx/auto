import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "com.xxzb.fenwoo",
    "appActivity": "com.xxzb.fenwoo.activity.addition.WelcomeActivity",
    "automationName": "UiAutomator1",
}

# 初始化客户端
driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4723/wd/hub',
    desired_capabilities=caps,
)




time.sleep(10)
driver.quit()
