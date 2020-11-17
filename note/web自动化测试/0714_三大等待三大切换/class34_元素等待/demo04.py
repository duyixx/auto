"""iframe 切换"""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()

driver.get('file:///D:/%E7%8F%AD%E7%BA%A7%E7%AE%A1%E7%90%86/python29%E6%9C%9F/class34_%E5%85%83%E7%B4%A0%E7%AD%89%E5%BE%85/demo.html')



# 先找到要切换的 iframe
iframe_elem = driver.find_element_by_xpath('//iframe[@src]')

driver.switch_to.frame(iframe_elem)

# 定位 baidu iframe 当中的 input kw
input_elem  = driver.find_element_by_id("kw")
print(input_elem)