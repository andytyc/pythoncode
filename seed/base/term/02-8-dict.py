#!/usr/bin/python3

dt1 = {}

print(dt1)

dt1['one'] = "1 - 菜鸟教程"
dt1[2] = "2 - 菜鸟工具"

print(dt1)

print(dt1['one'])  # 输出键为 'one' 的值
print(dt1[2])  # 输出键为 2 的值

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(tinydict)  # 输出完整的字典

print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值

dt3 = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
print(dt3)

dt4 = {x: x**2 for x in (2, 4, 6)}  # 使用的是字典推导式
print(dt4)

dt5 = dict(Runoob=1, Google=2, Taobao=3)
print(dt5)

'''
{}
{'one': '1 - 菜鸟教程', 2: '2 - 菜鸟工具'}
1 - 菜鸟教程
2 - 菜鸟工具
{'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
dict_keys(['name', 'code', 'site'])
dict_values(['runoob', 1, 'www.runoob.com'])
{'Runoob': 1, 'Google': 2, 'Taobao': 3}
{2: 4, 4: 16, 6: 36}
{'Runoob': 1, 'Google': 2, 'Taobao': 3}
'''