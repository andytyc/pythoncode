#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/14
# @Author  : andytyc
# @Github  : https://github.com/andytyc
# @Project: pythoncode
# @FileName: 04-1-param.py

_no_value = object()


def print_info(a, b=_no_value):
    if b is _no_value:
        print("b 没有赋值")
    else:
        print("b 赋值了")
    return


print_info(1)
print_info(2, 666)


def change(a):
    print("a", id(a))  # 指向的是同一个对象
    a = 10
    print("a [new]", id(a))  # 一个新对象


num = 1
print("num [前", id(num))
change(num)
print("num [后]", id(num))


def changeme(mylist):
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return


onelist = [10, 20, 30]
print("函数外取值 [前]: ", onelist)
changeme(onelist)
print("函数外取值 [后]:", onelist)


def printinfo(arg1, *vartuple):
    print("输出: ")
    print(arg1)
    print(vartuple)
    for var in vartuple:
        print(var)
    return


# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)


def printinfo2(arg1, **vardict):
    print("输出: ")
    print(arg1)
    print(vardict)


# 调用printinfo2 函数
printinfo2(1, a=2, b=3)
printinfo2(1)


def f(a, b, *, c):
    return a + b + c


# 报错: TypeError: f() takes 2 positional arguments but 3 were given
# f(1, 2, 3)
# 成功
res = f(1, 2, c=3)
print(res)
