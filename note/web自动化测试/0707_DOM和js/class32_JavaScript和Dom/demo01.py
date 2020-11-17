#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽


a = '{"username": "Yuz", "age": 18, "gender": "male"}'

# gender
# 字符串（文档） ===》 对象
import json
b = json.loads(a)
print(b["gender"])


# python 发送定位元素的操作

def find_element_by_id(id):
    """通过 ID 查找元素"""
    # 发送请求给webdriver
    # requests.post("/find_element_by_id", data={"param": id})
    # webdriver 接收
    if url == "/find_element_by_id":
        # js 去执行
        document.getElementById(id)