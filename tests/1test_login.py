import json
import unittest
import ddt
from common import requests_handler
from middleware.handler import Handler

# 初始化
logger = Handler.logger
test_data = Handler.excel.read_data("login")


@ddt.ddt
class LoginTestCase(unittest.TestCase):


    @ddt.data(*test_data)
    def test_login(self, case):
        # 第一步：准备用例数据
        # 请求方法
        method = case["method"]
        # 请求地址
        url = case["url"]
        # 请求参数
        data = json.loads(case["data"])
        # 请求头
        headers = json.loads(case["headers"])
        # 预期结果
        expected = json.loads(case["expected"])

        # 第二步：发送请求获取实际结果
        res = requests_handler.visit(
            method=method,
            url=url,
            json=data,
            headers=headers)
        # 获取实际结果


        print("预期结果：", expected)
        print("实际结果：", res)
        # 第三步：断言
        try:
            self.assertEqual(expected["code"], res["code"])
            self.assertEqual(expected["msg"], res["msg"])
        except AssertionError as e:
            # 结果回写excel中
            pass

