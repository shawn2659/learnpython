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
        print('%s: %s' % (self.name, self.score))


shawn = Student('shawn.zhao', 80)
joyce = Student('joyce.zhao', 100)

print(shawn.print_score())
print(joyce.print_score())
