# -*- coding: UTF-8 -*-

#数据结构练习
#列表当作堆栈用(后进先出)
stack=[1,2,3,4,5]
stack.append(6)
stack.append(7)
print(stack) #[1,2,3,4,5,6,7]
print(stack.pop()) #7
print(stack.pop()) #6
print(stack) #[1,2,3,4,5]


#将列表当作队列使用
