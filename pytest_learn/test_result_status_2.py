# -*- coding: utf-8 -*-
"""
@author: shawn.zhao
@Mail: yh.zhao@yamu.com
@file: test_result_status_2.py
@time: 2023/9/12 8:37
"""
import pytest


@pytest.fixture()
def pwd():
    print("获取密码")
    a = "polo"
    return a


def test_2(pwd):
    raise NameError
    assert pwd == "polo"