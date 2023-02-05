#!/usr/bin/python3

lt = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(lt)  # 输出完整列表

# 截取
print(lt[0])  # 输出列表第一个元素
print(lt[1:3])  # 从第二个开始输出到第三个元素
print(lt[2:])  # 输出从第三个元素开始的所有元素

# 截取，设置步长
print(lt[1::2])
print(lt[1::3])

# 拼接
print(tinylist * 2)  # 输出两次列表
# 重复
print(lt + tinylist)  # 连接列表

# 列表中的元素可以改变
a = [1, 2, 3, 4, 5, 6]
a[0] = 9
print(a)

a[2:5] = [13, 14, 15]
print(a)

a[2:5] = []   # 将对应的元素值设置为 []
print(a)

'''
['abcd', 786, 2.23, 'runoob', 70.2]
abcd
[786, 2.23]
[2.23, 'runoob', 70.2]
[123, 'runoob', 123, 'runoob']
['abcd', 786, 2.23, 'runoob', 70.2, 123, 'runoob']
[9, 2, 3, 4, 5, 6]
[9, 2, 13, 14, 15, 6]
[9, 2, 6]
'''
