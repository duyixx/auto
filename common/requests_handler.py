# 暂时没什么用

# import jsonpath as jsonpath
import socket

import requests


def visit(url="",
          method='get',
          params=None,
          data=None,
          json=None,
          rejson=0,
          request_wait=30,
          **kwargs
          ):
    """访问接口。返回字典 。 res.json()"""
    res = requests.request(
        method=method,
        url=url,
        params=params,
        data=data,
        json=json,
        timeout=request_wait,
        **kwargs
    )

    try:
        if rejson:
            return res.json()
        return res
    except Exception as e:
        return None
#
#
if __name__ == '__main__':
    pass
#     # res = visit(url='http://passporttest.senguo.me/api/login?method=login_by_wx_ticket',
#     #       method='get')
#     # print(res)
#     import requests
#     res=requests.post(url='http://pftest.senguo.me/login',
#                       data={"action":"phone_password","phone":"18162664593","password":"8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92","_xsrf":"2|88b4f88f|44ad7190003bfa521b5bdccbba562665|1603556879"})
#     print(res.status_code)
#     print(res.json())
#     coo=res.cookies
#     res2 = visit(url='http://pftest.senguo.me/login',
#           data={"action":"phone_password","phone":"18162664593","password":"8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92","_xsrf":"2|88b4f88f|44ad7190003bfa521b5bdccbba562665|1603556879"},
#           method="post",
#                  rejson=0
#           )
#     print("visit",res2)
#     print("v",res2.cookies)
#     print("v", res2.status_code)
#     print("v", res2.json())
#     # print(coo)
#     # res=requests.post(url='http://pftest.senguo.me/boss/order',
#     #                   data={"action":"sales_flow_record","batch_ids":[],"cashier_id_list":[],"customer_id_list":[],"from_date":"2020-07-27","goods_ids":[],
#     #                   "group_ids":[],"manual_only":0,"only_refund":0,"page":0,"fund_account_ids":[],"salesman_id_list":[],
#     #                   "supplier_id_list":[],"to_date":"2020-10-25","data_type":0,"need_sum":0,"customer_group_list":[]},
#     #                   cookies=coo
#     #                   )
#     # print(res.json())
#     login = visit(method="post",
#                 url='http://pftest.senguo.me/login',
#                 data={"action":"phone_password","phone":"18162664593","password":"8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92","_xsrf":"2|88b4f88f|44ad7190003bfa521b5bdccbba562665|1603556879"},
#                 )
#     cookies=login.cookies
#     print("cookies",cookies)
#     res=visit(method='post',
#               url='http://pftest.senguo.me/boss/order',
#               cookies=cookies,
#               data={"action":"sales_flow_record","batch_ids":[],"cashier_id_list":[],"customer_id_list":[],"from_date":"2020-07-27","goods_ids":[],
#                       "group_ids":[],"manual_only":0,"only_refund":0,"page":0,"fund_account_ids":[],"salesman_id_list":[],
#                       "supplier_id_list":[],"to_date":"2020-10-25","data_type":0,"need_sum":0,"customer_group_list":[]}
#               )
#     print(res.status_code)
#     print(res.text)
#     print(res.json())
#     print(jsonpath.jsonpath(res.json(),"$.data_list"))
#     res=visit(url="http://pftest.senguo.me",method="get")
#     print("res",res)
#     print("res.json()",res.json())