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
        print("[sentence] I am", adv, "actually", cls.actually)

    @staticmethod
    def other(person, do):  # 静态方法（类似java的static全局方法）, 使用装饰器 staticmethod
        print(person, "[other] is", do + "ing")

    @staticmethod
    def print_animal():
        print(">>>> print_animal <<<<")
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

print("**** 调用类属性 (类.方法名 ，实例化调用) ****")

print(adams.actually)  # (1) 实例调用类属性
print(Animal.actually)  # (2) 类调用类属性

print("**** 调用普通属性 (通过实例化后调用) ****")

print(adams.name)  # 实例调用普通属性
# print(Animal.name)  # 普通属性不能进行类调用: AttributeError: type object 'Animal' has no attribute 'name'

print("**** 调用普通方法 (通过实例化后调用) ****")

adams.sleep()  # 实例调用普通方法
adams.eat("meat")  # 实例调用有参数的普通方法

print("**** 调用类方法 (类.方法名 ，实例化调用（不推荐）) ****")

adams.sentence("really")  # 实例调用类方法
Animal.sentence("actually")  # 类调用类方法

print("**** 调用静态方法 (类.方法名 ，实例化调用) ****")

adams.other("Tim", "play")  # 实例调用静态方法
Animal.other("Mary", "watch")  # 类调用静态方法

print("**** 修改类属性 (类.方法名 ，实例化调用) ****")

# 创建实例调用Animal类
adams22 = Animal(name="Adams22", age=222)  # 创建实例 22

print(adams.actually)
print(adams22.actually)
print(Animal.actually)

Animal.actually = "Animal--happy"  # 类修改类属性 (影响类、其他实例)
print(adams.actually)
print(adams22.actually)
print(Animal.actually)

adams.actually = "animal-life"  # 实例修改类属性 (不影响类、其他实例)
print(adams.actually)
print(adams22.actually)
print(Animal.actually)

print("**** 修改普通属性 (实例化调用) ****")

adams.age = 3  # 实例修改普通属性
print(adams.actually, adams.age)
adams22.age = 333  # 实例修改普通属性
print(adams22.actually, adams22.age)

print("**** 知识点 (总结) ****")
Animal.print_animal()


# **** 调用类属性 (类.方法名 ，实例化调用) ****
# animal
# animal
# **** 调用普通属性 (通过实例化后调用) ****
# Adams
# **** 调用普通方法 (通过实例化后调用) ****
# Adams [sleep] is sleeping
# Adams [eat] is eating meat
# **** 调用类方法 (类.方法名 ，实例化调用（不推荐）) ****
# [sentence] I am really actually animal
# [sentence] I am actually actually animal
# **** 调用静态方法 (类.方法名 ，实例化调用) ****
# Tim [other] is playing
# Mary [other] is watching
# **** 修改类属性 (类.方法名 ，实例化调用) ****
# animal
# animal
# animal
# Animal--happy
# Animal--happy
# Animal--happy
# animal-life
# Animal--happy
# Animal--happy
# **** 修改普通属性 (实例化调用) ****
# animal-life 3
# Animal--happy 333
# **** 知识点 (总结) ****
# >>>> print_animal <<<<
# 这是之后定义子类（后续例子中会用到）的父类，主要讲解最基本的属性、方法以及属性的修改
# 类属性actually：属于整个类，每个实例都有的属性，内容相同，创建实例时不需要指定，类和实例都可以调用
# 普通属性name age：属于各个实例，用于存储实例数据
# 普通方法sleep eat：由对象调用，至少一个参数self; 只可以实例调用
# 类方法sentence：至少一个参数cls，可以引用类属性; 可由类调用; 也可以实例调用
# 静态方法other：类中的普通函数，可由类调用; 也可以实例调用(不推荐)
# 修改类属性：(1) 用类调用(类型.属性)修改，所有实例都更改；(2) 用实例调用(实例.属性)修改, 不影响类和其他实例
# 修改普通属性：直接赋值即可


