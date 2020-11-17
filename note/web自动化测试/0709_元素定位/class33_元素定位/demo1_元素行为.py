from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

# 元素定位
# 得到的返回值是一个 WebElement 的python对象。==》元素
# 方法1：id

# input_elems = driver.find_elements_by_id("kwffw")
# print(input_elems)
#
#
# input_elem = driver.find_element_by_id("kwffw")
# print(input_elem)
#
# # 获取元素的属性 ==》 WebElement()
# print(input_elem.get_attribute('name'))
# # 在python当中现在还不能直接修改元素，selenium 没有封装对应的方法。
#
# if not driver.find_elements_by_id("kwffw") :
#     print("该元素不存在")
# else:
#     print("该元素存在")


# name 属性
driver.find_element_by_name("wd")
driver.find_elements_by_name("wd")

# class_name
driver.find_element_by_class_name("s_ipt")
driver.find_element_by_class_name("s_ipt")

# 通过超链接的文本定位
e = driver.find_element_by_link_text("新闻")
e.click()

e = driver.find_element_by_partial_link_text("新")
e.click()

# tagname
driver.find_element_by_tag_name("input")

# 6 种元素定位方式
# 用的最多的：id, name, class_name,
# id 是唯一的。
# name, 用户输入经常会带 name 属性。
# class_name, 因为也经常出现