#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# email: avgmax@foxmail.com
# wechat: avgmax
# author: JhonSmith
import json
import logging

import pytest
from middleware.handler import Handler

# logger = logging.getLogger()


test_data = Handler.excel.read_data("trans")


class TestTrans():
    """
    接口路径：/api/easy/data-center/today_transaction/get
    测试步骤：登录批发易—切换到店铺465—获取日经营走势—断言状态码和响应体
    """

    @pytest.mark.success122
    @pytest.mark.parametrize("test_info", test_data)
    def test_trance_success(self, test_info, handler, easy_session, logger):
        print("")
        logger.info("执行用例{}".format(test_info["case_id"]))

        # 处理数据
        data = json.loads(test_info["data"])
        url = handler.p2u(test_info["interface"])
        expected_data = json.loads(test_info["expected_data"])
        expected_status = test_info["expected_status"]
        method = test_info["method"]

        # 请求
        res = easy_session.request(url=url, params=data, method=method)

        # 断言
        try:
            assert res.status_code == expected_status + 1
        except Exception as e:
            logger.error("状态码错误")
            raise e
        if res.status_code == 200:
            try:
                assert res.json()["success"] == expected_data["success"]
            except Exception as e:
                logger.error("返回数据错误")
                raise e


if __name__ == "__main__":
    pytest.main(["--alluredir=allureout", "-m success1", "-s"])
