import json
import unittest
import ddt
from common import requests_handler
from middleware.handler import Handler

# 初始化
logger = Handler.logger
test_data = Handler.excel.read_data("invest")
env_data = Handler()


@ddt.ddt
class LoginTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.token = env_data.token
        cls.member_id = env_data.member_id

    def setUp(self) -> None:
        self.db = env_data.db_mysql_class()
        # env_data.loan_id
        setattr(env_data, "loan_id", env_data.add_loan())
        # 添加项目
        # env_data.loan_id
        # 审核项目
        env_data.audit_loan()
        # 充值
        env_data.recharge()

    def tearDown(self) -> None:
        self.db.close()

    @ddt.data(*test_data)
    def test_invest(self, test_info):
        # 用handler()中同名属性的值替换用例data中被标记的数据
        data = test_info["data"]
        data = env_data.replace_data(data)
        data = eval(data)

        # 替换 token ,存在 headers 当中
        headers = test_info["headers"]
        headers = env_data.replace_data(headers)
        headers = json.loads(headers)

        # 查询之前的余额
        if test_info["check_sql"]:
            member = self.db.query("SELECT * FROM futureloan.member WHERE id={}".format(self.member_id))
            money_before = member['leave_amount']

            before_loan = self.db.query(
                "SELECT * FROM futureloan.invest WHERE member_id={}".format(self.member_id),
                one=False
            )

        # 访问接口
        resp = requests_handler.visit(
            url=env_data.yaml["host"] + test_info["url"],
            method=test_info["method"],
            headers=headers,
            json=data
        )
        print(data)
        print(resp)
        expected = json.loads(test_info["expected"])
        self.assertEqual(expected["code"], resp["code"])
        self.assertEqual(expected["msg"], resp["msg"])

        if resp["code"] == 0:
            after_loan = self.db.query(
                "SELECT * FROM futureloan.invest WHERE member_id={}".format(self.member_id),
                one=False
            )
            # 断言投资记录是否增加一条 invest
            self.assertEqual(len(before_loan) + 1, len(after_loan))

            # 断言用户余额是否减少
            member_after = self.db.query("SELECT * FROM futureloan.member WHERE id={}".format(self.member_id))
            money_after = member_after['leave_amount']
            self.assertEqual(money_before - data["amount"], money_after)

        # 接口自动化一定就比手工测试要高级

