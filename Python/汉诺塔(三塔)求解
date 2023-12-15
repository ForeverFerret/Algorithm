#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: YuShengjia
Email: chinanetysj@gmail.com
"""

# 汉诺塔的移动可以用递归函数非常简单地实现
# 请编写move(n, a, b, c)函数，它接收参数n, 表示3个柱子A、B、C中第1个柱子A的盘子数量, 然后打印出把所有盘子从A借助B移动到C的方法
#    if n == 1:
#        print(a, '-->', c)
#    if n == 2:
#        print(a, '-->', b)
#        print(a, '-->', c)
#        print(b, '-->', c)
#    if n == 3:
#        print(a, '-->', c)
#        print(a, '-->', b)
#        print(c, '-->', b)
#        print(a, '-->', c)
#        print(b, '-->', a)
#        print(b, '-->', c)
#        print(a, '-->', c)

def move(n, a, b, c):
    """汉诺塔(三圆盘)移动"""

    if n == 1:
        # 仅有一个盘子的时候
        # 直接将A柱(Source)的n(此时n=1)号盘 --> C柱(Target)
        print(a, '-->', c)
    else:
        # 多个盘子的时候
        # 1. 先将A柱(Source)的(n - 1)号盘 --> B柱(Auxiliary)
        # 2. 再将A柱(Source)的(n)号盘 --> C柱(Target)
        # 3. 最后将B柱(Auxiliary)的(n - 1)号盘 --> C柱(Target)
        move(n - 1, a, c, b)
        print(a, '-->', c)
        move(n - 1, b, a, c)

def main():
    move(3, 'A', 'B', 'C')


if __name__ == "__main__":
    main()
