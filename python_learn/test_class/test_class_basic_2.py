# -*- coding: utf-8 -*-
"""
@author: shawn.zhao
@Mail: yh.zhao@yamu.com
@file: test_class_basic_2.py
@time: 2023/10/3 7:34
"""


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_info(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


if __name__ == '__main__':
    joyce = Student("shawn", 35)
    joyce.print_info()
    print('他的分数评级是：%s' % joyce.get_grade())
