# -*- coding: UTF-8 -*-

import time; #引入time模块

ticks = time.time()
print("当前时间戳为:",ticks)

#获取当前时间
localtime1 = time.localtime(time.time())
print("本地时间为 :", localtime1)

#格式化输出当前时间
localtime2 = time.asctime( time.localtime(time.time()) )
print("本地时间为 :", localtime2)

import time
#格式化日期
# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
  
# # 将格式字符串转换为时间戳
# a = "2016-03-20 11:45:39"
# print(time.mktime(time.strptime(a,'%Y-%m-%d %H:%M:%S')))

# # #将"2011-09-28 10:00:00"转化为时间戳
# # time.mktime(time.strptime(a,'%Y-%m-%d %H:%M:%S'))

#日历
import calendar

cal = calendar.month(2016,1)
print("以下输出2016年1月份的日历：")
print(cal);



