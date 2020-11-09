import json
import unittest
import ddt
import requests

from common import requests_handler
from middleware.handler import Handler

# 初始化
logger = Handler.logger
test_data = Handler.excel.read_data("shop_register")
env_data = Handler()


@ddt.ddt
class RegTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        pass
        # cls.token = env_data.token
        # cls.member_id = env_data.member_id

    def setUp(self) -> None:
        self.db = env_data.MysqlDbClient()
        self.session = env_data.login_easy()
    def tearDown(self) -> None:
        self.db.close()
        self.session.close()


    @ddt.data(*test_data)
    def test_add_success(self, test_info):
        data = json.loads(test_info["data"])
        headers = json.loads(test_info["headers"])
        url=env_data.yaml["host"]["pf"]+"/"+test_info["interface"]
        print(self.session.cookies)

        reg_res = self.session.post(url=url,headers=headers,json=data)
        print(reg_res.status_code)
        print(reg_res.json())
        assert reg_res.status_code==200
        print(reg_res.json())
        assert reg_res.json()["success"] is True
        #
        # if "#member_id#" in data:
        #     data = data.replace("#member_id#", str(self.member_id))
        #
        # headers = test_info["headers"]
        #
        # if "#token#" in headers:
        #     headers = headers.replace("#token#", self.token)
        #
        #
        # if test_info["check_sql"]:
        #     before_loan = self.db.query(
        #         "SELECT * FROM futureloan.loan WHERE member_id={}".format(self.member_id),
        #         one=False
        #     )
        #
        # data = eval(data)
        # headers = json.loads(headers)
        #
        # # 查询之前的余额
        #
        # resp = requests_handler.visit(
        #     url=env_data.yaml["host"] + test_info["url"],
        #     method=test_info["method"],
        #     headers=headers,
        #     json=data
        # )
        #
        # expected = json.loads(test_info["expected"])
        # self.assertEqual(expected["code"], resp["code"])
        # self.assertEqual(expected["msg"], resp["msg"])
        #
        # if resp["code"] == 0:
        #     after_loan = self.db.query(
        #         "SELECT * FROM futureloan.loan WHERE member_id={}".format(self.member_id),
        #         one=False
        #     )
        #     self.assertEqual(len(before_loan) + 1, len(after_loan))




