#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

# roi is the object or region of object we need to find
roi = cv2.imread('data/images/football.png')
hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# target is the image we search in 
target = cv2.imread('data/images/glass.png')
hsvt = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)

# calculating object histogram
roihist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0 ,256])

# normalize histogram and apply backprojection
# 归一化： 原始图像，结果图像，映射到结果图像中的最小值，最大值，归一化类型
# cv2.NORM_MINMAX 对数组的所有值进行转换，使他们线性映射到最小值和最大值之间
cv2.normalize(roihist, roihist, 0, 255, cv2.NORM_MINMAX)

dst = cv2.calcBackProject([hsvt], [0, 1], roihist, [0, 180, 0, 256], 1)

# now convolute with circular disc
# 此处卷积可以把分散的点连在一起
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
dst = cv2.filter2D(dst, -1, disc)

# thresholding and binary AND
ret, thresh = cv2.threshold(dst, 50, 250, 0)
# 三通道图像，使用merge.
thresh = cv2.merge((thresh, thresh, thresh))

cv2.imshow('thresh', thresh)
# 按位操作
res = cv2.bitwise_and(target, thresh)

res = np.hstack((target, thresh, res))
cv2.imshow('1', res)
cv2.waitKey(0)

cv2.destroyAllWindows()
