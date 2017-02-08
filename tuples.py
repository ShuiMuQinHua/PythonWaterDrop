# -*- coding: UTF-8 -*-
#元组练习
# Python 的元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号，列表使用方括号。
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可

tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"
tup4 = () #创建空元组
tup5 = (50,) #元组中只包含一个元素时，需要在元素后面添加逗号
print(tup3) # ('a', 'b', 'c', 'd')
print(tup5) #(50,)

print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])


#元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz')
# 以下修改元组元素操作是非法的。
# tup1[0] = 100
tup3 = tup1 + tup2;
print (tup3) #(12, 34.56, 'abc', 'xyz')

tup=('Google', 'Runoob', 1997, 2000)
print (tup)
del tup;
print ("删除后的元组 tup : ")
# print (tup)  #以上实例元组被删除后，输出变量会有异常信息

tup = ('Google', 'Runoob', 1997, 2000)
print(len(tup)) #4
print(tup+tup) #('Google', 'Runoob', 1997, 2000,'Google', 'Runoob', 1997, 2000)

tup8=["hi"]
print(tup8*4) #("hi","hi","hi","hi")

print("Google" in tup) #true

for x in tup:
    print(x)

print(tup[1]) #Runoob
print(tup[-2]) #1997
print(tup[1:]) #('Runoob', 1997, 2000)

a=('a','b','a')
print(len(a)) #3
print(max(a)) #b
print(min(a)) #a
# tuple(seq) 将列表转换为元组


