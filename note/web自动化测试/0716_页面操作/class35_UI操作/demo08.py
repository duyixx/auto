

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
# 最大化窗口
driver.maximize_window()

driver.get("http:/www.baidu.com")

e = driver.find_element_by_id("kw")


e.send_keys("雨泽")

# 发送回车按键
# e.send_keys(Keys.ENTER)

# 提交数据方法3：submit, 提交的数据必须要在 form 表单当中。
e.submit()

time.sleep(2)