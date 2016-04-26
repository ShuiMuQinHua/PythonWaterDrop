# -*- coding: UTF-8 -*-

# 导入模块  (import导入模块)
# from fib import fibonacci  (要导入模块fib的fibonacci函数)
# 现在可以调用模块里包含的函数了
from function import printme
printme("222")


Money = 2000
def AddMoney():
   # 想改正代码就取消以下注释:我们在全局命名空间里定义一个变量money。我们再在函数内给变量money赋值，然后Python会假定money是一个局部变量。然而，我们并没有在访问前声明一个局部变量money，结果就是会出现一个UnboundLocalError的错误。加上下面这句，就会修正错误
   global Money
   Money = Money + 1
 
print(Money)
AddMoney()
print(Money)


# 导入内置math模块
import math
 
content = dir(math)
 
print(content);


def test_globle():
	print(globals())

def test_locals():
	print(locals())

test_globle()
test_locals()







