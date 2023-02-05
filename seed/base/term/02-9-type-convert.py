num_int = 123  # 整数
num_flo = 1.23  # 浮点数

num_new = num_int + num_flo

print("datatype of num_int:", type(num_int))  # int
print("datatype of num_flo:", type(num_flo))  # float

print("Value of num_new:", num_new)
print("datatype of num_new:", type(num_new))  # float

# int() 强制转换为整型：

x = int(1)  # x 输出结果为 1
y = int(2.8)  # y 输出结果为 2
z = int("3")  # z 输出结果为 3

print(x, y, z)

# float() 强制转换为浮点型：

x = float(1)  # x 输出结果为 1.0
y = float(2.8)  # y 输出结果为 2.8
z = float("3")  # z 输出结果为 3.0
w = float("4.2")  # w 输出结果为 4.2

print(x, y, z)
print(w)

# float() 强制转换为浮点型：

x = str("s1")  # x 输出结果为 's1'
y = str(2)  # y 输出结果为 '2'
z = str(3.0)  # z 输出结果为 '3.0'

print(x, y, z)

# 整型和字符串类型进行运算，就可以用强制类型转换来完成：

num_int = 123
num_str = "456"

print("num_int 数据类型为:", type(num_int))  # int
print("类型转换前，num_str 数据类型为:", type(num_str))  # str

num_str = int(num_str)  # 强制转换为整型
print("类型转换后，num_str 数据类型为:", type(num_str))  # int

num_sum = num_int + num_str

print("num_int 与 num_str 相加结果为:", num_sum)
print("sum 数据类型为:", type(num_sum))  # int
