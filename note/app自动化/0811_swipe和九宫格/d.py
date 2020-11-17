import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

caps = {
    "platformName": "Android",
    "platformVersion": "5.1",
    "automationName": "UiAutomator2",
    "deviceName": "Android Emulator",
    "appActivity": "com.lemon.lemonban.activity.WelcomeActivity",
    "appPackage": "com.lemon.lemonban",
    "noReset": False,
}


def find_presence_element(driver, locator):
    return WebDriverWait(driver, 10, 0.2).until(EC.presence_of_element_located(locator))


driver = webdriver.Remote(desired_capabilities=caps)

# 点击我的
me = find_presence_element(driver,
                           (MobileBy.ID, 'com.lemon.lemonban:id/navigation_my'))
me.click()

# 点击登录
login = find_presence_element(driver,
                              (MobileBy.ID, 'com.lemon.lemonban:id/fragment_my_lemon_avatar_layout'))
login.click()

# 输入手机
mobile = find_presence_element(driver, (MobileBy.ID, 'com.lemon.lemonban:id/et_mobile'))
mobile.send_keys('123')
# 点击登录
login_btn = find_presence_element(driver, (MobileBy.ID, 'com.lemon.lemonban:id/btn_login'))
login_btn.click()
# 定位 toast
toast = find_presence_element(driver, (MobileBy.XPATH, "//*[contains(@text, '手机')]"))
#

# import MobyieBy as By

print(toast.text)
driver.quit()