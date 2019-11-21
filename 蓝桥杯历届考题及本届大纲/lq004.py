#!/usr/bin/python
# -*- coding: UTF-8 -*-
import turtle
import random

# 画布大小，宽800，高600
turtle.screensize(800, 600, "white")
# 线宽为5
turtle.pensize(5)
# 绘图速度为7
turtle.speed(7)
'''
# 线段颜色为黑色
turtle.pencolor("black")
# 填充颜色为黄色
turtle.fillcolor("yellow")
'''
# 同时设置画笔颜色和填充颜色
turtle.color("black", "yellow")


def Pentagram():
    L = random.randint(10, 150)
    turtle.begin_fill()
    for a in range(5):
        turtle.forward(L)
        turtle.right(144)
    turtle.end_fill()


for b in range(5):
    turtle.penup()
    x = random.randint(-400, 400)
    y = random.randint(-150, 150)
    turtle.goto(x, y)
    Pentagram()

turtle.mainloop()

# https://www.cnblogs.com/chen0307/articles/9645138.html
