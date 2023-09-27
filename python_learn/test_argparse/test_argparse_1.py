# -*- coding: utf-8 -*-
"""
@author: shawn.zhao
@Mail: yh.zhao@yamu.com
@file: test_argparse_1.py
@time: 2023/9/27 8:52
"""

import argparse


def main():
    parser = argparse.ArgumentParser(description="Demo of argparse")
    parser.add_argument('-n', '--name', default='Li', help="Enter the name")
    args = parser.parse_args()
    print(args)
    name = args.name
    # print('Hello {}'.format(name))
    return name


if __name__ == '__main__':
    main()