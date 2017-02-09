# -*- coding: UTF-8 -*-
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数

a , b = 0 , 1
while b<100:
    print(b)
    a , b = b,a + b

#end关键字  关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符
a, b = 0, 1
while b < 100:
    print(b, end=',')
    a, b = b, a+b