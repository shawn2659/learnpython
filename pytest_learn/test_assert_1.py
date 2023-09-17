# -*- coding: utf-8 -*-

import pytest

# 断言异常
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

# if __name__ == '__main__':
#     test_zero_division()