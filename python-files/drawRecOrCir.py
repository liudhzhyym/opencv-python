#! /usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

# 当鼠标按下时变为True
drawing = False

# 如果mode为True绘制矩形，按下‘m’变成绘制曲线
mode = True
ix, iy = -1, -1

# 创建回调函数
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                # 绘制圆圈，小圆点连在一起就成了线
                cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

# Create image window
img = np.zeros((512, 512, 3), np.uint8)

cv2.namedWindow('Image')
cv2.setMouseCallback('Image', draw_circle)

while(1):
    cv2.imshow('Image', img)
    k = cv2.waitKey(1)
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()

