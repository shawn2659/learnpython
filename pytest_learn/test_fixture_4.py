# -*- coding: utf-8 -*-
"""
@author: shawn.zhao
@Mail: yh.zhao@yamu.com
@file: test_fixture_4.py
@time: 2023/9/10 20:25
"""

import pytest


@pytest.fixture()
def fixture_demo():
    # setup
    print("\n连接数据库")
    yield
    # teardown
    # print("清空脏数据")
    assert 1 == 2

def test_case(fixture_demo):
    print("\n执行test_case")
    assert True


if __name__ == '__main__':
    pytest.main(["-s"])