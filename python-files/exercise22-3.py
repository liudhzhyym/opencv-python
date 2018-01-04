#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt
from time import clock
import sys

# import video
# video模块也是opencv官方文档中自带的

if __name__ == '__main__':

    # 构建HSV颜色地图
    hsv_map = np.zeros((180, 256, 3), np.uint8)

    h, s = np.indices(hsv_map.shape[:2])
    hsv_map[:,:,0] = h
    hsv_map[:,:,1] = s
    hsv_map[:,:,2] = 255
    hsv_map = cv2.cvtColor(hsv_map, cv2.COLOR_HSV2BGR)

    cv2.namedWindow('hsv_map')
    cv2.imshow('hsv_map', hsv_map)

    cv2.namedWindow('hist', 0)
    hist_scale = 10
    def set_scale(val):
        global hist_scale
        hist_scale = val

    cv2.createTrackbar('scale', 'hist', hist_scale, 32, set_scale)

    try: fn = sys.argv[1]
    except: fn = 0
    cam = video.create_capture(fn, fallback=' ')

    while True:
        flag, frame = cam.read()
        cv2.imshow('camera', frame)

        small = cv2.pyrDown(frame)
        hsv = cv2.cvColor(frame, cv2.COLOR_BGR2HSV)

        dark = hsv[:,:,2] < 32

        hsv[dark] = 0

        h = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

        h = np.clip(h * 0.005 * hist_scale, 0, 1)

        vis = hsv_map * h[:,:,np.newaxis] / 255.0
        cv2.imshow('hist', vis)
        ch = 0xFF & cv2.waitKey(1) 
        if ch == 27:
            break

    cv2.waitKey(0)

cv2.destroyAllWindows()


