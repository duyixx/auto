"""鼠标操作"""
#
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
# 最大化窗口
driver.maximize_window()

driver.get("http:/www.baidu.com")

# 步骤1：移动到设置
setting = driver.find_element_by_id('s-usersetting-top')
# 鼠标悬停到 setting 元素

action_chains = ActionChains(driver)
# TODO: perform() 一定要加，否则动作不会生效
action_chains.move_to_element(setting).click().perform()

time.sleep(2)

adv_setting = driver.find_element_by_link_text('高级搜索')
adv_setting.click()

driver.quit()


# 双击
# ac = ActionChains(driver)
# ac.double_click(e).perform()
#
# ac.context_click(e).perform()
#
# ac.drag_and_drop(e1, e2).perform()

# 链式调用