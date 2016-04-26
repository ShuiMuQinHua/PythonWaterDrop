# -*- coding: UTF-8 -*-

# 打开一个文件
fo = open("foo.txt", "w")
# print("文件名: ", fo.name)
# print("是否已关闭 : ", fo.closed)
# print("访问模式 : ", fo.mode)
# str = "www.runoob.com!"
fo.write("www.runoob.com!\nVery good site!\n");
# print("末尾是否强制加空格 : ", fo.softspace)
fo.close()


# 打开一个文件
fo = open("foo.txt", "r+")
str = fo.read(100);
print("读取的字符串是 : ", str)
# 关闭打开的文件
fo.close()


# 打开一个文件
fo = open("foo.txt", "r+")
str = fo.read(10);
print("读取的字符串是 : ", str)
 
# 查找当前位置
position = fo.tell();
print("当前文件位置 : ", position)
 
# 把指针再次重新定位到文件开头
position = fo.seek(0, 0);
str = fo.read(10);
print("重新读取字符串 : ", str)
# 关闭打开的文件
fo.close()


import os
 
# 重命名文件foo.txt到test2.txt。
# os.rename( "foo.txt", "test.txt")
# 删除文件
# os.remove("11.txt")
# 创建一个新的目录
# os.mkdir("test")
# os.remove("test")
# 获取当前的工作目录
print(os.getcwd())




