# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
Author: YuShengjia
Email: chinanetysj@gmail.com
"""

# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909
def is_palindrome(n: int) -> bool:
    n_list = [int(i) for i in str(n)]
    half_index = int(len(n_list) / 2)
    if n_list[:half_index + 1] == n_list[-1: -half_index - 2: -1]:
        return True
    return False

def main():
    output = filter(is_palindrome, range(1, 1000))
    print('1~1000:', list(output))


if __name__ == "__main__":
    main()
