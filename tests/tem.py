import json

import requests

from common import requests_handler
from middleware import handler

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