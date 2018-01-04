#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

im = cv2.imread('data/images/rectangle.png')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray, 127, 255, 0)
image, contours0, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# cnt = contours0[0]
# M = cv2.moments(cnt)

# cx = int(M['m10']/M['m00'])
# cy = int(M['m01']/M['m00'])

# area = cv2.contourArea(cnt) 
# Or area = int(M['m00'])

# perimeter = cv2.arcLength(cnt, True)

# epsilon = 0.1 * perimeter
# approx = cv2.approxPolyDP(cnt, epsilon, True)

contours = [cv2.approxPolyDP(cnt, 3, True) for cnt in contours0]


im = cv2.drawContours(im, contours0, -1, (127, 255, 255), 3)


# print(approx[1])
# print(cnt)
# print(perimeter)
# print(area)
# print(M)
# print(M['m00'])

cv2.namedWindow('approx')
while(1):
    cv2.imshow('approx', im)
    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()
