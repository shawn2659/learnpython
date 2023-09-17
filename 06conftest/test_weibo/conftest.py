# -*- coding: utf-8 -*-
"""
@author: shawn.zhao
@Mail: yh.zhao@yamu.com
@file: conftest.py
@time: 2023/9/17 7:22
"""

import pytest


@pytest.fixture(scope="function")
def open_weibo(login):
    name, token = login
    print(f"&&& 用户 {name} 返回微博首页 &&&")