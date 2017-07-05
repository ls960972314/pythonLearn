#!/usr/bin/python
# -*- coding: UTF-8 -*-

print '''
python算数运算符
'''
a = 21
b = 10
c = 0

c = a + b
print "21 + 10 的值为：", c

c = a - b
print "21 - 10 的值为：", c

c = a * b
print "21 * 10 的值为：", c

c = a / b
print "21 ／ 10 的值为：", c
print "21.0 / 10 的值为:", 21.0 / 10

c = a % b
print "21 % 10 的值为：", c

# 修改变量 a 、b 、c
a = 2
b = 3
c = a ** b
print "2 ** 3 的值为：", c

a = 10
b = 5
c = a // b
print "10 ／／ 5 的值为：", c

print '''
Python比较运算符
'''
c = 0

if (a == b):
    print "1 - a 等于 b"
else:
    print "1 - a 不等于 b"

if (a != b):
    print "2 - a 不等于 b"
else:
    print "2 - a 等于 b"

if (a <> b):
    print "3 - a 不等于 b"
else:
    print "3 - a 等于 b"

if (a < b):
    print "4 - a 小于 b"
else:
    print "4 - a 大于等于 b"

if (a > b):
    print "5 - a 大于 b"
else:
    print "5 - a 小于等于 b"

# 修改变量 a 和 b 的值
a = 5;
b = 20;
if (a <= b):
    print "6 - a 小于等于 b"
else:
    print "6 - a 大于  b"

if (b >= a):
    print "7 - b 大于等于 a"
else:
    print "7 - b 小于 a"

print '''
Python赋值运算符
'''
a = 21
b = 10
c = 0

c = a + b
print "1 - c 的值为：", c

c += a
print "2 - c 的值为：", c

c *= a
print "3 - c 的值为：", c

c /= a
print "4 - c 的值为：", c

c = 2
c %= a
print "5 - c 的值为：", c

c **= a
print "6 - c 的值为：", c

c //= a
print "7 - c 的值为：", c

print '''
Python位运算符
'''
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0

c = a & b;  # 12 = 0000 1100
print "1 - c 的值为：", c

c = a | b;  # 61 = 0011 1101
print "2 - c 的值为：", c

c = a ^ b;  # 49 = 0011 0001
print "3 - c 的值为：", c

c = ~a;  # -61 = 1100 0011
print "4 - c 的值为：", c

c = a << 2;  # 240 = 1111 0000
print "5 - c 的值为：", c

c = a >> 2;  # 15 = 0000 1111
print "6 - c 的值为：", c

print '''
Python逻辑运算符
'''
a = 10
b = 20

if (a and b):
    print "1 - 变量 a 和 b 都为 true"
else:
    print "1 - 变量 a 和 b 有一个不为 true"

if (a or b):
    print "2 - 变量 a 和 b 都为 true，或其中一个变量为 true"
else:
    print "2 - 变量 a 和 b 都不为 true"

# 修改变量 a 的值
a = 0
if (a and b):
    print "3 - 变量 a 和 b 都为 true"
else:
    print "3 - 变量 a 和 b 有一个不为 true"

if (a or b):
    print "4 - 变量 a 和 b 都为 true，或其中一个变量为 true"
else:
    print "4 - 变量 a 和 b 都不为 true"

if not (a and b):
    print "5 - 变量 a 和 b 都为 false，或其中一个变量为 false"
else:
    print "5 - 变量 a 和 b 都为 true"

print '''
Python成员运算符
'''
a = 10
b = 20
list = [1, 2, 3, 4, 5];

if (a in list):
    print "1 - 变量 a 在给定的列表中 list 中"
else:
    print "1 - 变量 a 不在给定的列表中 list 中"

if (b not in list):
    print "2 - 变量 b 不在给定的列表中 list 中"
else:
    print "2 - 变量 b 在给定的列表中 list 中"

# 修改变量 a 的值
a = 2
if (a in list):
    print "3 - 变量 a 在给定的列表中 list 中"
else:
    print "3 - 变量 a 不在给定的列表中 list 中"

print '''
Python身份运算符
'''
a = 20
b = 20

if (a is b):
    print "1 - a 和 b 有相同的标识"
else:
    print "1 - a 和 b 没有相同的标识"

if (a is not b):
    print "2 - a 和 b 没有相同的标识"
else:
    print "2 - a 和 b 有相同的标识"

# 修改变量 b 的值
b = 30
if (a is b):
    print "3 - a 和 b 有相同的标识"
else:
    print "3 - a 和 b 没有相同的标识"

if (a is not b):
    print "4 - a 和 b 没有相同的标识"
else:
    print "4 - a 和 b 有相同的标识"

print '''
Python运算符优先级
'''

a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d  # ( 30 * 15 ) / 5
print "(a + b) * c / d 运算结果为：", e

e = ((a + b) * c) / d  # (30 * 15 ) / 5
print "((a + b) * c) / d 运算结果为：", e

e = (a + b) * (c / d);  # (30) * (15/5)
print "(a + b) * (c / d) 运算结果为：", e

e = a + (b * c) / d;  # 20 + (150/5)
print "a + (b * c) / d 运算结果为：", e

print '''
python中会为每个出现的对象分配内存，哪怕他们的值完全相等（注意是相等不是相同）。
如执行a=2.0，b=2.0这两个语句时会先后为2.0这个Float类型对象分配内存，然后将a与b分别指向这两个对象。所以a与b指向的不是同一对象：
'''

a = 2.0
b = 2.0
a is b  # 结果为False
a == b  # 结果为True
print '''
但是为了提高内存利用效率对于一些简单的对象，如一些数值较小的int对象，
python采取重用对象内存的办法，如指向a=2，b=2时，由于2作为简单的int类型且数值小，python不会两次为其分配内存，而是只分配一次，然后将a与b同时指向已分配的对象：
'''
a = 2
b = 2
a is b  # 结果为True
a == b  # 结果为True
print '''
如但果赋值的不是2而是大的数值，情况就跟前面的一样了：
'''
a = 4444
b = 4444
a is b  # 结果为False
a == b  # 结果为True
