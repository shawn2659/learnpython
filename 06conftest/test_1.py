# -*- coding: utf-8 -*-
"""
@author: shawn.zhao
@Mail: yh.zhao@yamu.com
@file: test_1.py
@time: 2023/9/13 8:57
"""
import pytest


# @pytest.mark.usefixtures("login")
# def test_get_info():
#     name, token = login              #无法获取login，原因是“如果fixture有返回值，那么使用@pytest.mark.usefixtures()的方式是无法获取到返回值的。必须使用传参的方式”
#     print("***基础用例：获取用户个人信息***")
#     print(f"用户名:{name}, token:{token}")


def test_get_info(login):
    name, token = login
    print("***基础用例：获取用户个人信息***")
    print(f"用户名:{name}, token:{token}")