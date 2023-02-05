#!/usr/bin/python3

tp1 = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tp1)  # 输出完整元组

# 截取
print(tp1[0])  # 输出元组的第一个元素
print(tp1[1:3])  # 输出从第二个元素开始到第三个元素
print(tp1[2:])  # 输出从第三个元素开始的所有元素

# 拼接
print(tp1 + tinytuple)  # 连接元组
# 重复
print(tinytuple * 2)  # 输出两次元组

# 它可以包含可变的对象，比如：list 列表
tp2 = ('abc', 'de', 123, 456, ['hh', 'jj', 'kk', 999, 888])

print(tp2)

# 元素不可变，所以会报错: TypeError: 'tuple' object does not support item assignment
# tp2[2] = 'ff'     # 报错
# tp2[4] = ['mmm', 'nnn', 666]  # 报错

tp2[4][3] = 666
print(tp2)  # 成功，第5个元素是列表，修改列表内的元素是可以的！

# 构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：

tp3 = ()    # 空元组
print(tp3)

tp4 = (20,)  # 一个元素，需要在元素后添加逗号
print(tp4)
