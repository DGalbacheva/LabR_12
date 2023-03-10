#!/usr/bin/env python3
# -+- coding: utf-8 -+-

import timeit
from functools import lru_cache

def factorial_iter(n):
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product

def factorial_recurse(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * factorial_recurse(n - 1)

@lru_cache
def factorial_rec_lru(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial_recurse(n - 1)

if __name__ == '__main__':
    print("Время затраченное на итеративную версию")
    print(f'{timeit.timeit(lambda: factorial_iter(500), number=10000)},\n')
    print("Время затраченное на рекурсивную версию")
    print(f'{timeit.timeit(lambda: factorial_recurse(500), number=10000)},\n')
    print("Время затраченное на рекурсивную версию с lru_cache")
    print(timeit.timeit(lambda: factorial_rec_lru(500), number=10000))

