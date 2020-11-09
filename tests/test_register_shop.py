#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# email: avgmax@foxmail.com
# wechat: avgmax
# author: JhonSmith
import logging

import pytest
from data.reg_data import data as test_data
from data.reg_data import url
from middleware.handler import Handler

# logger = logging.getLogger()
class TestRegister():
    """
    登录批发易
    注册店铺
    """

    @pytest.mark.success
    @pytest.mark.parametrize("test_info", test_data)
    def test_register_success(self, test_info,handler):
        easy_session = handler.login_easy()
        print(test_info)
        res = easy_session.request(url=url, method="post", json=test_info)
        print(res.json())
        logger=handler.logger
        try:
            assert res.status_code == 2001
        except Exception as e:
            logger.error("出错了")
            raise e
        # logger.info("注册成功")



if __name__ == "__main__":
    pytest.main()
