"""iframe 切换"""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()

driver.get('file:///D:/%E7%8F%AD%E7%BA%A7%E7%AE%A1%E7%90%86/python29%E6%9C%9F/class35_UI%E6%93%8D%E4%BD%9C/demo.html')


# 先找到要切换的 iframe
iframe_elem = driver.find_element_by_xpath('//iframe[@src]')

driver.switch_to.frame(iframe_elem)

# 定位 baidu iframe 当中的 input kw
input_elem  = driver.find_element_by_id("kw")
print(input_elem)

# 要定位主页面的元素，必须要切换回主页面
driver.switch_to.default_content()
driver.find_element_by_id("hello")

# 个别特殊情况：

# iframe 等待。显性等待
WebDriverWait(driver, 30, poll_frequency=0.5).until(
    expected_conditions.frame_to_be_available_and_switch_to_it(iframe_elem)
)





