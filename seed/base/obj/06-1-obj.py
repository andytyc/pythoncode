#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/15
# @Author  : andytyc
# @Github  : https://github.com/andytyc
# @Project: pythoncode
# @FileName: 06-1-obj.py


class ClassA:
    var1 = 100
    var2 = 0.01
    var3 = "两点水"

    def fun1(self):
        print("我是 fun1")

    def fun2(self):
        print("我是 fun2")

    def fun3(self):
        print("我是 fun3")


# 实例（类对象）
boy = ClassA()
# 调用属性
print(boy.var1)
print(boy.var2)
print(boy.var3)
# 调用方法
boy.fun1()
boy.fun2()
boy.fun3()


class Test:
    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()


class Test2:
    def prt(runoob):
        print(runoob)
        print(runoob.__class__)


t2 = Test2()
t2.prt()


# 类定义
class People:
    # 定义基本属性
    name = ""
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁, 重 %d" % (self.name, self.age, self.__weight))


# 实例化类
p = People("runoob", 10, 30)
# 调用实例方法
p.speak()


class Site:
    def __init__(self, name, url):
        self.name = name  # public
        self.__url = url  # private

    def who(self):
        print("name  : ", self.name)
        print("url : ", self.__url)

    def __foo(self, w):  # 私有方法
        print("这是私有方法", w)

    def foo(self):  # 公共方法
        print("这是公共方法")
        self.__foo("公共foo调用")


x = Site("菜鸟教程", "www.runoob.com")
x.who()  # 正常输出
x.foo()  # 正常输出
# x.__foo()  # 报错, AttributeError: 'Site' object has no attribute '__foo'


class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1  # 类内部可以调用私有属性
        self.publicCount += 1
        print("count:", self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)  # 正常
# print(counter.__secretCount)  # 报错(实例不能访问私有变量)


# 类定义
class People2:
    # 定义基本属性
    name = ""
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁, 重 %d" % (self.name, self.age, self.__weight))

    def __del__(self):
        # 实例释放资源时自动调用
        print("i'm game over", self.name)


# 实例化类
p2 = People2("runoob2", 10, 30)
# 调用实例方法
p2.speak()


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "Vector (%d, %d)" % (self.a, self.b)  # print()打印输出时，会执行这个__str__方法

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)  # 返回一个新的Vector实例对象


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)  # + 加运算触发__add__, print打印触发__str__
