#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

from selenium import webdriver


driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 元素定位
driver.find_element_by_id("kw")

