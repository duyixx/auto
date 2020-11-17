"""bg s_ipt_wr quickdelete-wrap"""

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

e = driver.find_element_by_class_name("s_ipt_wr")
print(e)


e = driver.find_element("id", 'kw')
e = driver.find_element_by_id('kw')

