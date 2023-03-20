class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23


# 如果你实例化此类，并尝试访问在__init__构造函数中定义的foo和_bar属性，会发生什么情况？
t = Test()
print("foo :", t.foo)

# 你会看到_bar中的单个下划线并没有阻止我们“进入”类并访问该变量的值。
# 这是因为Python中的单个下划线前缀仅仅是一个约定 - 至少相对于变量和方法名而言。
print("_bar :", t._bar)

# foo : 11
# _bar : 23
