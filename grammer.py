# -*- coding: UTF-8 -*-

# 反斜线换行
item_one=1
item_two=2
item_three=3
total=item_one+\
    item_two+\
    item_three
print(total)

# [],{},()中的换行 不需要反斜线
total=['item_one', 'item_two', 'item_three',
       'item_four', 'item_five']
print(total)

#python中单引号和双引号完全相同
#使用三引号('''或""")可以指定一个多行字符串
word='字符串'
sentence="这是一个句子"
para="""这是一个段落，
可以由多行组成"""
print(word)
print(sentence)
print(para)

# 给多个变量赋值
a = b = c = 1
print(a)
print(b)
print(c)
a, b, c = 1, 2, "runoob"
print(a)
print(b)
print(c)
