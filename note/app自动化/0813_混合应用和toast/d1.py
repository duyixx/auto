import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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

# 获取现在的页面名字
print(driver.current_activity)
# 获取包名
print(driver.current_package)
# 获取现在上下文环境, 原生环境和 web 环境，和 web当中的 iframe 差不多
print(driver.current_context)
# 获取所有的上下文华景
print(driver.contexts)

# 无法使用。要进入web环境使用
print(driver.current_url)

# 跳转到页面,测试很少用，因为要模拟用户的路径，
# driver.start_activity(package,  activity)

# 后台运行 5s, 一直在后台运行， -1
driver.background_app(5)

# MultiAction


# 输入键盘
# web ==> driver.send_keys() Keys
# 当你需要用到对应的 keycode, 键盘操作的时候，网上查找键位的 code 码表。
# driver.send_keys(Keys.SPACE)

# 方法二，封装 MobileKeys 类，放到 common 当中。下次直接用
class MobileKeys:
    ENTER = 66
    HOME = 3

driver.press_keycode(MobileKeys.ENTER)

# driver.click()
# driver.hide_keyboard()
# 隐藏键盘，智能手机都是虚拟键盘。
# app键盘会把内容挡住。