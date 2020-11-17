import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

package_name = "com.lemon.lemonban"

caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": package_name,
    "appActivity": ".activity.MainActivity",
    "automationName": "UiAutomator2",
}


# 初始化客户端
driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4723/wd/hub',
    desired_capabilities=caps,
)

# 隐式等待
driver.implicitly_wait(20)


# 点击我的
me = driver.find_element(MobileBy.ID, 'com.lemon.lemonban:id/navigation_my')
me.click()

# 点击登录
login = driver.find_element(MobileBy.ID,
                            'com.lemon.lemonban:id/fragment_my_lemon_avatar_layout')
login.click()

#
login_btn = driver.find_element(MobileBy.ID, 'com.lemon.lemonban:id/btn_login')
login_btn.click()

# toast 的xpath定位
# 1. xpath,   '//*[contains(@text, "手机号码或密码不能为空")]'
# 2. xpath toast的固定表示  '//*[//android.widget.Toast]'
# TODO: Toast 定位如果要用显示等待
# toast定位的显式等待只能用 presence, 不能用 visiblve（因为会自动消失）
el = driver.find_element(By.XPATH, '//*[contains(@text, "手机号码或密码不能为空")]')
print(el.text)

time.sleep(3)
driver.quit()