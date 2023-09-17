# -*- coding: utf-8 -*-
"""
@author: shawn.zhao
@Mail: yh.zhao@yamu.com
@file: test_fixture_5.py
@time: 2023/9/10 20:32
"""

import pytest


@pytest.fixture(autouse=True)
def fixture_one():
    print("\n执行fixture_one")
    yield 1


def test_e(fixture_one):
    print("执行test_e")
    print(fixture_one)
    assert fixture_one == 1


if __name__ == '__main__':
    pytest.main(["-s"])