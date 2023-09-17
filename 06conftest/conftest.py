# -*- coding: utf-8 -*-
"""
@author: shawn.zhao
@Mail: yh.zhao@yamu.com
@file: conftest.py
@time: 2023/9/13 8:57
"""

import pytest


@pytest.fixture(scope="session")
def login():
    print("\n====登录功能，返回账号，token===")
    name = "testyy"
    token = "npoi213bn4"
    yield name, token
    print("\n====退出登录！！！====")


@pytest.fixture(autouse=True)
def get_info(login):
    name, token = login
    print(f"\n== 每个用例都调用的外层fixture：打印用户token： {token} ==")