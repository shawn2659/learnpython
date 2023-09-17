# -*- coding: utf-8 -*-
"""
@author: shawn.zhao
@Mail: yh.zhao@yamu.com
@file: test_fixture_3.py
@time: 2023/9/10 17:05
"""

import pytest


@pytest.fixture
def openbrowser():
    # 会话前置操作setup
    print("\n===打开浏览器===")
    test = "测试变量是否返回"
    yield test
    # 会话后置操作teardown
    print("===关闭浏览器===")


@pytest.fixture
def login(openbrowser):
    # 方法级别前置操作setup
    print(f"输入账号，密码先登录{openbrowser}")
    name = "==我是账号=="
    pwd = "==我是密码=="
    age = "==我是年龄=="
    # 返回变量
    yield name, pwd, age
    # 方法级别后置操作teardown
    print("登录成功")


def test_s1(login):
    print("==开始测试用例1==")
    # 返回的是一个元组
    print(login)
    # 分别赋值给不同变量
    name, pwd, age = login
    print(name, pwd, age)
    assert "账号" in name
    assert "密码" in pwd
    assert "年龄" in age


def test_s2(login):
    print("==开始测试用例2==")
    print(login)


if __name__ == "__main__":
    pytest.main(["-s"])
