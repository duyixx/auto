# !/usr/bin/env python3
# -*-coding:utf-8 -*-
import copy
import hashlib
import json
import os
import types
from time import sleep

import requests
# from jsonpath import jsonpath
from pymysql.cursors import DictCursor

from common import yaml_handler, excel_handler, logging_handler, requests_handler
from common.db_handler import MysqlHandler, RedisHandler
from config import config


def trans_cookies(cookie):
    """将cookies转换为k1=v1; k2=v2; k3=v3; ...形式的字符串
    :param cookie: requests返回的对象.cookies
    :return: 转换后的cookie字符串
    """
    cookie_str = ""
    for key in cookie.keys():
        if cookie_str:
            cookie_str += "; "
        cookie_str += "=".join([str(key), cookie.get(str(key))])
    return cookie_str


def tran_pwd(row_pwd: str):
    m = hashlib.sha256()
    m.update(row_pwd.encode("utf-8"))
    return m.hexdigest()


class MysqlHandlerMid(MysqlHandler):
    """读取配置文件的选项， MysqlHandler"""

    def __init__(self):
        """初始化所有的配置项，从yaml当中读取
        db:
          host: "test.senguo.me"
          port: 3306
          user: "test"
          password: "senguo_mysql"
          charset: 'utf8'
        """
        db_mysql_config = Handler.yaml["db_mysql"]

        super().__init__(
            host=db_mysql_config["host"],
            port=db_mysql_config["port"],
            user=db_mysql_config["user"],
            password=db_mysql_config["password"],
            charset=db_mysql_config["charset"],
            cursorclass=DictCursor
        )


class RedisHandlerMid(RedisHandler):
    def __init__(self):
        """初始化所有的配置项，从yaml当中读取
        db:
          host: "test.senguo.me"
          port: 6379
          auth: "senguo_redis"
        """
        db_redis_config = Handler.yaml["db_redis"]
        super().__init__(
            host=db_redis_config["host"],
            port=db_redis_config["port"],
            auth=db_redis_config["auth"]
        )

    # 提取 token
    # jsonpath
    # token_str = jsonpath(res, "$..token")[0]
    # token_type = jsonpath(res, "$..token_type")[0]
    # member_id = jsonpath(res, "$..id")[0]
    # token = " ".join([token_type, token_str])
    # 提取 member_id
    # return {"token": token, "member_id": member_id}


