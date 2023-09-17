# -*- coding: utf-8 -*-
"""
@author: shawn.zhao
@Mail: yh.zhao@yamu.com
@file: test_result_status_3.py
@time: 2023/9/12 8:45
"""

import pytest


# 断言装饰器
@pytest.mark.xfail(raises=ZeroDivisionError)
def test_f():
    1 / 0
