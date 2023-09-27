# -*- coding: utf-8 -*-
"""
@author: shawn.zhao
@Mail: yh.zhao@yamu.com
@file: test_class_basic_1.py
@time: 2023/9/24 7:46
"""

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('1')
        print('%s的分数是: %s' % (self.name, self.score))
        print('2')
        return 123


if __name__ == '__main__':
    shawn = Student('shawn.zhao', 80)
    joyce = Student('joyce.zhao', 100)
    # shawn.print_score()
    # joyce.print_score()
    print(shawn.print_score())
    print('3')
    print(joyce.print_score())
    # print(shawn)

