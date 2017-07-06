#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys

# 同一行显示多条语句
one = 'one'; sys.stdout.write(one + '\n')

# 行和缩进
if True:
    print "True"
elif False:
    print "False"
else:
    print "Other"

# 多行语句
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
print days

total = "item_one" + \
        "item_two" + \
        "item_three"

print "total is " + total

# 引号
word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""

# 多行注释
'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""

# print输出不换行

x="a"
y="b"
print x,
print y,
