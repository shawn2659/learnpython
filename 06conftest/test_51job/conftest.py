# -*- coding: utf-8 -*-
"""
@author: shawn.zhao
@Mail: yh.zhao@yamu.com
@file: conftest.py
@time: 2023/9/17 7:12
"""

import pytest

@pytest.fixture(scope="module")
def open_51(login):
    name, token = login
    print(f"###用户 {name} 打开51job网站###")