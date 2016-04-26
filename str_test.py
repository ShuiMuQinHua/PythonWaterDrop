# -*- coding: UTF-8 -*-

test_str = "zheshiwode"
print(test_str)
print(len(test_str))

test_list = ['a','b','c','d']
print(test_list)
print(test_list[1])
print(test_list[:])

test_list[:2] + ['bacon', 2*2]
print(test_list)

print(len(test_list))

test_list.append("e")
print(test_list)

a, b = 0, 1
while b < 10:
	print(b)
	a, b = b, a+b


x = 0
if x==0:
	print("x is zero")
elif x>0:
	print("x > 0")
else:
	print("x <0")


test = [1,2,3,4,5,6]
for i in test:
	print(i)


#如果你需要一个数值序列，内置函数 range() 会很方便，它生成一个等差级数链表
for i in range(5):
	print(i)



a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
	print(i, a[i])


def composer_zero(test_num):
	if test_num>0:
		print(1)
	elif test_num==0:
		print(0)
	else:
		print(-1)

composer_zero(22)


def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print(complaint)

ask_ok('sfd')