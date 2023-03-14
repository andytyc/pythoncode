#!/usr/bin/python3

import sys


def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")  # 生成器返回的迭代器对象 f ，这个 f 只能用于 next(f) 方法
    except StopIteration:
        print("\niter.next() is end")
        sys.exit()
