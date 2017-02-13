# -*- coding: UTF-8 -*-

var1='hello world!'
var2="runoob"
print("var1[0]:",var1[0]) #h
print("var2[1:5]:",var2[1:5]) #unoo

print("已更新的字符串:",var1[:6]+"runoob!")

a = "Hello"
b = "Python"

print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])

# 成员运算符
if( "H" in a) :
    print("H 在变量 a 中")
else :
	print("H 不在变量 a 中")

if( "M" not in a) :
    print("M 不在变量 a 中")
else :
	print("M 在变量 a 中")

print (r'\n')
print (R'\n')

#python字符串格式化
print("我叫 %s 今年 %d 岁!" % ('小明',10))

# python三引号 python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)

# pythob内建函数
name="cyy"
print(name.capitalize()) #Cyy
print(name.center(10,'*')) #***cyy****
print(name.count("y",0)) #2

byts=name.encode()
print(byts) #b'cyy'
print(byts.decode()) #cyy

print(name.endswith("y")) #true

tabtest="aaaertet"
print(tabtest.expandtabs())

print(tabtest.find('f')) #-1 返回索引 不存在则返回-1
print(tabtest.index('a')) # 不存在的 会发生警告

allnum="1234aaa"
allnum2="123ddd_"
print(allnum.isalnum()) #true  至少有一个字符并且所有的字符都是字母或者数字则返回true
print(allnum2.isalnum()) #false

allchar="sede"
print(allchar.isalpha()) # 至少有一个字符并且所有的字符都是字母则返回true


allnums="123"
print(allnums.isdigit()) # true 如果字符串只包含数字则返回 True 否则返回 False..

lower="123aws"
print(lower.islower()) #true 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False

numeric="1234"
print(numeric.isnumeric()) #true 如果字符串中只包含数字字符，则返回 True，否则返回 False

space=" "
print(space.isspace()) #true 如果字符串中只包含空格，则返回 True，否则返回 False.

# istitle() 返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
# isupper()
# join(seq)
# len(string)
# ljust(width[,fillchar])
# lower()
# lstrip()
# maketrans()
# max(str)
# min(str)
# replace(old, new [, max])
# rfind(str, beg=0,end=len(string))
# rindex( str, beg=0, end=len(string))
# rjust(width, [, fillchar])
# rstrip()
# split(str="", num=string.count(str))
# splitlines([keepends])
# startswith(str, beg=0,end=len(string))
# strip([chars])
# swapcase()
# title()
# translate(table, deletechars="")
# upper()
# zfill (width)
# isdecimal()