class Dog(Animal):  # 类的继承
    # #############################################
    # 只使用@property装饰器与普通函数做对比
    # #############################################

    # 不用装饰器
    def eating(self):
        print("[eating] I am eating")

    @property  # 用装饰器, 这个方法调用就可以不加括号，即将其转化为属性
    def running(self):
        if 3 <= self.age < 130:
            print("[running] I am running")
        elif 0 < self.age < 3:
            print("[running] I can't run")
        else:
            print("[running] please input true age")

    # #############################################
    # 三种装饰器，可以 {获取、设置、删除} 这样定义的属性
    # #############################################

    @property  # 用 property 的装饰器, 转换 函数名 为属性, 用于：获取值
    def country(self):
        return self._country  # 注意这个属性之前从来没有定义过，是在下面的setter中定义的

    @country.setter  # 用 函数名.setter 的装饰器, 用于：设置值
    def country(self, value):  # 设置这个属性的值
        self._country = value

    @country.deleter  # 用 函数名.deleter 的装饰器, 用于：删除属性
    def country(self):
        del self._country
        print("The attr [1] country is delete ok")

    # #############################################
    # 用property函数实现和装饰器相同的功能
    # #############################################

    def get_city(self):
        return self._city

    def set_city(self, value):
        self._city = value

    def del_city(self):
        print("The attr [2] country is delete ok")
        del self._city

    city = property(get_city, set_city, del_city, "where it is in")

    # #############################################
    # 总结
    # #############################################

    @staticmethod
    def print_dog():
        print("这是Animal的一个子类，主要讲解三个装饰器进行方法向属性的转换")
        print("类继承，创建实例时仍要指定父类的普通属性")
        print("@property装饰器将方法转化为属性方式调用，此时的方法必须只有一个self参数")
        print("使用@property后可以看做一个属性(country)，用property函数可以达到相同的效果(city)")
        print("注：city中property第四个参数只是一个说明，用Dog.city.__doc__来调用，即返回 where it is in")


david = Dog("David", 2)  # 创建实例

print("**** 用和不用@property (对比) ****")

david.eating()  # 调用普通方法
david.running  # 用过@property装饰器后不需要加括号

dean = Dog("Dean", 4)
dean.running  # 在@property的属性中封装了逻辑判断，会根据各种运行条件下输出不同的结果

print("**** property 方法转属性 (实现方式1: 三个装饰器实现) ****")

# print(david.country)  # 这个属性如果还没有set设置值，直接访问会报错 AttributeError: 'Dog' object has no attribute '_country'
david.country = "America"  # 设置值
print(david.country)  # 访问正常
david.country = "America66"  # 设置值
print(david.country)  # 访问正常
del david.country  # 如果这里的不出现_country则这样就可以删除，但是用self.country则真的变成了属性，所以为了区别多定义了一个_country
# print(david.country)  # 若删除了, 则无法再调用 david.country 会报错 AttributeError: 'Dog' object has no attribute '_country'

print("**** property 方法转属性 (实现方式2: 不用装饰器，用三个函数组装) ****")

# print(david.city)  # 这个属性如果还没有set设置值，直接访问一样会报错 AttributeError: 'Dog' object has no attribute '_city'
david.city = "Beijing"
print(david.city)
david.city = "Beijing222"
print(david.city)
del david.city
# print(david.city)  # 已删除后再访问一样会报错: AttributeError: 'Dog' object has no attribute '_city'

print("**** 知识点 (总结) ****")
Dog.print_dog()


# **** 用和不用@property (对比) ****
# [eating] I am eating
# [running] I can't run
# [running] I am running
# **** property 方法转属性 (实现方式1: 三个装饰器实现) ****
# America
# America66
# The attr [1] country is delete ok
# **** property 方法转属性 (实现方式2: 不用装饰器，用三个函数组装) ****
# Beijing
# Beijing222
# The attr [2] country is delete ok
# **** 知识点 (总结) ****
# 这是Animal的一个子类，主要讲解三个装饰器进行方法向属性的转换
# 类继承，创建实例时仍要指定父类的普通属性
# @property装饰器将方法转化为属性方式调用，此时的方法必须只有一个self参数
# 使用@property后可以看做一个属性(country)，用property函数可以达到相同的效果(city)
# 注：city中property第四个参数只是一个说明，用Dog.city.__doc__来调用，即返回 where it is in


