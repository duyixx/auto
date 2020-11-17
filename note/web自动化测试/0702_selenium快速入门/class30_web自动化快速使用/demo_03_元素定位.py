import time

from selenium.webdriver import Chrome

driver = Chrome()

driver.get("http://www.baidu.com")

# 元素定位
# 元素: 网页页面的一个组件
# 定位： 查找要操作的元素的过程
# 8 大元素定位方式。
# 定位
input_elem = driver.find_element_by_id("kw")

# 输入
input_elem.send_keys("柠檬班")


time.sleep(2)


