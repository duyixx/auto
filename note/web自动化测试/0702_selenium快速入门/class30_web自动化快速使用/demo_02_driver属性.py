from selenium.webdriver import Chrome

driver = Chrome()

driver.get("http://www.baidu.com")

# 网页标题
print(driver.title)

# 网页的URL
print(driver.current_url)

# 所有的窗口句柄
# 你开了多少个标签页（窗口） 就有多少个元素存在列表当中
print(driver.window_handles)

# 当前窗口句柄
print(driver.current_window_handle)

# 当前页面的源代码
# 前端工程师编写的页面（HTML）
# HTML是我们进行 web 自动化测试的依据。
print(driver.page_source)