class Cat(Animal):
    def __init__(self, weight):  # 覆盖了父类的__init__，所以定义实例时不需要指定name和age
        self.__weight = weight
        self._weight = weight + 1
        self.weight = self._weight + 1

    def get_myweight(self):
        print("[cat] My _weight is", self._weight, "kg")

    def get_trueweight(self):
        print("[cat] Actually the cat's weight is", self.__weight)

    @staticmethod
    def print_cat():
        print(">>>> print_cat <<<<")
        print("这个类是Animal类的子类，也是Blackcat类的父类")
        print("Cat类和Blackcat类结合，主要用于讲解私人属性、方法的继承与覆盖")

        print("weight是普通属性，可以在外部访问，即用类调用属性获得，可以被子类内部调用")
        print("_weight这样前面加一个下划线表示希望你不要在外部访问它，但是还是可以访问的，可以被子类内部调用")
        print("__weight这样加两个下划线的是不允许外部访问的，只可以在类中被调用，不可以被子类内部调用")

        print("__init__在子类中定义则覆盖了父类中的__init__，不需要指定父类中的属性，也无法调用父类的属性")
        print("在子类中实现和父类同名的方法，也会把父类的方法覆盖掉")


class BlackCat(Cat):
    def get_weight(self):  # 可以
        print("[black cat] My weight is", self.weight)

    def get_weight_again(self):  # 可以使用
        print("[black cat]  My _weight is", self._weight)

    def get_true_weight(self):
        # 不可以使用, 这个方法因为无法调用self.__weight所以这个方法无法使用, 会报错:
        # AttributeError: 'BlackCat' object has no attribute '_BlackCat__weight'
        print("[black cat] Actually My weight is exactly", self.__weight)

        # 真不能访问吗？
        # 也可以这样特殊访问:
        # print("[black cat] Actually My weight is exactly", self._Cat__weight)

    def get_trueweight(self):  # 重写: 覆盖了Cat父类中定义的方法
        print("[black cat] Actually My (_weight +1) is exactly", self._weight + 1)


print("**** 测试私人属性的外部访问 ****")

cole = Cat(5)
print(cole.weight)
print(cole._weight)
cole.get_trueweight()  # 在类中引用私有属性__weight，用这个方法返回
print(cole._Cat__weight)  # 特殊提示: 非要访问也可以，其实是python解释器把__weight改成了_Cat__weight

print("**** 测试私人属性的子类调用 ****")

cain = BlackCat(5)
cain.get_weight()
cain.get_weight_again()
# cain.get_true_weight()  # 直接访问 __weight 会报错, 但逻辑修改为 _Cat__weight 就可以正常访问了

print("**** 测试方法的继承与覆盖 ****")

cain.get_myweight()  # 调用父类方法
cain.get_trueweight()  # 子类中同名函数覆盖父类方法

print("**** 知识点 (总结) ****")
cain.print_cat()


# **** 测试私人属性的外部访问 ****
# 7
# 6
# [cat] Actually the cat's weight is 5
# 5
# **** 测试私人属性的子类调用 ****
# [black cat] My weight is 7
# [black cat]  My _weight is 6
# **** 测试方法的继承与覆盖 ****
# [cat] My _weight is 6 kg
# [black cat] Actually My (_weight +1) is exactly 7
# **** 知识点 (总结) ****
# >>>> print_cat <<<<
# 这个类是Animal类的子类，也是Blackcat类的父类
# Cat类和Blackcat类结合，主要用于讲解私人属性、方法的继承与覆盖
# weight是普通属性，可以在外部访问，即用类调用属性获得，可以被子类内部调用
# _weight这样前面加一个下划线表示希望你不要在外部访问它，但是还是可以访问的，可以被子类内部调用
# __weight这样加两个下划线的是不允许外部访问的，只可以在类中被调用，不可以被子类内部调用
# __init__在子类中定义则覆盖了父类中的__init__，不需要指定父类中的属性，也无法调用父类的属性
# 在子类中实现和父类同名的方法，也会把父类的方法覆盖掉


