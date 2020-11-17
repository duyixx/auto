import time

from selenium import webdriver

driver = webdriver.Chrome()
# 设置隐性等待的超时时间
driver.implicitly_wait(10)

driver.get('http://www.baidu.com')

e = driver.find_element_by_id("kw")
e.send_keys("柠檬班")

# 点击百度一下
driver.find_element_by_id('su').click()

# 等待元素加载完成
# time.sleep(0.5)
driver.find_element_by_link_text("emon.ke.qq.com/")


# time.sleep(1)
# driver.find_element()


