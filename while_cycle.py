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

for letter in 'Python':     # 第一个实例
   print('当前字母 :', letter)

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print('当前单词 :', fruit)

print("Good bye!")

fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print('当前水果 :', fruits[index])

print("Good bye!")

for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j = num/i          # 计算第二个因子
         print('%d 等于 %d * %d' % (num,i,j))
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print(num, '是一个质数')

# 循环嵌套
i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print(i, " 是素数")
   i = i + 1

print("Good bye!")


