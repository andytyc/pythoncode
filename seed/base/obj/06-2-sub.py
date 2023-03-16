#!/usr/bin/python3


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
        print("%s 说: 我 %d 岁 重 %d" % (self.name, self.age, self.__weight))


# 单继承示例
class Student(People):
    grade = ""

    # 重写构造方法
    def __init__(self, n, a, w, g):
        # 调用父类的构函 (这样就实现了：在People初始化基础上，再定制化Student的一些初始化)
        People.__init__(self, n, a, w)
        self.grade = g

    # 重写/覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


s = People("peo", 10, 60)
# 方式1: 调用实例方法
s.speak()
# 方式2: 调用实例方法
People.speak(s)

s = Student("stu", 10, 60, 3)
s.speak()


# 单继承示例
class Student66(People):
    grade = ""

    # 重写构造方法
    def __init__(self, n, a, w, g):
        # 调用父类的构函 (这样就实现了：在People初始化基础上，再定制化Student的一些初始化)
        People.__init__(self, n, a, w)
        self.grade = g

    # 重写/覆写父类的方法
    def speak(self):
        # 调用父类的speak
        People.speak(self)
        print("\n%s 我还有话说:\n" % self.name)
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


s = Student66("stu66", 10, 60, 3)
s.speak()


# 另一个类，多重继承之前的准备
class Speaker:
    topic = ""
    name = ""

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


# 多重继承
class Sample(Speaker, Student):
    a = ""

    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)


many = Sample("man", 25, 80, 4, "Python")
many.speak()  # 方法名同，默认调用的是在括号中参数位置排前父类的方法


# 类定义
class People77:
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
        print("%s 说: 我 %d 岁 重 %d" % (self.name, self.age, self.__weight))


# 单继承(单个父类)
class Student77(People77):
    grade = ""

    # 重写构造方法
    def __init__(self, n, a, w, g):
        # 调用父类的构函 (这样就实现了：在People初始化基础上，再定制化Student的一些初始化)
        # People.__init__(self, n, a, w)  # 还有种方式，使用 super 方法
        super(Student77, self).__init__(n, a, w)  # 使用super方法
        self.grade = g

    # 重写/覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


s = People77("peo77", 10, 60)
s.speak()

s = Student77("stu77", 10, 60, 3)
s.speak()
super(Student77, s).speak()  # s作为子类(Student77)的对象，调用父类(People77)的方法


class Test:
    math = 100

    # 类构造方法也是实例方法(有self)
    def __init__(self):
        self.Chinese = 90
        self.English = 80

    # 不能获取类属性，也不能获取构造函数定义的变量，属于function类型
    @staticmethod
    def say():
        print("我的语文成绩是：90")


# 方式1: 类直接调用
Test.say()
print(Test.say)  # <function Test.say at 0x000001C2620257B8>

# 方式2: 实例化后调用
A = Test()
A.say()
print(A.say)  # <function Test.say at 0x000001C2620257B8>


class Test22:
    math = 100

    # 类构造方法也是实例方法(有self)
    def __init__(self):
        self.Chinese = 90
        self.English = 80

    # 可以获取类属性，不能获取构造函数(self 实例方法)定义的变量，属于method类型
    @classmethod
    def say(cls):
        print("我的数学成绩是：{}".format(cls.math))


# 方式1: 类直接调用
Test22.say()
print(Test22.say)  # <bound method Test22.say of <class '__main__.Test22'>>

# 方式2: 实例化后调用(不推荐这样使用)
Test22().say()
print(Test22().say)  # <bound method Test22.say of <class '__main__.Test22'>>

# 我的数学成绩是：100
# <bound method Test22.say of <class '__main__.Test22'>>
# 我的数学成绩是：100
# <bound method Test22.say of <class '__main__.Test22'>>


class User1(object):
    pass


class User2(User1):
    pass


class User3(User2):
    pass


user1 = User1()
user2 = User2()
user3 = User3()

# isinstance()就可以告诉我们，一个实例化对象是否是某种类型
print(isinstance(user3, User2))  # True
print(isinstance(user3, User1))  # True
print(isinstance(user3, User3))  # True
print(isinstance(user2, User3))  # False
print(isinstance(user2, User1))  # True

print("****")

# 判断 A 是否是 B,C 的子类
print(issubclass(User3, User1))  # True
print(issubclass(User3, User2))  # True
print(issubclass(User3, (User1, User2)))  # True
print(issubclass(User1, User3))  # False
print(issubclass(User1, User2))  # False

print("****")

# 基本类型也可以用isinstance()判断
print(isinstance("两点水", str))  # True
print(isinstance(347073565, int))  # True
print(isinstance(347073565, str))  # False
