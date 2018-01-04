#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy

img1 = cv2.imread('/Users/amourlee/Desktop/convex.png', 0)
img2 = cv2.imread('/Users/amourlee/Desktop/convex2.png', 0)

ret, thresh = cv2.threshold(img1, 127, 255, 0)
ret, thresh2 = cv2.threshold(img2, 127, 255, 0)

image, contours, hierarchy = cv2.findContours(thresh, 2, 1)
cnt1 = contours[0]

image, contours, hierarchy = cv2.findContours(thresh2, 2, 1)
cnt2 = contours[0]

ret = cv2.matchShapes(cnt1, cnt2, 1, 0.0)
print ret
