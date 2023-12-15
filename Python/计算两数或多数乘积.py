# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
Author: YuShengjia
Email: chinanetysj@gmail.com
"""

def mul(x, y, *args):
    """计算两数或多数乘积"""
    z = 1
    for i in args:
        z *= i
    return x * y * z


def main():
    print(mul(1, 2, 3, 4, 5))
    print(mul(1, 2))


if __name__ == "__main__":
    main()
