"""启动浏览器"""
import time

from selenium import webdriver

# 启动谷歌浏览器
# 依赖: 先安装好 chromedriver_for_87.0.4280.20_in_mac.exe 驱动
# 通过 excutable_path 配置 chromedriver_for_87.0.4280.20_in_mac 的路径
driver = webdriver.Chrome(executable_path=r"d:\chromedriver.exe")

# 打开网址
driver.get("http://zhihu.com")

# 窗口最大化
driver.maximize_window()

# 窗口最小化
driver.minimize_window()

# 设置窗口大小
driver.set_window_size(800, 600)

# 打开baidu
driver.get("http://baidu.com")

# 休眠2s
time.sleep(2)

# 后退
driver.back()
time.sleep(2)

# 前进
driver.forward()
time.sleep(2)

# 刷新
driver.refresh()
time.sleep(2)

# 退出浏览器
driver.quit()

