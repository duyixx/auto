#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
import unittest
import ddt
import json

from common import requests_handler
from middleware.handler import Handler

# 初始化数据
logger = Handler.logger
test_data = Handler.excel.read_data("register_v0")


@ddt.ddt
class TestRegister(unittest.TestCase):

    @ddt.data(*test_data)
    def test_register(self, test_info):

        # 判断测试用例数据有没有 #phone#, 如果有，就要替换成动态生成的手机号码。
        if "#phone#" in test_info["data"]:
            phone = self.random_phone()
            test_info["data"] = test_info["data"].replace("#phone#", phone)

        # 访问接口
        data = json.loads(test_info["data"])
        resp = requests_handler.visit(
            url=test_info["url"],
            method=test_info["method"],
            json=data,
            headers=json.loads(test_info["headers"])
        )
        expected_dict = json.loads(test_info["expected"])

        try:
            for key, value in expected_dict.items():
                self.assertEqual(value, resp[key])

            if resp["code"] == 0:
                # 查询数据当中有没有插入手机号码注册成功的记录
                # db = Handler.db_mysql_class()
                sql_code = "SELECT * from futureloan.member WHERE mobile_phone={};".format(data["mobile_phone"])
                user = self.db.query(sql_code)
                self.assertTrue(user)

            logger.info("测试用例通过")
        except AssertionError as e:
            logger.error("测试用例无法通过:{}".format(e))
            raise e

    def random_phone(self):
        """随机生成一个动态的手机号码。
        注册成功的用例当中，需要一个没有被注册过的手机号。需要查询数据库。
        """
        # 第一步，随机生成手机号
        # 前面 2 位  13
        import random
        while True:
            phone = "13"
            for i in range(9):
                num = random.randint(0, 9)
                phone += str(num)
            print(phone)

            # 查询数据库，如果数据库当中有这个手机号，再次生成，while,
            # from middleware.handler import MysqlHandlerMid
            # db = MysqlHandlerMid()
            db = Handler.db_mysql_class()

            sql_code = "SELECT * FROM futureloan.member WHERE mobile_phone={};".format(phone)
            phone_record = db.query(sql_code)

            if not phone_record:
                db.close()
                return phone
            db.close()
