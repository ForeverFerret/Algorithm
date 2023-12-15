#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: YuShengjia
Email: chinanetysj@gmail.com
"""

def move(n, a, b, c):
    """汉诺塔(三圆盘)移动"""

    # 当仅有一个盘子的时候
    # 直接将A柱(Source)的n(此时n=1)号盘 --> C柱(Target)
    if n == 1:
        print(a, "-->", c)
    
    # 多个盘子的时候
    # 1. 先将A柱(Source)的(n - 1)号盘 --> B柱(Auxiliary)
    # 2. 再将A柱(Source)的(n)号盘 --> C柱(Target)
    # 3. 最后将B柱(Auxiliary)的(n - 1)号盘 --> C柱(Target)
    # Q: 为什么是n-1呢?
    # A: 因为假如有两个圆盘, 上面的是1号, 下面的是2号, 移动的话要先动1号, 也就是(n-1)号
    else:
        move(n - 1, a, c, b)
        print(a, "-->", c)
        move(n - 1, b, a, c)

def main():
    move(3, 'A', 'B', 'C')


if __name__ == "__main__":
    main()
