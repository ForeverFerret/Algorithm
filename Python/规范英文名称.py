# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
Author: YuShengjia
Email: chinanetysj@gmail.com
"""

def normalize(name: str) -> str:
    """规范英文名称"""
    return reduce(
        lambda x, y: x + y.lower(),
        map(str.upper, name),
    )

def main():
    L1 = ['adam', 'LISA', 'barT']
    L2 = list(map(normalize, L1))
    print(L2)


if __name__ == "__main__":
    main()
