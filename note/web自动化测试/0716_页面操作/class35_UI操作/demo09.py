

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

driver.get('file:///D:/%E7%8F%AD%E7%BA%A7%E7%AE%A1%E7%90%86/python29%E6%9C%9F/class35_UI%E6%93%8D%E4%BD%9C/demo.html')

# 点击选择多喝热水
# pangheng = driver.find_element_by_xpath("//option[@value='pangheng']")
# pangheng.click()


# time.sleep(2)
# driver.quit()

# 先定位到 Select 元素
select_elem = driver.find_element_by_name("mselect")
s = Select(select_elem)
# 选择选项 value
# s.select_by_value("pangheng")
# 选择选项：通过文本内容
s.select_by_visible_text("胖哼")


time.sleep(2)