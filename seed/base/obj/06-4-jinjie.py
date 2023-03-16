class Animal:
    actually = "animal"  # 类属性

    def __init__(self, name, age):  # 定义实例时，放在括号里的才要指定
        self.name = name  # 普通属性（实例属性），要在__init__方法中定义
        self.age = age

    def sleep(self):  # 普通方法（实例方法）
        print(self.name, "[sleep] is sleeping")

    def eat(self, food):  # 普通方法（实例方法），另带参数
        print(self.name, "[eat] is eating", food)

    @classmethod
    def sentence(cls, adv):  # 类方法, 使用装饰器 classmethod
        print("[sentence] I am", adv, "an", cls.actually)

    @staticmethod
    def other(person, do):  # 静态方法（类似java的static全局方法）, 使用装饰器 staticmethod
        print(person, "is", do + "ing")

    @staticmethod
    def print_animal():
        print("这是之后定义子类（后续例子中会用到）的父类，主要讲解最基本的属性、方法以及属性的修改")
        print("类属性actually：属于整个类，每个实例都有的属性，内容相同，创建实例时不需要指定，类和实例都可以调用")
        print("普通属性name age：属于各个实例，用于存储实例数据")

        print("普通方法sleep eat：由对象调用，至少一个参数self; 只可以实例调用")
        print("类方法sentence：至少一个参数cls，可以引用类属性; 可由类调用; 也可以实例调用")
        print("静态方法other：类中的普通函数，可由类调用; 也可以实例调用(不推荐)")

        print("修改类属性：(1) 用类调用(类型.属性)修改，所有实例都更改；(2) 用实例调用(实例.属性)修改, 不影响类和其他实例")
        print("修改普通属性：直接赋值即可")


# 创建实例调用Animal类
adams = Animal(name="Adams", age=2)  # 创建实例

adams.actually  # (1) 实例调用类属性
# 'animal'
Animal.actually  # (2) 类调用类属性
# 'animal'

adams.name  # 实例调用普通属性
# 'Adams'

adams.sleep()  # 实例调用普通方法
# Adams is sleeping
adams.eat("meat")  # 实例调用有参数的普通方法
# Adams is eating meat

adams.sentence("really")  # 实例调用类方法
# I am really an animal
Animal.sentence("actually")  # 类调用类方法
# I am actually an animal

adams.other("Tim", "play")  # 实例调用静态方法
# Tim is playing
Animal.other("Mary", "watch")  # 类调用静态方法
# Mary is watching

Animal.actually = "Animal"  # 类修改类属性
adams.actually
# 'Animal'
adams.actually = "animal"  # 实例修改类属性
Animal.actually
# 'Animal'

adams.age = 3  # 实例修改普通属性

Animal.print_animal()  # 类调用静态方法
