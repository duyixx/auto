import unittest
from decimal import Decimal

import ddt
import json
from common import requests_handler
from middleware.handler import Handler


# 初始化数据
env_data = Handler()
test_data = env_data.excel.read_data("audit")

@ddt.ddt
class TestAudit(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # 普通用户登录
        cls.token = env_data.token
        cls.member_id = env_data.member_id

        # 管理员用户登录
        # 在 yaml 当中添加管理员的账号和密码
        # 封装 admin_login() 函数进行登录， 放到 handler 中。
        cls.admin_token = env_data.admin_token

    def setUp(self) -> None:
        self.db = env_data.db_mysql_class()
        # 添加项目
        self.loan_id = env_data.loan_id

    def tearDown(self) -> None:
        self.db.close()

    @ddt.data(*test_data)
    def test_audit(self, test_info):

        # 数据替换
        data = test_info["data"]
        if "#loan_id#" in data:
            data = data.replace("#loan_id#", str(self.loan_id))

        if "#pass_loan_id#" in data:
            pass_loan = self.db.query("SELECT * FROM futureloan.loan WHERE status !=1;")
            data = data.replace("#pass_loan_id#", str(pass_loan["id"]))

        data = eval(data)

        # 替换 headers
        headers = test_info["headers"]
        if "#admin_token#" in headers:
            headers = headers.replace("#admin_token#", self.admin_token)

        if "#token#" in headers:
            headers = headers.replace("#token#", self.token)

        headers = eval(headers)

        resp = requests_handler.visit(
            url=env_data.yaml["host"] + test_info["url"],
            method=test_info["method"],
            headers=headers,
            json=data
        )

        expected = json.loads(test_info["expected"])
        self.assertEqual(expected["code"], resp["code"])
        self.assertEqual(expected["msg"], resp["msg"])

        if resp["code"] == 0:
            # 验证数据库状态
            loan = self.db.query(
                "SELECT * FROM futureloan.loan WHERE id={}".format(self.loan_id)
            )
            self.assertEqual(expected["status"], loan["status"])
