"""xpath"""


from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

e = driver.find_element_by_class_name("s_ipt_wr")
print(e)

# 通过 xpath 定位新闻
# e = driver.find_element("xpath", "//a[text()='新闻']")
# e.click()
## 通过 xpath contains 定位新闻
e = driver.find_element("xpath", "//a[contains(text(), '新')]")
e.click()
