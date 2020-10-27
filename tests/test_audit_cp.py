import json
import unittest
import ddt
from common import requests_handler
from middleware.handler import Handler

# 初始化
logger = Handler.logger
test_data = Handler.excel.read_data("audit")
env_data = Handler()


@ddt.ddt
class LoginTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # 普通用户登录
        cls.token = env_data.token
        cls.member_id = env_data.member_id

        # admin 登录
        cls.admin_token = env_data.admin_token

    def setUp(self) -> None:
        self.db = env_data.db_mysql_class()

        # 添加标
        self.loan_id = env_data.loan_id

    def tearDown(self) -> None:
        self.db.close()


    @ddt.data(*test_data)
    def test_add(self, test_info):
        data = test_info["data"]
        if "#loan_id#" in data:
            # loan_id = 9
            data = data.replace("#loan_id#", str(self.loan_id))

        # 动态生成一个已经不是审核状态的标。
        # 数据库中查找 status != 1,
        if "#pass_loan_id#" in data:
            pass_loan = self.db.query("SELECT * FROM futureloan.loan WHERE status !=1;")
            data = data.replace("#pass_loan_id#", str(pass_loan["id"]))

        headers = test_info["headers"]

        if "#admin_token#" in headers:
            headers = headers.replace("#admin_token#", self.admin_token)

        data = eval(data)
        headers = json.loads(headers)

        # 查询之前的余额

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
            # loan_id = 8, status = 2
            loan = self.db.query("SELECT * FROM futureloan.loan WHERE id={};".format(self.loan_id))
            self.assertEqual(loan["status"], expected["status"])

            # env_data.pass_loan_id = loan["id"]



