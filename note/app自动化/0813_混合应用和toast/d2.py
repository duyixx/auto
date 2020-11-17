import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

package_name = "com.lemon.lemonban"

caps = {
    "platformName": "Android",
    "deviceName": "774a0b78",
    "appPackage": package_name,
    "appActivity": ".activity.MainActivity",
    "automationName": "UiAutomator1",
    "chromedriverExecutableDir": r"D:\chromedriver_win32"
}

# 初始化客户端
driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4723/wd/hub',
    desired_capabilities=caps,
)

# 隐式等待
driver.implicitly_wait(20)

# 定位 师资团队
# 'new UiSelector().text("师资团队")'
# driver.find_element_by_android_uiautomator()

print(driver.contexts)

el = driver.find_element(
    MobileBy.ANDROID_UIAUTOMATOR,
    'new UiSelector().text("师资团队")'
)
el = driver.find_element(
    MobileBy.XPATH, '//*[@text="师资团队"]'
)

el.click()

# 进入到了 webview
# 不能 直接定位
# 要切换到 web 模式，web 环境
# ['NATIVE_APP', 'WEBVIEW_com.lemon.lemonban']
# NAVIVE_APP 就是原生环境。
# 进入webview 页面了 'WEBVIEW_com.lemon.lemonban'
print(driver.contexts)

web_view_context = 'WEBVIEW_' + package_name
driver.switch_to.context(web_view_context)

# 可以进行元素定位了？？
# TODO； 原生环境当中的 text 是属性，用 @text=
# TODO: H5环境是函数  text()=
el = driver.find_element(By.XPATH, '//h1[text()="柠檬班"]')
print(el.text)

time.sleep(2)
driver.quit()
