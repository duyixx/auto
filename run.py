"""运行所有的用例。"""
import os
import unittest
from datetime import datetime
from config import config
from libs.HTMLTestRunnerNew import HTMLTestRunner

# 加载用例
loader = unittest.TestLoader()
suites = loader.discover(config.CASE_PATH)

# 测试报告的路径
ts = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
reports_filename = "reports-{}.html".format(ts)
reports_path = os.path.join(config.REPORTS_PATH, reports_filename)

# 运行用例
with open(reports_path, mode='wb') as f:
    runner = HTMLTestRunner(
        f,
        title="python29期测试报告",
        description="测试报告",
        tester="yuz"
    )
    runner.run(suites)