class Tiger:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        return "[Tiger] I am eating"

    def myname(self):
        return "[Tiger] my name is " + self.name


class WhiteTiger(Tiger):
    def __init__(self, name, age, height):
        # 1 处让子类中可以调用父类的属性，其实就相当于运行父类的_init_函数。

        # 标准引用 (standard call)
        # 如果没有#1，则实例无法调用name属性；也无法调用realname方法，因为它用到了name属性，所以：需要初始化父类，这样就有了这些属性。
        # super(WhiteTiger, self).__init__(name, age)  # 1 (1-1) 调用父类初始化操作

        #######
        # #1处 除了上边方式，还有几种等价定义形式如下
        #######

        # 直接引用（hardwired call）
        # 这种方式有个缺点: 不使用super而是直接用"父类名称"，这样做的弊端是，如果"父类名称"改了，则所有这么用的位置都得改
        # Tiger.__init__(self, name, age)  # (1-2) 也可以调用父类初始化操作

        # 间接引用（indirected call）
        # 直接用super()简化写法，这是python3中才有的用法
        # Python3.x 和 Python2.x 的一个区别是: Python 3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx
        super().__init__(name, age)  # (1-3) 也可以调用父类初始化操作, self不用传入（自动传入）
        # super().__init__(self, name, age)  # 报错: TypeError: __init__() takes 3 positional arguments but 4 were given

        self.height = height

    def eatmore(self):
        # 此处用super调用父类的eat方法，但实际上用self.eat调用就可以了，但如果要在Whitetiger中再定义一个eat方法，其中
        # 要调用父类的eat方法，则必须用super，如下所示
        return "[WhiteTiger] more " + self.eat()  # 2 这里子类未重写eat(), 所以继承了父类eat(), 直接调用就可以调用父类eat
        # 也可以使用 super
        # return "[WhiteTiger] more " + super(WhiteTiger, self).eat()  #2 调用父类eat

    def realname(self):
        return "[WhiteTiger] Actually " + super(WhiteTiger, self).myname()  # 调用父类myname


wtony = WhiteTiger("Tony", 10, 100)

print(wtony.eat())
print(wtony.myname())

print(wtony.eatmore())
print(wtony.realname())


# [Tiger] I am eating
# [Tiger] my name is Tony
# [WhiteTiger] more [Tiger] I am eating
# [WhiteTiger] Actually [Tiger] my name is Tony


# 四边形
class Rectangle:
    def __init__(self, length, width, **kwargs):
        print("[Rectangle] __init__", length, width, kwargs)
        self.length = length
        self.width = width
        super().__init__(**kwargs)  # 还可以往上调用，是因为object 是所有对象的基类; 只是再python3.x中可以不显示声明继承object

    # 面积
    def area(self):
        print("[Rectangle] You're getting the area...")
        return self.length * self.width

    # 周长
    def perimeter(self):
        print("[Rectangle] You're getting the perimeter...")
        return 2 * (self.length + self.width)


# 正方形
class Square(Rectangle):
    def __init__(self, length, **kwargs):
        print("[Square] __init__", length, kwargs)
        super().__init__(length=length, width=length, **kwargs)  # 调用父类进行初始化


print("**** 查看类的MRO ****")

# 对于Rectangle的实例而言，调用它的任何方法，它首先会从Rectangle中找对应的方法，其次是object。
# 提示：object是python中所有类的基类，它实际上没有任何特殊方法以外的方法。
print("Rectangle : ", Rectangle.__mro__)

# 方式1 (输出一个元组)
print("Square : ", Square.__mro__)
# 方式2
print("Square : ", Square.mro())


# 立方体
class Cube(Square):
    # 表面积
    def surface_area(self):
        print("[Cube] You're getting the surface_area...")
        face_area = super().area()
        return face_area * 6

    # 体积
    def volume(self):
        print("[Cube] You're getting the volume...")
        face_area = super().area()
        return face_area * self.length


