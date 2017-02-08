# -*- coding: UTF-8 -*-
# 列表练习

list1=['google','runoob',1997,2000]
list2=[1,2,3,4,5,6,7]
print("list1[0]:",list1[0]) #google
print("list2[1:5]:",list2[1:5]) #[2, 3, 4, 5]

#更新列表
list=['google','runoob',1997,2000]
print ("第三个元素为 : ", list[2]) #1997
list[2] = 2001
print ("更新后的第三个元素为 : ", list[2]) #2001

#删除列表的元素
list = ['Google', 'Runoob', 1997, 2000]
print (list)
del list[2]
print ("删除第三个元素 : ", list) #['Google', 'Runoob', 2000]

list = ['Google', 'Runoob', 1997, 2000]
print(len(list)) #4
print(list+list) #['Google', 'Runoob', 1997, 2000,'Google', 'Runoob', 1997, 2000]

list3=["hi"]
print(list3*4) #["hi","hi","hi","hi"]

print("Google" in list) #true

for x in list:
    print(x)

print(list[1]) #Runoob
print(list[-2]) #1997
print(list[1:]) #['Runoob', 1997, 2000]

# 嵌套列表
a=['a','b','a']
b=['b']
x=[a,b]
print(x)  #[['a', 'b', 'a'], ['b']]

# python列表函数与方法
print(len(a)) #3
print(max(a)) #b
print(min(a)) #a
# list(seq) 将元组转换为列表

a.append("ss") #在a的后面追加内容
print(a) #['a', 'b', 'a', 'ss']

print(a.count("a")) #2
a.extend(b)
print(a) #['a', 'b', 'a', 'ss','b']

print(a.index('a')) #0

a.insert(0,'ccc')
print(a) # ['ccc', 'a', 'b', 'a', 'ss', 'b']

print(a.pop(1))
print(a) #根据索引 移除 列表中的某一个元素

a.remove('a') #移除某个值的第一个匹配项
print(a)

a.sort() #对原列表进行排序
print(a)

a.clear() #清空列表
print(a)

a=['a','b','a']
n=a.copy() #复制列表
print(n)