class Handler(object):
    """初始化所有的数据。
    在其他的模块当中重复使用。
    是从 common 当中实例化对象。
    """
    # 加载 python 配置项
    conf = config

    # YAML 数据
    yaml = yaml_handler.read_yaml(os.path.join(config.CONFIG_PATH, "config.yml"))

    # excel 数据
    __excel_path = conf.DATA_PATH
    __excel_file = yaml["excel"]["file"]
    excel = excel_handler.ExcelHandler(os.path.join(__excel_path, __excel_file))

    # logger
    __logger_config = yaml["default_logger"]
    logger = logging_handler.Logger(__logger_config)
    # mysql 应不应该放到Handler, 不行。 db 对象。
    # 不存储对象，我存储类. TODO: 没有听明白的可以不用这一行，使用的时候直接导入
    # MysqlHandlerMid
    MysqlDbClient = MysqlHandlerMid
    RedisDbClient = RedisHandlerMid

    def request_to_login(self, session, url, data, method="get", headers=None):
        """登录结果判断"""

        web_aft_login = session.request(url=url, data=data, method=method, headers=headers)
        if web_aft_login.json()["success"] is None:
            self.logger.error("登录账号时出现意料之外的情况, user:{}".format(data["phone"]))
            raise Exception(format(web_aft_login.json()))
        if web_aft_login.status_code == 200 and web_aft_login.json()["success"] is True:
            self.logger.info("登录成功, 账号：{}".format(data["phone"]))
            return session
        if web_aft_login.json()["success"] is False:
            self.logger.warning("登录失败, 账号：{}".format(data["phone"]))
            raise Exception(format(web_aft_login.json()))
        else:
            self.logger.error("登录账号时出现意料之外的情况")
            raise Exception("unknown error: {}".format(web_aft_login.json()))

    def login_backend(self, user_to_login=None):
        """登录后台测试账号"""
        session = requests.Session()

        # def backend_switch_shop(session: requests.Session(), sp_id: int):
        #     """后台切换店铺"""
        #     res = session.post(
        #         url='http://centertest.senguo.me/api/shop?method=set_shop_cookie',
        #         data={"shop_type": "pf", "shop_id": sp_id}
        #     )
        #     return res
        #
        # def switch_shop(s_self, sp_id):
        #     """用于切换店铺: session.backend_switch_shop()"""
        #     return backend_switch_shop(session=session, sp_id=sp_id)

        def switch_shop(s_self, sp_id):
            res = session.request(
                url=self.yaml["host"]["center"] + '/api/shop?method=set_shop_cookie',
                method="post",
                data={"shop_type": "pf", "shop_id": sp_id}
            )
            return res

        session.switch_shop = types.MethodType(switch_shop, session)

        url = self.yaml["host"]["pf"] + "/login"
        # request_data
        web_to_login = session.request(url=url, method="get")
        default_user = copy.deepcopy(self.yaml["users"]["default_user"])
        data = user_to_login if user_to_login else default_user
        data["password"] = tran_pwd(data["password"])
        data["_xsrf"] = web_to_login.cookies.get("_xsrf")
        data["action"] = "phone_password"
        return self.request_to_login(session=session, url=url, data=data, method="post")

    def login_easy(self, user_to_login=None):
        """登录批发易"""
        session = requests.Session()

        # def boss_switch_shop(session: requests.Session(), sp_id: int):
        #     """老板助手切换店铺"""
        #     res = session.request(
        #         url="http://pftest.senguo.me/boss/home",
        #         method="post",
        #         data={"action": "shop_change", "shop_id": sp_id}
        #     )
        #     return res
        #
        # def switch_shop(s_self, sp_id):
        #     """用于切换店铺: session.boss_switch_shop()"""
        #     return boss_switch_shop(session=session, sp_id=sp_id)

        def switch_shop(s_self, sp_id):
            res = session.request(
                url=self.yaml["host"]["pf"] + "/boss/home",
                method="post",
                data={"action": "shop_change", "shop_id": sp_id}
            )
            return res

        session.switch_shop = types.MethodType(switch_shop, session)

        url = self.yaml["host"]["pf"] + "/api/easy/login/password/"
        # request_headers
        # headers = {"Content-Type": "application/json"}
        # request_data
        default_user = copy.deepcopy(self.yaml["users"]["default_user"])
        data = user_to_login if user_to_login else default_user
        data["password"] = tran_pwd(data["password"])
        return self.request_to_login(session=session, url=url, data=data, method="post")

    def replace_data(self, data):
        """用于将用例data中pattern匹配的字符串修改为handler()中以该字符串为名属性的值"""
        import re
        patten = r"#(.*?)#"
        while re.search(patten, data):
            key = re.search(patten, data).group(1)
            value = getattr(self, key, "")
            data = re.sub(patten, str(value), data, 1)
        return data

    def p2u(self, path: str):
        """拼接项目host和接口路径"""
        return "".join((self.yaml["host"]["pf"], path))


# @property
# def token(self):
#     return self.login(self.yaml["users"]["user0"])["token"]
# @property
# def user_cookies(self, user_to_login=None):
#     """
#     to get a new logined cookie
#     :param user_to_login: eg. {"phone":"12345678901","password":"123456 to encode"}
#     :return: response object
#     """
#     return self.__login(user_to_login).cookies

# @property
# def signer_role_list(self):
#     return self.login(self.yaml["users"]["user0"]).json()["role_list"]

# @property
# def admin_token(self):
#     return self.login(self.yaml["admin_user"])["token"]

# @property
# def loan_id(self):
#     return self.add_loan()

# def __login(self, user_to_login=None):
#     """登录测试账号"""
#     url = self.yaml["host"]["pf"] + "/login"
#     default_user = copy.deepcopy(self.yaml["users"]["user0"])
#     m = hashlib.sha256()
#     m.update(default_user["password"].encode("utf-8"))
#     default_user["password"] = m.hexdigest()
#     data = user_to_login if user_to_login else default_user
#     cookie_from_login_web = requests.request(url=url, method="get").cookies
#     headers = {"Cookie": trans_cookies(cookie_from_login_web),
#                "Origin": "http://pftest.senguo.me",
#                "Referer": "http://pftest.senguo.me/manage/"}
#     data["action"] = "phone_password"
#     data["_xsrf"] = cookie_from_login_web.get("_xsrf")
#     res = requests_handler.visit(url=url, method="post", headers=headers, json=data)
#     if res.json()["success"]:
#         sleep(1.2)
#         return res
#     else:
#         self.logger.warning("账号{phone}登录失败".format(phone=data["phone"]))
#         raise Exception(res.json())

