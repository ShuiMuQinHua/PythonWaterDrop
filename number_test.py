# -*- coding: UTF-8 -*-
import math
import random
a=1.0
print(a)  #1.0
print(int(a)) #1
print(a)  #1.0

b=2.5
c=a+b
print(c)

d=a-1*1
f=d/4
g=17/3
h=17//3
j=17%3

k=5**2  #5的平方
l=2**7 #2的7次方

r=1-10
m=abs(r) #取绝对值
math.ceil(4.1) #5返回数字的上入整数
math.fabs(-10) #返回数字的绝对值
math.floor(4.9) #返回4
max(1,2,4) #最大值
min(2,1,6) #最小值

#随机数函数
random.choice(range(10)) #从0到9中随机挑选一个整数
random.randrange(1,10,2) #从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
random()  #随机生成下一个实数，它在[0,1)范围内。
random.shuffle() #将序列的所有元素随机排序

