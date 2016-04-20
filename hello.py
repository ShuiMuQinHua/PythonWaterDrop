# -*- coding: UTF-8 -*-

test_str = "hello,python!";
print(test_str);

if True :
	print("true")
else :
	print("false")

if False:
 	print("False")
else:
	print("222")
	print("True")


item_one=3
item_two=4
item_three=5
item=item_one+\
	 item_two+\
	 item_three
print(item)

"""
这是多行注释，
使用的是3个引号
"""

word='word'
sentence="这是一个句子"
paragraph="""这是一个段落。包含多个语句"""
print(word)
print(sentence)
print(paragraph)

import sys; x='runoob'; sys.stdout.write(x+'\n')


# expression=True
# if expression :
# 	suite1
# else :
# 	suite

a = b = c = 1
d,e,f=1,2,"123"
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# python的几种数据类型 Number(数字) String(字符串) List(列表) Tuple(元组) Dictionary(字典)

s = 'ilovepython' 
print(s[1:5])

# list数据类型  list是允许更新的
list = ['abcd',786,2.23,'john',70.2]
print(list)
print(list[0])
print(list[4])

# touple 元组数据类型  元组不允许更新
touple=('abcd',786,2.23,'john',70.2)
tinytuple = (123, 'john')
print(touple)  #打印出touple
print(touple[1:3]) #打印出第二个至第三个的元素
print(touple[2:]) # 打印出从第三个元素开始的所有元素
print(tinytuple*2) #打印两遍 tinytuple
print(touple+tinytuple) #打印两个元组的组合

# dictionary 字典数据类型  字典是无序的
dict = {}
dict['one'] = "this is one"
dict[2]="this is two"
tinydict = {'name':'john','code':6734,'dept':'sales'}
print(dict['one']) 
print(dict[2])
print(dict)
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

num = 56
print(hex(num))
















