"""Alert切换"""
#
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()

driver.get('file:///D:/%E7%8F%AD%E7%BA%A7%E7%AE%A1%E7%90%86/python29%E6%9C%9F/class35_UI%E6%93%8D%E4%BD%9C/demo_alert.html')

hello_elem = driver.find_element_by_id('hello')
hello_elem.click()

time.sleep(2)
# 切换到 alert
malert = driver.switch_to.alert
# 点击确认
time.sleep(2)
malert.accept()
# malert.dismiss()

# 也有等待的条件
# expected_conditions.alert_is_present()
WebDriverWait(driver, 30, poll_frequency=0.5).until(
    expected_conditions.alert_is_present()
)