# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
Author: YuShengjia
Email: chinanetysj@gmail.com
"""

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s: str) -> float:
    # map: 将字符串变为数字列表; 记录小数点位数floatNum
    # reduce: 将数字列表变为数字; 乘以10的负(-)floatNum次方
    splitChar = '.'

    def charHandler(char: str):
        if char == splitChar:
            return splitChar
        return int(char)

    l = list(map(charHandler, s))
    decimalPlaces = len(l[l.index(splitChar): -1])
    l.remove(splitChar)

    return reduce(lambda x, y: x * 10 + y, l) * 10 ** -decimalPlaces


def main():
    print('str2float(\'123.456\') =', str2float('123.456'))
    if abs(str2float('123.456') - 123.456) < 0.00001:
        print('测试成功!')
    else:
        print('测试失败!')
   

if __name__ == "__main__":
    main()
