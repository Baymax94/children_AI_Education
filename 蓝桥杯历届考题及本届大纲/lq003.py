#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re  # 正则表达式

txt = input("Please input number: ")
lis = re.findall(r'\d+\.?\d*', txt)
new_lis = list(map(int, lis))

# 输入的数字所对应的字母
print(new_lis)
text = ""
for x in range(len(new_lis)):
    if new_lis[x] > 27:
        b = '[bad]'
        text = text + b
    else:
        a = new_lis[x] + 64
        text = text + chr(a)
print(text)

# 输入数字的个数
L = len(new_lis)
print("数字个数：", L)
# 输入的最小数字
print("最小数字：", min(new_lis))
# 输入的数字从大到小排列
# 外层循环确定比较的轮数，x是下标，lt[x]在外层循环中代表lt中所有元素
lt = new_lis
for x in range(L - 1):
    #内层循环开始比较
    for y in range(x + 1, L):
        #lt[x]在for y 循环中是代表特定的元素，lt [y]代表任意一个lt任意一个元素。
        if lt[x] < lt[y]:
            #让lt[x]和lt列表中每一个元素比较，找出小的
            lt[x], lt[y] = lt[y], lt[x]
print("从大到小：", lt)
