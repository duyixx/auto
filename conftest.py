"""固定文件名 conftest.py.

存储所有的测试夹具。fixture
"""
import pytest

from middleware.handler import Handler


@pytest.fixture(scope="class")
def handler():
    h = Handler()
    yield h

@pytest.fixture(scope="function")
def easy_session():
    """登录批发易"""
    h=Handler()
    yield h.login_easy()


@pytest.fixture(scope="function")
def logger():
    h=Handler()
    yield h.logger
