#!/usr/bin/python
# -*- coding: UTF-8 -*-

tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );

print "tup1[0]: ", tup1[0]
print "tup2[1:5]: ", tup2[1:5]

"""
元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
"""

tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

# 以下修改元组元素操作是非法的。
# tup1[0] = 100;

# 创建一个新的元组
tup3 = tup1 + tup2;
print tup3;


"""
元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
"""
tup = ('physics', 'chemistry', 1997, 2000);

print tup;
del tup;

"""
任意无符号的对象，以逗号隔开，默认为元组
"""
print 'abc', -4.24e93, 18+6.6j, 'xyz';
x, y = 1, 2;
print "Value of x , y : ", x,y;
