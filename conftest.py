"""固定文件名 conftest.py.
存储所有的测试夹具。fixture
"""
import pytest
import os

from middleware.handler import Handler


@pytest.fixture(scope="class")
def handler():
    h = Handler()
    yield h


@pytest.fixture(scope="class")
def easy_session(handler):
    """登录批发易"""
    easy_session = handler.login_easy()
    yield easy_session
    easy_session.close()


@pytest.fixture(scope="function")
def easy_switch_shop(easy_session):
    easy_session.switch_shop(645)
    yield easy_session


@pytest.fixture(scope="module")
def logger():
    logger = Handler.logger
    yield logger
