# -*- coding: utf-8 -*-
"""
@author: shawn.zhao
@Mail: yh.zhao@yamu.com
@file: test_setup_teardown_1.py
@time: 2023/9/10 8:21
"""

import pytest
import os

def setup_module():
    print("=====整个.py模块开始前只执行一次:打开浏览器=====")


def teardown_module():
    print("=====整个.py模块结束后只执行一次:关闭浏览器=====")


def setup_function():
    print("===每个函数级别用例开始前都执行setup_function===")


def teardown_function():
    print("===每个函数级别用例结束后都执行teardown_function====")


def test_one():
    print("one")


def test_two():
    print("two")


class TestCase():
    def setup_class(self):
        print("====整个测试类开始前只执行一次setup_class====")

    def teardown_class(self):
        print("====整个测试类结束后只执行一次teardown_class====")

    def setup_method(self):
        print("==类里面每个用例执行前都会执行setup_method==")

    def teardown_method(self):
        print("==类里面每个用例结束后都会执行teardown_method==")

    def test_three(self):
        print("three")

    def test_four(self):
        print("four")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "-ra", "test_setup_teardown_1.py"], [["--alluredir","./test_result"]])
    os.system("allure generate ./test_result -o ./test_report --clean")