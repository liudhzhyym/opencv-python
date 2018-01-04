#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

#mouse callback function
previouspt=(0,0)
def draw_line(event, x, y, flags, param):
    global previouspt
    if event == cv2.EVENT_LBUTTONDOWN:
        previouspt=(x, y)
    if event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):
        cv2.line(img, previouspt, (x, y), (0,250,0), 1)
        previouspt = (x, y)

# 创建图像与窗口并将窗口与回调函数绑定

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_line)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()


