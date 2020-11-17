"""窗口切换"""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()

driver.get('http://www.baidu.com')

e = driver.find_element_by_id("kw")
e.send_keys("柠檬班")

# 点击百度一下
driver.find_element_by_id('su').click()

# 显性等待
# 第一步：设置定时器
wait = WebDriverWait(driver, 5, poll_frequency=0.5)
# 第二部：设置满足的条件
# locator =
locator = ('xpath', '//*[text()="lemon.ke.qq.com/"]')
elem = wait.until(expected_conditions.element_to_be_clickable(locator=locator))

elem.click()



# 获取现在的 URL 地址，http://lemon.ke.qq.com/
print(driver.current_url)

# 窗口切换, 窗口句柄
print(driver.window_handles)

driver.switch_to.window(driver.window_handles[-1])

print(driver.current_url)