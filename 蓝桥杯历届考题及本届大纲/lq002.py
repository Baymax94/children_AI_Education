#!/usr/bin/python
# -*- coding: UTF-8 -*-
for i in range(0, 10, 1):
    for j in range(0, 10, 1):
        for k in range(0, 10, 1):
            if (i == 3) or (j == 3) or (k == 3):
                if (i == 3) and (j == 3):
                    a = i * 100 + j * 10 + k
                    c = 0
                    for b in range(2, a // 2 + 1):
                        if (a % b) == 0:
                            c = 1
                            break
                    if c == 1:
                        print('&', a)
                    else:
                        print('&', a, '*')
                elif (j == 3) and (k == 3):
                    a = i * 100 + j * 10 + k
                    c = 0
                    for b in range(2, a // 2 + 1):
                        if (a % b) == 0:
                            c = 1
                            break
                    if c == 1:
                        print('&', a)
                    else:
                        print('&', a, '*')
                else:
                    a = i * 100 + j * 10 + k
                    c = 0
                    for b in range(2, a // 2 + 1):
                        if (a % b) == 0:
                            c = 1
                            break
                    if c == 1:
                        print(a)
                    else:
                        print(a, '*')
