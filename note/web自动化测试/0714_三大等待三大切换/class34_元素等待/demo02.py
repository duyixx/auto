"""显性等待"""

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
locator = ('xpath', '//*[text()="lemon..qq.com/"]')
elem = wait.until(expected_conditions.element_to_be_clickable(locator=locator))

print(elem.text)


# def wait_element_clickable(locator, driver, timeout=20, poll=0.5):
#     """等待元素被点击"""
#     wait = WebDriverWait(driver, timeout=timeout, poll_frequency=poll)
#     elem = wait.until(expected_conditions.element_to_be_clickable(locator=locator))
#     return elem

# driver.find_element_by_link_text("emon.ke.qq.com/")