# def login_admin(self):
#     """登录admin测试账号"""
#     res = requests_handler.visit(
#         url=Handler.yaml["host"] + "/member/login",
#         method="post",
#         headers={"X-Lemonban-Media-Type": "lemonban.v2"},
#         json=Handler.yaml["admin_user"]
#     )
#
#     # 提取 token
#     # jsonpath
#     token_str = jsonpath(res, "$..token")[0]
#     token_type = jsonpath(res, "$..token_type")[0]
#     token = " ".join([token_type, token_str])
#     # 提取 member_id
#     return token

# def add_loan(self):
#     data = {"member_id": self.member_id,
#             "title": "木森借钱买飞机",
#             "amount": 2000,
#             "loan_rate": 12.0,
#             "loan_term": 3,
#             "loan_date_type": 1,
#             "bidding_days": 5}
#     # 发送请求，添加项目
#     res = requests_handler.visit(
#         url=Handler.yaml["host"] + "/loan/add",
#         method="post",
#         headers={"X-Lemonban-Media-Type": "lemonban.v2", "Authorization": self.token},
#         json=data
#     )
#
#     # 提取项目的id给审核的用例使用
#     return jsonpath(res, "$..id")[0]

# def audit_loan(self):
#     """审核项目"""
#     data = {"loan_id": self.loan_id, "approved_or_not": True}
#
#     resp = requests_handler.visit(
#         url=Handler.yaml["host"] + "/loan/audit",
#         method="patch",
#         headers={"X-Lemonban-Media-Type": "lemonban.v2", "Authorization": self.admin_token},
#         json=data
#     )
#     print(resp)
#     # return self.loan_id
#
# def recharge(self):
#     """充值"""
#     data = {"member_id": self.member_id, "amount": 500000}
#
#     resp = requests_handler.visit(
#         url=Handler.yaml["host"] + "/member/recharge",
#         method="post",
#         headers={"X-Lemonban-Media-Type": "lemonban.v2", "Authorization": self.token},
#         json=data
#     )


if __name__ == '__main__':
    h = Handler()
    # h.logger.info("asdsfasdafasdf")
    # m_str = '{"member_id": #member_id#,"token":"#token#", "loan_id": #loan_id#, "admin_token": #admin_token#,
    # "random_prop":"#random#"}' a = h.replace_data(m_str) print(a) print(h.MysqlDbClient().query("select * from
    # senguopf.shop where id < 200;")) print(h.RedisDbClient().find_keys())
    # c = h.login()
    # print(c.cookies)
    # print("xx", c.json()["role_list"])
    hs1 = h.login_easy({"phone": "17386049001", "password": "123456"})
    hs2 = h.login_easy({"phone": "18162664593", "password": "senguo2020"})
    c = hs1.switch_shop(105)
    hs2.switch_shop(431)

    print(hs1.cookies)
    print(hs2.cookies)
    print(hs1.cookies)
    # print(c)

    # hs3 = h.login_easy({"phone": "17386049010", "password": "123456"})
    # print(hs3.cookies)
    # url="http://pftest.senguo.me/api/easy/shop/register/"
    # data={"shop_name":"qwertyuipfgh0","shop_img":"pfeasy/MTYwNDc4MDEwMzgyMi0xYmU2M2ZhYw==.jpg","business_license":"pfeasy/MTYwNDc4MDEwNjAyMS0zNDgzYzI2Nw==.jpg","shop_province":420000,"shop_city":420100,"shop_county":420106,"shop_address":"asdasd","latitude":30.58108413,"longitude":114.3162001,"inviter_phone":"","description":""}
    # headers={"Content-Type":"application/json; charset=UTF-8"}
    # re = hs3.request(url=url,headers=headers, method="post", json=data)
    # print(re.json())
    # re = hs.get(url="http://pftest.senguo.me/easy/api/easy/shop/register/")
    # print(hs.cookies)
    # print(hs.cookies)
    # print("coo", hs)
    # print("t", trans_cookies(hs.cookies))

    # data_path = Handler.conf.DATA_PATH
    # print(Handler.yaml["excel"]["file"])
    #
    # # print(Handler.__excel_path)
    # # print(Handler.__excel_path)
    # print(Handler.logger)

    # 模块本来就是对象。
    # config.DATA_PATH
    # # 变量赋值
    # conf = config
    # db = MysqlHandlerMid()
    # data = db.query("SELECT * FROM futureloan.member LIMIT 10;")
    # print(data)

    # print(Handler.db_mysql_class)
    # print(Handler.db_mysql_class().query("SELECT * FROM futureloan.member LIMIT 10;"))

    # 测试login 函数
    # print(login())

    # print(Handler().admin_token())

    # h = Handler()
    # data = '{"loan_id": "#loan_id#", "member_id": "#member_id#"}'
    # new = h.replace_data(data)
    # print(new)
# data = {"s": 1, "d": 2}
# h.replace_data(data)
