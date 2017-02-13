# -*- coding: UTF-8 -*-
# 字典练习

#键必须唯一

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
print ("dict['aa']: ", dict['aa']) #访问字典中不存在的数据 会返回错误


dict['Age']=8  # 更新 Age
dict['School']='菜鸟教程'  # 添加信息

#删除字典元素
del dict['Name']
dict.clear()     # 删除字典
del dict         # 删除字典

#字典键的特性
# 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
# 键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print(len(dict))   #3
print(str(dict))  #"{'Name': 'Runoob', 'Class': 'First', 'Age': 7}"
print(type(dict))

dict.clear()
dict.copy()
dict.fromkeys()
dict.get('Age')
print('Age' in dict)
dict.items()
dict.keys()
dict.setdefault('Age')

dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
dict.update(dict1)

dict.values()






