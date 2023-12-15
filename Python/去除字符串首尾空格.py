#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: YuShengjia
Email: chinanetysj@gmail.com
"""

def trim(s: str) -> str:
    """去除字符串首位空格"""

    # 空格字符
    space_char = ' '

    # 首字符
    start_num = 0
    start_char = s[start_num]

    # 尾字符
    end_num = -1
    end_char = s[end_num]

    # 首字符为空格
    if start_char == space_char:
        start_num += 1

    # 尾字符为空格
    if end_char == space_char:
        end_num -= 1

    return s[start_num:end_num]


def main():
    s = " ppppp "
    print(f"[{s}]")
    print(f"[{trim(s)}]")


if __name__ == "__main__":
    main()
