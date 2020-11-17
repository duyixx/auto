

from appium import webdriver

caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "app":r"D:\data\柠檬班环境\app测试环境\应用apk包\Future-release-2018.apk"
}

# 初始化客户端
driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4723/wd/hub',
    desired_capabilities=caps,
)
