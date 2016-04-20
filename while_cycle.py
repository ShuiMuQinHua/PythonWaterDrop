# -*- coding: UTF-8 -*-

#import sys;
count = 0
while (count < 9):
	print('the count is:',count)
	count = count + 1

print("good bye!")

i = 1
while i < 10:
	i += 1
	if i % 2 >0:  #非偶数跳过输出
		continue
	print(i)      #输出偶数2、4、6、8、10

i = 1
while 1:
	print(i) 
	i += 1
	if i > 10:
		break

# var = 1
# while var == 1 : #条件为true，可以无限循环下去
# 	num = input("enter a number :")
# 	print("You entered: ", num)

# print("Good bye!")


count = 0
while count < 5:
	print(count,"is less than 5")
	count = count + 1
else:
	print(count,"is not less than 5")
