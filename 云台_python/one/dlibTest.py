#!Anaconda/anaconda/python
#coding: utf-8

import dlib                     #人脸识别的库dlib
import numpy as np              #数据处理的库numpy
import cv2                      #图像处理的库OpenCv
from pyfirmata import Arduino, util
import time
import serial

class face_emotion():

    def __init__(self):
        # 使用特征提取器get_frontal_face_detector
        self.detector = dlib.get_frontal_face_detector()
        # dlib的68点模型，使用作者训练好的特征预测器
        self.predictor = dlib.shape_predictor("D:/wp_python/Nano/venv/shape_predictor_68_face_landmarks.dat")

        #建cv2摄像头对象，这里使用电脑自带摄像头，如果接了外部摄像头，则自动切换到外部摄像头
        self.cap = cv2.VideoCapture(0)
        # 设置视频参数，propId设置的视频参数，value设置的参数值
        self.cap.set(3, 480)
        # 截图screenshoot的计数器
        self.cnt = 0
        self.ser = serial.Serial()
        self.ser.baudrate = 9600  # 设置波特率
        self.ser.port = "COM3"  # 端口是COM3
        self.ser.open()  # 打开串口


    def learning_face(self):
        # cap.isOpened（） 返回true/false 检查初始化是否成功
        while(self.cap.isOpened()):

            # cap.read()
            # 返回两个值：
            #    一个布尔值true/false，用来判断读取视频是否成功/是否到视频末尾
            #    图像对象，图像的三维矩阵
            flag, im_rd = self.cap.read()

            # 每帧数据延时1ms，延时为0读取的是静态帧
            k = cv2.waitKey(1)

            # 取灰度
            img_gray = cv2.cvtColor(im_rd, cv2.COLOR_RGB2GRAY)

            # 使用人脸检测器检测每一帧图像中的人脸。并返回人脸数rects
            faces = self.detector(img_gray, 0)

            # 待会要显示在屏幕上的字体
            font = cv2.FONT_HERSHEY_SIMPLEX

            # 如果检测到人脸
            if(len(faces)!=0):

                # 对每个人脸都标出68个特征点
                for i in range(len(faces)):
                    # enumerate方法同时返回数据对象的索引和数据，k为索引，d为faces中的对象
                    for k, d in enumerate(faces):

                        cv2.rectangle(im_rd, (d.left(), d.top()), (d.right(), d.bottom()), (0, 0, 255))
                        fw(self,d.top(),d.bottom(),d.left(),d.right())

                        # 计算人脸热别框边长
                        self.face_width = d.right() - d.left()

                # 标出人脸数
                cv2.putText(im_rd, "Faces: "+str(len(faces)), (20,50), font, 1, (0, 0, 255), 1, cv2.LINE_AA)
            else:
                # 没有检测到人脸
                cv2.putText(im_rd, "No Face", (20, 50), font, 1, (0, 0, 255), 1, cv2.LINE_AA)

            # 窗口显示
            cv2.imshow("camera", im_rd)

        # 释放摄像头
        self.cap.release()

        # 删除建立的窗口
        cv2.destroyAllWindows()

def fw(self,t,b,l,r):
    #print(str((d.left() / 2 + d.right() / 2) - 300) + " " + str((d.top() / 2 + d.bottom() / 2) - 250))
    y = (b - t) / 2 + t;
    x = (r - l) / 2 + l;
    print(str(t)+"    "+str(b)+"   "+str(l)+"   "+str(r))
    print("    " +str(x) + "   " + str(y))

    if(x-280>=50 and abs(y-300)<=40):
        print("右")
        self.ser.write(b"5")
    elif (x - 280 >= 50 and y - 300 >= 40):
        print("右下")
        self.ser.write(b"2")
    elif (x - 280 >= 50 and y - 300<=-40):
        print("右上")
        self.ser.write(b"0")
    elif (x - 280 <= -50 and abs(y-300)<=40):
        print("左")
        self.ser.write(b"6")
    elif (x - 280 <= -50 and y-300<=-40):
        print("左上")
        self.ser.write(b"1")
    elif (x - 280 <= -50 and y-300 >= 40):
        print("左下")
        self.ser.write(b"3")
    elif (abs(x - 280) <= 50 and y-300>=40):
        print("下")
        self.ser.write(b"7")
    elif (abs(x - 280) <= 50 and y-300<=-40):
        print("上")
        self.ser.write(b"4")



if __name__ == "__main__":
    my_face = face_emotion()
    my_face.learning_face()