# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
Author: YuShengjia
Email: chinanetysj@gmail.com
"""

def triangles(n: int):
    """杨辉三角生成"""
    L = [1]
    while n > 0:
        n -= 1
        yield L
        L = [sum(i) for i in zip([0] + L, L + [0])]


def main():
    for i in triangles(6): print(i)


if __name__ == '__main__':
    main()