# 三角形
class Triangle:
    def __init__(self, base, height, **kwargs):
        print("[Triangle] __init__", base, height, kwargs)
        self.base = base
        self.height = height
        super().__init__(**kwargs)  # 调用父类进行初始化

    def area(self):
        print("[Triangle] You're getting the area...")
        return 0.5 * self.base * self.height


# 金字塔 RightPyramid
class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height, **kwargs):
        print("[RightPyramid] __init__", base, slant_height, kwargs)
        self.base = base
        self.slant_height = slant_height  # 斜高
        kwargs["height"] = slant_height
        kwargs["length"] = base
        # super().__init__(base, **kwargs)  # 调用父类, 错误, 这个例子可以很好的理解下函数的传参数
        super().__init__(base=base, **kwargs)  # 调用父类, 正确

    # 求出底面积，然后利用底面周长 * 斜高 / 2 来求侧面积，最终相加得到总的表面积
    def area(self):
        print("[RightPyramid] You're getting the area...")
        base_area = super().area()  # 调用父类
        perimeter = super().perimeter()  # 调用父类
        return 0.5 * perimeter * self.slant_height + base_area

    # 求表面积，这种方法是先求每个侧面的面积，再加上底面积
    def area_2(self):
        print("[RightPyramid] You're getting the area...")
        base_area = super().area()  # 调用父类
        triangle_area = super().area()  # 调用父类
        return triangle_area * 4 + base_area


print("**** super单继承调用 ****")

# 简单继承调用
print(">>>> (Square)")
print("Square MRO : ", Square.__mro__)

sq = Square(10)
print("面积 :", sq.area(), "周长 :", sq.perimeter())

# 简单继承调用
print(">>>> (Cube)")
print("Cube MRO : ", Cube.__mro__)

c = Cube(9)
print("表面积 :", c.surface_area())
print("体积 :", c.volume())

print("**** super多继承调用 ****")

# 这里要仔细看下，在继承链路中，在 Rectangle 后的不是 object 而是 Triangle 然后 object
# 因为在 object 链路节点下，Rectangle 和 Triangle 是平级的！！！
# 在 Pycharm 工具中，也有可视化查看类调用链路的页面按钮，更方便！！！
print("Rectangle MRO : ", RightPyramid.__mro__)

pyramid = RightPyramid(2, 4)
print("area :", pyramid.area())
print("area_2 :", pyramid.area_2())

"""
**** 查看类的MRO ****
Rectangle :  (<class '__main__.Rectangle'>, <class 'object'>)
Square :  (<class '__main__.Square'>, <class '__main__.Rectangle'>, <class 'object'>)
Square :  [<class '__main__.Square'>, <class '__main__.Rectangle'>, <class 'object'>]
**** super单继承调用 ****
>>>> (Square)
Square MRO :  (<class '__main__.Square'>, <class '__main__.Rectangle'>, <class 'object'>)
[Square] __init__ 10 {}
[Rectangle] __init__ 10 10 {}
[Rectangle] You're getting the area...
[Rectangle] You're getting the perimeter...
面积 : 100 周长 : 40
>>>> (Cube)
Cube MRO :  (<class '__main__.Cube'>, <class '__main__.Square'>, <class '__main__.Rectangle'>, <class 'object'>)
[Square] __init__ 9 {}
[Rectangle] __init__ 9 9 {}
[Cube] You're getting the surface_area...
[Rectangle] You're getting the area...
表面积 : 486
[Cube] You're getting the volume...
[Rectangle] You're getting the area...
体积 : 729
**** super多继承调用 ****
Rectangle MRO :  (<class '__main__.RightPyramid'>, <class '__main__.Square'>, <class '__main__.Rectangle'>, <class '__main__.Triangle'>, <class 'object'>)
[RightPyramid] __init__ 2 4 {}
[Square] __init__ 2 {'base': 2, 'height': 4}
[Rectangle] __init__ 2 2 {'base': 2, 'height': 4}
[Triangle] __init__ 2 4 {}
[RightPyramid] You're getting the area...
[Rectangle] You're getting the area...
[Rectangle] You're getting the perimeter...
area : 20.0
[RightPyramid] You're getting the area...
[Rectangle] You're getting the area...
[Rectangle] You're getting the area...
area_2 : 20
"""
