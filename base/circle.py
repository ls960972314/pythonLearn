#!/usr/bin/python
# -*- coding: UTF-8 -*-

print """
----------------------if else----------------------
"""
str = "y"
if str == "y":
    print "y"
elif str == "z":
    print "z"
else:
    print "other"

print """
----------------------while----------------------
"""

count = 0
while count < 5:
    print count, " is  less than 5"
    count = count + 1
else:
    print count, " is not less than 5"

print """
----------------------for----------------------
"""

for num in range(10, 20):  # 迭代 10 到 20 之间的数字
    for i in range(2, num):  # 根据因子迭代
        if num % i == 0:  # 确定第一个因子
            j = num / i  # 计算第二个因子
            print '%d 等于 %d * %d' % (num, i, j)
            break  # 跳出当前循环
    else:  # 循环的 else 部分
        print num, '是一个质数'

# 输出 Python 的每个字母
for letter in 'Python':
    if letter == 'h':
        pass
        print '这是 pass 块'
    print '当前字母 :', letter

print "Good bye!"
