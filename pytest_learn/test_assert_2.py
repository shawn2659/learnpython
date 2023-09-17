# -*- coding: utf-8 -*-
"""
@author: shawn.zhao
@Mail: yh.zhao@yamu.com
@file: test_assert_2.py
@time: 2023/9/10 8:12
"""

import pytest

# 详细断言异常
def test_zero_division_long():
    with pytest.raises(ZeroDivisionError) as excinfo:
        1 / 0

    # 断言异常类型 type
    assert excinfo.type == ZeroDivisionError
    # 断言异常 value 值
    assert "division by zero" in str(excinfo.value)