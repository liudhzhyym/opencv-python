#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/Users/amourlee/Desktop/convex.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# find Harris corners
gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
dst = cv2.dilate(dst, None)
ret, dst = cv2.threshold(dst, 0.01*dst.max(), 255, 0)
dst = np.uint8(dst)

ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

# define the criteria to stop and refine the corners
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)

# Python: cv2.cornerSubPix(image, corners, winSize, zeroZone, criteria)
# zeroZone – Half of the size of the dead region in the middle of the search zone 
# over which the summation in the formula below is not done. It is used sometimes
# to avoid possible singularities of the autocorrelation matrix. The value of (-1,-1) 
# indicates that there is no such a size.

corners = cv2.cornerSubPix(gray, np.float32(centroids), (5, 5),(-1, -1), criteria)

# Now draw them
res = np.hstack((centroids, corners))
# np.int0 可以用来省略小数点后面的数字
res = np.int0(res)
img[res[:, 1], res[:, 0]] = [0, 0, 255]
img[res[:, 3], res[:, 2]] = [0, 255, 0]

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
