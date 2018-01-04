#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

cap = cv2.VideoCapture( 0 )

while(1):
    
    # 获取每一帧
    ret, frame = cap.read()

    # 转换到HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 设定蓝色的阈值
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 250, 250])

    # 设定绿色的阈值
    lower_green = np.array([50, 50, 50])
    upper_green = np.array([70, 250, 250])

    # 根据阈值构建掩模
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    # 对原图像和掩模进行位运算
    res_blue = cv2.bitwise_and( frame, frame, mask = mask_blue)
    res_green = cv2.bitwise_and( frame, frame, mask = mask_green)

    # 显示图像
    res = cv2.add(res_green, res_blue)
    cv2.imshow('frame', frame)
    cv2.imshow('hsv', hsv)
    # cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    k = cv2.waitKey(5)
    if k == ord('q'):
        break

cv2.destroyAllWindows()
