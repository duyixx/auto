import unittest
from decimal import Decimal

import ddt
import json
from common import requests_handler
from middleware.handler import Handler


# 初始化数据
env_data = Handler()
test_data = env_data.excel.read_data("recharge")


@ddt.ddt
class TestRecharge(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.token = env_data.token
        cls.member_id = env_data.member_id

    def setUp(self) -> None:
        self.db = env_data.db_mysql_class()

    def tearDown(self) -> None:
        self.db.close()

    @ddt.data(*test_data)
    def test_recharge(self, test_info):
        # 充值接口的访问
        data = test_info["data"]
        if "#member_id#" in data:
            data = data.replace("#member_id#", str(self.member_id))

        headers = test_info["headers"]

        if "#token#" in headers:
            headers = headers.replace("#token#", self.token)

        data = json.loads(data)
        headers = json.loads(headers)

        # 查询之前的余额 Decimal 类型
        user_info = self.db.query("SELECT leave_amount FROM futureloan.member WHERE id={}".format(self.member_id))
        before_money = user_info["leave_amount"]

        resp = requests_handler.visit(
            url= env_data.yaml["host"] + test_info["url"],
            method = test_info["method"],
            headers = headers,
            json=data
        )

        expected = json.loads(test_info["expected"])
        self.assertEqual(expected["code"], resp["code"])
        self.assertEqual(expected["msg"], resp["msg"])

        # 充值成功需要校验数据库
        # 充值之前的金额 +  充值金额 == 充值之后的余额
        if resp["code"] == 0:
            user_info = self.db.query("SELECT leave_amount FROM futureloan.member WHERE id={}".format(self.member_id))
            after_money = user_info["leave_amount"]
            # a = before_money + data["amount"] == after_money
            self.assertTrue(before_money + Decimal(str(data["amount"])) == after_money)

            # 精度控制（）

