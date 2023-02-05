s = "Runoob"

# 截取（默认步长为1）
print(s[0:-1])  # 输出第一个到倒数第二个的所有字符
print(s[0])  # 输出字符串第一个字符
print(s[2:5])  # 输出从第三个开始到第五个的字符
print(s[2:])  # 输出从第三个开始的后的所有字符

# 截取，设置步长
print(s[2::1])
print(s[2::2])
print(s[2::3])

# 拼接
print(s + "TEST")  # 连接字符串
# 重复
print(s * 2)  # 输出字符串两次，也可以写成 print (2 * str)

# 转义
# 使用反斜杠 \ 转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串
print('Ru\noob')
print(r'Ru\noob')

# 字符
# 打印s字符串中的第一个和第6个字符
print(s[0], s[5])

'''
Runoo
R
noo
noob
RunoobTEST
RunoobRunoob
Ru
oob
Ru\noob
R b
'''