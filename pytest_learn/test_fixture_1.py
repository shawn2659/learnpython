# -*- coding: utf-8 -*-
"""
@author: shawn.zhao
@Mail: yh.zhao@yamu.com
@file: test_fixture_1.py
@time: 2023/9/10 12:26
"""

import pytest

@pytest.fixture()
def login():
    print("请输入用户名密码进行登录")
    return "这是返回值"

# def test_action1(login):
#     print("需要登录才能进行的操作")
#
# def test_action2():
#     print("不需要登录就可以进行的操作")

@pytest.fixture()
def login2():
    print("点击登录按钮")

# @pytest.mark.usefixtures("login2")
# @pytest.mark.usefixtures("login")
def test_action3(login, login2):      #fixture有返回值时，必须使用传参的方式调用fixture。
# def test_action3():
    reply_content = login
    print(reply_content)
    print("显示首页")

if __name__ == '__main__':
    pytest.main(['-v'])