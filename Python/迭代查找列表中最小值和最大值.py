# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
Author: YuShengjia
Email: chinanetysj@gmail.com
"""

def findMinAndMax(L):
    """使用迭代查找一个list中最小和最大值"""
    minNum = maxNum = None
    for i in L:
        if (minNum is None) and (maxNum is None):
            minNum = maxNum = i
            continue
        if minNum > i:
            minNum = i
        if maxNum < i:
            maxNum = i
    return minNum, maxNum


def main():
    print(findMinAndMax([7, 1, 3, 9, 5]))


if __name__ == "__main__":
    main()
