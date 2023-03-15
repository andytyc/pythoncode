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
s.speak()

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
