# -*- coding: UTF-8 -*-
#所有参数（变量）都是按引用传递
def printme(str):
	"打印传入的字符串到标准显示设备上"
	print(str)
	return;

#调用函数
printme("我要调用用户自定义函数！");
printme("再次调用同一函数");
printme(str = "关键字参数")  #使用关键字参数，参数顺序可以和申明时的顺序不一致，但是必须要保证和申明时的参数名称一样，它会自动根据参数名称进行匹配

#可写函数说明
def changeme(mylist):
	"修改传入的列表"
	mylist.append([1,2,3,4])
	print("函数内取值：",mylist)
	return

#调用changeme函数  内外取值，输出的结果是一样的，因为他们是同一个引用
mylist = [10,20,30]
changeme(mylist)
print("函数外取值：",mylist)


# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2;
 
# 调用sum函数
print("相加后的值为 : ", sum( 10, 20 ))
print("相加后的值为 : ", sum( 20, 20 ))


# 可写函数说明
def sum( arg1, arg2 ):
   # 返回2个参数的和."
   total = arg1 + arg2
   print("函数内 : ", total)
   return total;
 
# 调用sum函数
total = sum( 10, 20 );
print("函数外 : ", total)


#python的所有参数都是按引用传递
# 可写函数说明
def changeme(mylist):
	"修改传入的列表"
	mylist.append([1, 2, 3, 4]);
	print("函数内取值: ", mylist)
	return

# 调用changeme函数
mylist = [10, 20, 30];
changeme(mylist);
print("函数外取值: ", mylist)



# 加了星号（*）的变量名会存放所有未命名的变量参数。如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。
# 可写函数说明
def printinfo(arg1, *vartuple):
	"打印任何传入的参数"
	print("输出: ")
	print(arg1)
	for var in vartuple:
		print(var)
	return;

# 调用printinfo 函数
printinfo(10);
printinfo(70, 60, 50);


#匿名函数
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2;
# 调用sum函数
print("相加后的值为 : ", sum(10, 20))  #30
print("相加后的值为 : ", sum(20, 20))  #40



# return返回 练习
# 可写函数说明
def sum( arg1, arg2 ):
   # 返回2个参数的和."
   total = arg1 + arg2
   print ("函数内 : ", total)
   return total;

# 调用sum函数
total = sum( 10, 20 );
print ("函数外 : ", total)


