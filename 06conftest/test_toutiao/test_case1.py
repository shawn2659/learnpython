# -*- coding: utf-8 -*-
"""
@author: shawn.zhao
@Mail: yh.zhao@yamu.com
@file: test_case1.py
@time: 2023/9/17 7:21
"""


def test_no_fixture(login):
    print("==没有__init__测试用例，我进入头条了==", login)