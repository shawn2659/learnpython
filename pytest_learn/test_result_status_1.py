# -*- coding: utf-8 -*-
"""
@author: shawn.zhao
@Mail: yh.zhao@yamu.com
@file: test_result_status_1.py
@time: 2023/9/12 8:32
"""
import pytest


@pytest.fixture()
def pwd():
    print("获取用户名")
    a = "yygirl"
    assert a == "yygirl"
    yield a


def test_1(pwd):
    assert pwd == "yygirl"