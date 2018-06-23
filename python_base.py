# /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "0LIN1ISA"
# Date:2018/6/22 21:26

"""类型和运算----类型和运算----类型和运算----类型和运算----类型和运算----类型和运算----类型和运算----类型和运算----类型和运算"""

# 寻求帮助
import os

obj = os
dir(obj)  # 简单的列出对象obj所包含的方法名称，返回一个字符串列表
help(obj.kill)  # 查询obj.func的具体介绍和用法

# 测试类型的三种方法
L = [1, 'a']
if type(L) == type([]):
    print('L is list')
if type(L) == list:
    print('L is list')
if isinstance(L, list):  # 推荐使用isinstance方法
    print('L is list')

# Python类型分为哈希类型和不可哈希类型

# 哈希类型，即在原地不能改变的变量类型，不可变类型。可使用hash函数查看其hash值，也可以作为字典的key。
# 包括以下类型
# 1：数字类型：int,float,decimal.Decimal,fractions.Fraction,complex
# 2：字符串类型：str,bytes
# 3：元组：tuple
# 4：冻结集合：frozenset
# 5：布尔类型：True,False
# 6：空类型：None

# 不可哈希类型，原地可变类型：list,dict和set。他们不可以作为字典的Key。

# 数字常量
1234, -1234, 0, 9999999  # 整数
1.23, 1., 3.14e-10, 4E210, 4.0e+210  # 浮点数
0o177, 0x9ff, 0x9FF, 0b101010  # 八进制，十六进制，二进制数字
3 + 4j, 3.0 + 4.0j, 3J  # 复数常量，也可以用complex(real,image)来创建
hex(10), oct(10), bin(10)  # 将十进制数转换为16进制，8进制和2进制
# 在2.x中，有两种类型：一般整数（32位）和长整数（无穷进度）。可以用l或L结尾，迫使一般整数成为长整数。
float('inf'), float('-inf'), float('nan')  # 无穷大，无穷小，非数

# 数字的表达式操作符
"""
yield x  # 生成器函数发送协议
lambda args: expression  # 生成匿名函数
x if y else z  # 三元选择表达式
x and y, x or y, not x  # 逻辑与，逻辑或，逻辑非
x in y, x not in y  # 成员对象测试
x is y, x is not y  # 对象实体测试
x < y, x <= y, x > y, x >= y, x == y, x != y  # 大小比较，集合子集或超集值相当性操作符
a = 3
print(1 < a < 3)  # python允许连续比较
x | y, x & y, x ^ y  # 位或，位与，位异或
x << y, x >> y  # 位操作：x左移，y右移
+, -, *, /, //, %, **  # 真除法，floor除法：返回不大于真除法结果的整数值，取余，幂运算
-x, +x, ~x  # 一元减法，识别、按位求补（取反）
x[i], x[i:j:k]  # 索引，切片，调用
int(3.14), float(3)  # 强制类型转换
"""

# 整数可以使用bit_length函数测试所占位数
a = 1
print(a.bit_length())
b = 1024
print(bin(1024))  # 0b10000000000
print(b.bit_length())

# repr和str显示格式的区别
"""
repr格式：默认的交互模式回显，产生的结果看起来他们就像是代码。
str格式：打印语句，转换成对用户更加友好的格式。
"""

# 数字相关的模块
# math模块
# Decimal模块:小数模块
import decimal
from decimal import Decimal

Decimal('0.01') + Decimal('0.02')  # 返回Decimal('0.03')
decimal.getcontext().prec = 4  # 设置全局精度为4，即小数点后边为4位
print(Decimal('0.01') + Decimal('0.02'))
# Fraction模块：分数模块
from fractions import Fraction

x = Fraction(4, 6)  # 分数类型 4/6
print(x)
x = Fraction('0.25')  # 分数类型 1/4 接受字符串类型参数
print(x)

# 集合set
"""
set是一个无序不重复元素集，基本功能包括关系测试和消除重复元素。
set支持union（联合），intersection（交），difference（差）和symmetric difference（对称差集）等数学运算。
set支持x in set，len(set)，for x in set等操作。
set不记录元素位置或者插入点，因此不支持indexing，slicing，或其他类序列的操作。
"""

s = set([3, 5, 9, 10])  # 创建一个数值集合，返回{3,5,9,10}
t = set("Hello")  # 创建一个唯一字符的集合返回{'l', 'H', 'e', 'o'}

a = t | s
a = t.union(s)  # t和s的并集

b = t & s
b = t.intersection(s)  # t和s的交集

c = t - s
c = t.difference(s)  # 求差集（项在t中，但不在s中）
