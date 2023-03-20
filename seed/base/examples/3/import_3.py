from my_module2 import *

print("external_func :", external_func2())
print("_internal_func :", _internal_func2())  # 模块如果定义指明了 __all__ 列表，就可以访问此方法

# external_func : 12
# _internal_func : 42
