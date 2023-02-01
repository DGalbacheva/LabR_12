#!/usr/bin/env python3
# -+- coding: utf-8 -+-

def rec():
    n = int(input())
    if n == 0:
        return
    rec()
    print(n)


if __name__ == '__main__':
    print("Введите последовательност чисел:")
    rec()


