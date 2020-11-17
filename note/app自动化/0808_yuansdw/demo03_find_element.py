import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "com.lemon.lemonban",
    "appActivity": ".activity.MainActivity",
    "automationName": "UiAutomator1",
}

# 初始化客户端
driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4723/wd/hub',
    desired_capabilities=caps,
)

# 通过 ID
# el = driver.find_element("id", "com.lemon.lemonban:id/navigation_my")
# el.click()

# 通过 content-desc 属性查找
# el = driver.find_element_by_accessibility_id("值")

# uiautomator
# 值，value: Java 代码
# TODO: Java 代码表示字符串是用双引号，单引号不行，
# TODO：可以在里面的引号之前打 \

# selector = 'new UiSelector().resourceId(\"com.lemon.lemonban:id/navigation_my\")'
# el = driver.find_element_by_android_uiautomator(selector)
# # el = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, "")
# el.click()


# 和xpath 一样，可以进行条件的组合。
# 比 xpath 更快
# 子元素new UiSelector().resourceId("com.lemon.lemonban:id/smallLabel").text("我的柠檬").childSelector(
# new UiSelector().resourceId())

# 父元素， （子元素）  ==》 通过子元素的特征找到父元素
# new UiSelector().checkable(false).childSelector(
#        new UiSelector().checkable()
# )


selector = 'new UiSelector().resourceId("com.lemon.lemonban:id/smallLabel").text("我的柠檬")'

#
el = driver.find_element_by_android_uiautomator(selector)
el.click()

# XPATH
# el = driver.find_element(MobileBy.XPATH, "")

time.sleep(2)
driver.quit()

# 元素等待
# 强制
# 隐式等待
# 显示等待

# 元素定位辅助工具
# appium
# uiautomatorviewer: android 调试工具   手动刷新
#

