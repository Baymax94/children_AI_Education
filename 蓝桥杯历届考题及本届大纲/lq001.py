#!/usr/bin/python
# -*- coding: UTF-8 -*-
num = 0
L = [1, 3, 5, 8]
for i in range(0, 4, 1):
    for j in range(0, 4, 1):
        for k in range(0, 4, 1):
            if (i != j) and (i != k) and (j != k):
                a = 100 * L[i] + 10 * L[j] + L[k]
                num = num + 1
                print(a)
print(num)