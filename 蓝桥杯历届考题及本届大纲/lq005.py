# -*- coding: utf-8 -*-
'''
绘制分形树
'''
import turtle as tt
# import turtle as tl

# 把树干画出来
tt.speed(300)
distance = 60
tt.left(90)
tt.penup()
tt.backward(distance)
tt.pendown()
tt.forward(distance)


# y型，指定长度和角度
def ybranch(new_distance, degree):
    if new_distance < 5:
        return
    tt.left(degree)
    tt.forward(new_distance)
    ybranch(new_distance / 4 * 3, degree)
    tt.backward(new_distance)
    tt.right(degree * 2)
    tt.forward(new_distance)
    ybranch(new_distance / 4 * 3, degree)
    tt.backward(new_distance)
    tt.left(degree)


ybranch(distance, 30)

tt.exitonclick()
'''
def draw_smalltree(tree_length, tree_angle):

    if tree_length >= 3:
        tl.forward(tree_length)  #往前画
        tl.right(tree_angle)  #往右转
        draw_smalltree(tree_length - 10, tree_angle)  #画下一枝，直到画到树枝长小于3

    tl.left(2 * tree_angle)  #转向画左
    draw_smalltree(tree_length - 10, tree_angle)  #直到画到树枝长小于3
    tl.rt(tree_angle)  #转到正向上的方向，然后回溯到上一层
    if tree_length <= 30:  #树枝长小于30，可以当作树叶了，树叶部分为绿色
        tl.pencolor('green')
    if tree_length > 30:
        tl.pencolor('brown')  #树干部分为棕色

    tl.backward(tree_length)  #往回画，回溯到上一层


def main():
    tl.penup()
    #tl.pencolor('green')
    tl.left(90)  #因为树是往上的，所以先把方向转左
    tl.backward(250)  #把起点放到底部
    tl.pendown()
    tree_length = 60  #我设置的最长树干为60
    tree_angle = 20  #树枝分叉角度，我设为20
    draw_smalltree(tree_length, tree_angle)
    tl.exitonclick()  #点击才关闭画画窗口


if __name__ == '__main__':
    main()
'''