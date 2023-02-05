########
# 过滤掉长度小于或等于3的字符串列表，并将剩下的转换成大写字母
########

names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']

# 表达式 name.upper() 对每个 name 进行操作并返回新的值
new_names = [name.upper() for name in names if len(name) > 3]

print("list", new_names)

########
# 计算 30 以内可以被 3 整除的整数：
########

multiples = [i for i in range(30) if i % 3 == 0]

print("list", multiples)

########
# 使用字符串及其长度创建字典：
########

listdemo = ['Google', 'Runoob', 'Taobao']

# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
newdict = {key: len(key) for key in listdemo}

print("dict", newdict)

########
# 提供三个数字，以三个数字为键，三个数字的平方为值来创建字典：
########

dt1 = {x: x ** 2 for x in (2, 4, 6)}
print("dict", dt1)

########
# 计算数字 1,2,3 的平方数：
########

setnew = {i ** 2 for i in (1, 2, 3)}

print("set", setnew)

########
# 判断不是 abc 的字母并输出：
########

set2 = {x for x in 'abracadabra' if x not in 'abc'}

print("set", set2)

########
# 生成一个包含数字 1~9 的元组
########

a = (x for x in range(1,10))

print(a, "类型", type(a))  # 返回的是生成器对象, <class 'generator'>, generator object

tp1 = tuple(a)  # 使用 tuple() 函数，可以直接将生成器对象转换成元组

print(tp1, type(tp1))  # <class 'tuple'>

########
# 可以使用 if else 来实现表达式过滤
########

list1 = ['python', 'test1', 'test2']

list2 = [word.title() if word.startswith('p') else word.upper() for word in list1]

print("if else ==>", list2)
