#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Video histogram sample to show live histogram of video

Keys:
    ESC    -exit

'''

import numpy as np
import cv2

# built-in modules
import sys

# local modules
import video


if __name__ == '__main__':

    # 构建 HSV 颜色地图
    hsv_map = np.zeros((180, 256, 3), np.uint8)
    # np.indices 可以返回由数组索引构建的新数组
    h, s = np.indices(hsv_map.shape[:2])
    hsv_map[:,:,0] = h
    hsv_map[:,:,1] = s
    hsv_map[:,:,2] = 255
    hsv_map = cv2.cvtColor(hsv_map, cv2.COLOR_HSV2BGR)
    cv2.imshow('hsv_map', hsv_map)

    cv2.namedWindow('hist', 0)
    hist_scale = 10

    def set_scale(val):
        global hist_scale
        hist_scale = val

    cv2.createTrackbar('scale', 'hist', hist_scale, 32, set_scale)

    try:
        fn = sys.argv[1]
    except:
        fn = 0

    cam = video.create_capture(fn, fallback='synth:bg=data/images/baboon.jpg:class=chess:noise=0.05')

    while (True):
        flag, frame = cam.read()
        cv2.imshow('camera', frame)

        # 图像金字塔
        # 通过图像金字塔降低分辨率，但不会对直方图有太大影响
        # 但这种低分辨率可以很好的抑制噪声，从而去除孤立的小点对直方图的影响
        small = cv2.pyrDown(frame)

        hsv = cv2.cvtColor(small, cv2.COLOR_BGR2HSV)

        # 取 V 通道（亮度）的值
        # 常见的用法 dark = hsv[:,:,2] < 32
        # 此步骤得到的是一个布尔矩阵，小于32的为真，大于32的为假
        dark = hsv[...,2] < 32
        h = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
        
        # np.clip(a, a_min, a_max, out = None)[source]
        # Given an interval, values outside the interval are clipped to the interval edges
        h = np.clip(h*0.005*hist_scale, 0, 1)

        # In numpy one can use the 'newaxis' object in the slicing syntax to create an 
        # axis of length one. one can also use None instead of newaxis,
        # the effect is exactly the same
        # h 从一维变成3维
        vis = hsv_map * h[:,:,np.newaxis] / 255.0
        cv2.imshow('hist', vis)

        ch = cv2.waitKey(1)
        if ch == 27:
            break

    cv2.destroyAllWindows()
