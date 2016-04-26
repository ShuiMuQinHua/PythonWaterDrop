# -*- coding: UTF-8 -*-

# break语句
for letter in 'Python':     # First Example
   if letter == 'h':
      break
   print('Current Letter :', letter)
  
var = 10                    # Second Example
while var > 0:              
   print('Current variable value :', var)
   var = var -1
   if var == 5:
      break

print("Good bye!")


# continue语句
for letter in 'Python':     # 第一个实例
   if letter == 'h':
      continue
   print('当前字母 :', letter)

var = 10                    # 第二个实例
while var > 0:              
   var = var -1
   if var == 5:
      continue
   print('当前变量值 :', var)
print("Good bye!")


# 输出 Python 的每个字母
for letter in 'Python':
   if letter == 'h':
      pass
      print('这是 pass 块')
   print('当前字母 :', letter)

print("Good bye!")


