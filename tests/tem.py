import json

import requests

# from common import requests_handler
# from middleware import handler

# res=requests.request(url="http://pftest.senguo.me/login",method="get")
#
# def trans_cookies(cookie:object):
#     cookie_str=""
#     for key in cookie.keys():
#         if cookie_str:
#             cookie_str+="; "
#         cookie_str+="=".join([str(key),cookie.get(str(key))])
#     return cookie_str
#
# cookie1=trans_cookies(res.cookies)
# res2=requests.request(url="http://pftest.senguo.me/login",method="post",
#                         headers={"Cookie":cookie1,"Origin": "http://pftest.senguo.me",
# "Referer": "http://pftest.senguo.me/manage/"},
#                       data={"action":"phone_password",
#                      "password":"8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92",
#                      "phone":"17386049001",
#                      "_xsrf":res.cookies.get("xsrf")})
#
#
# print("cookie1",cookie1)
# cookie2 = trans_cookies(res2.cookies)
# print("cookie2",cookie2)
# cookie3=cookie1+";"+cookie2
# print("cookie3",cookie3)
# print("res2",res2.json())
# data3='{"action":"sales_flow_record","batch_ids":[],"cashier_id_list":[],"customer_id_list":[],"from_date":"2020-09-15","goods_ids":[],"group_ids":[],"manual_only":0,"only_refund":0,"page":1,"fund_account_ids":[],"salesman_id_list":[],"supplier_id_list":[],"to_date":"2020-09-22","data_type":1,"need_sum":1,"customer_group_list":[]}'
#
# data3=json.loads(data3)
# print("data3",data3)
# res3=requests.request(url="http://pftest.senguo.me/boss/order",method="post",data=data3,headers={"Cookie":cookie3,"Origin": "http://pftest.senguo.me",
# "Referer": "http://pftest.senguo.me/manage/"},)
# print("res3",res3.cookies)
# print("res3",res3.json())
#
# data4='{"action":"get_list","page_size":30,"page":0,"company_type":[],"active_goods_owner":[],"sort_type":"","sort_rule":""}'
# data4=json.loads(data4)
# res4=requests.request(url="http://pftest.senguo.me/boss/supplier",method="post",data=data4,headers={"Cookie":cookie3,"Origin": "http://pftest.senguo.me",
#                                                                                                  "Referer": "http://pftest.senguo.me/manage/"},)
# print("res4",res4.cookies)
# print("res4",res4.json())
#
#
# import hashlib
# m = hashlib.sha256()
# m.update(b'1234567')
# print(m.hexdigest())

