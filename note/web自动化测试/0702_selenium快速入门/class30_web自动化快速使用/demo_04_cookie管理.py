"""requests cookie 管理，

session: 开启浏览器

/login
/invest

分两次：2个会话，第一次的登录状态会传到第二次去？？ 不会
1次会话： 第一次访问login ,   可以。

requests 是可以用 session 记录 cookie
"""
# 基于 cookie 机制的登录

import requests
requests.request()


s = requests.session()

# login 获取到的 cookie 自动保存到 session
s.request("get", url="/login")

s.request("get", url="/invest")