# import requests
# s=requests.Session()
# url="http://pftest.senguo.me/login"
# r=s.get(url=url)
# print("r",r.cookies,)
# print("s",s.cookies,"\n")
# r2=s.post(url="http://pftest.senguo.me/login",cookies=r.cookies,data={"action":"phone_password","phone":"17386049001","password":"8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92","_xsrf":r.cookies.get("_xsrf")})
# print("r2",r2.cookies,"\n",r2.json())
# print("s",s.cookies,"\n")
# data3={"action":"shop_change","shop_id":"423","log":"{\"1604748273758\":{\"front_end_pay_id\":\"LS1604748264929\",\"local_time\":\"2020-11-07 19:24:33\",\"opearte_obj\":{\"operate_text\":\"切换店铺\",\"changeShopId\":\"423\"},\"cashier_name\":\"星河图史\",\"shop_name\":\"极地雪西瓜\"},\"1604748275310\":{\"front_end_pay_id\":\"LS1604748275310\",\"local_time\":\"2020-11-07 19:24:35\",\"opearte_obj\":{\"operate_text\":\"newTempOrder\",\"operate_info_text\":\"前端新建订单\",\"front_end_pay_id\":\"LS1604748275310\"},\"cashier_name\":\"星河图史\",\"shop_name\":\"新毛利旧入库\"},\"1604748275311\":{\"front_end_pay_id\":\"LS1604748275310\",\"local_time\":\"2020-11-07 19:24:35\",\"opearte_obj\":{\"operate_text\":\"DOM ready\"},\"cashier_name\":\"星河图史\",\"shop_name\":\"新毛利旧入库\"},\"1604748275966\":{\"front_end_pay_id\":\"LS1604748275310\",\"local_time\":\"2020-11-07 19:24:35\",\"opearte_obj\":{\"operate_text\":\"切换接单\"},\"cashier_name\":\"星河图史\",\"shop_name\":\"新毛利旧入库\"},\"1604750059811\":{\"front_end_pay_id\":\"LS1604748275310\",\"local_time\":\"2020-11-07 19:54:19\",\"opearte_obj\":{\"operate_text\":\"logout\"},\"cashier_name\":\"星河图史\",\"shop_name\":\"新毛利旧入库\"},\"1604750061019\":{\"front_end_pay_id\":\"LS1604748275310\",\"local_time\":\"2020-11-07 19:54:21\",\"opearte_obj\":{\"operate_text\":\"sureLogout\",\"check_cash_cent\":0},\"cashier_name\":\"星河图史\",\"shop_name\":\"新毛利旧入库\"},\"1604750183223\":{\"front_end_pay_id\":\"LS1604750183221\",\"local_time\":\"2020-11-07 19:56:23\",\"opearte_obj\":{\"operate_text\":\"newTempOrder\",\"operate_info_text\":\"前端新建订单\",\"front_end_pay_id\":\"LS1604750183221\"},\"cashier_name\":\"星河图史\",\"shop_name\":\"极地雪西瓜\"},\"1604750183224\":{\"front_end_pay_id\":\"LS1604750183221\",\"local_time\":\"2020-11-07 19:56:23\",\"opearte_obj\":{\"operate_text\":\"DOM ready\"},\"cashier_name\":\"星河图史\",\"shop_name\":\"极地雪西瓜\"},\"1604750183981\":{\"front_end_pay_id\":\"LS1604750183221\",\"local_time\":\"2020-11-07 19:56:23\",\"opearte_obj\":{\"operate_text\":\"切换接单\"},\"cashier_name\":\"星河图史\",\"shop_name\":\"极地雪西瓜\"}}","_xsrf":"2|997feb1b|69bb0cea4970d7826ca593e3cc371d4c|1604436343"}
# r3=s.post(
#     url="http://pftest.senguo.me/accountant/home",
#     cookies=s.cookies,
#     data=data3
# )
# print("r3",r3.cookies,"\n",r3.json())
# print("s",s.cookies,"\n")
# import requests
#
# r = requests.get('http://pftest.senguo.me/static/images/logo1.png?v=7e96caee04e8a02301a80ff88c197dde')
# print(r.text)
# print(r.content)
# from PIL import Image
# from io import BytesIO
# i=Image.open(BytesIO(r.content))

# s = {"1":1,"2":2}
# for k,v in s.items():
#     print(v)
# class C():
#     s=requests.Session()
#     def p(self,sp):
#         print("aaaaa",sp)
#
# # s.p=p
# # s.p(s,123)
#     import types
#     s.psdsd=types.MethodType(p,s)
#
# C().psdsd
# s= requests.Session()
# # s.get("http://pftest.senguo.me/easy/login")
# res = s.post(url="http://pftest.senguo.me/api/easy/login/password/",data={"phone":"17386049010","password":"8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"})
# print(res.json())

import pytest

# def tf(x):
#     return x+2
#
# class TestClass:
#     def test_success(self):
#         assert tf(2)>3
#     def test_fail(self):
#         assert tf(0)>3


url="http://pftest.senguo.me/api/easy/data-center/today_transaction/get"
data=json.loads('{"to_date":"2020-11-14","data_type":0}')
from middleware.handler import Handler
h=Handler()
easy_session = h.login_easy({"phone":"17386049001","password":"123456"})
xx = easy_session.switch_shop(465)
print(xx.json())
# res=easy_session.request(url=url,method="get",data=data)
# print(res)
# print(res.json())
# print(easy_session.cookies)
