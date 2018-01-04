#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib as plt

img = cv2.imread('/Users/amourlee/Desktop/ccc.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(img_gray)

dst = cv2.cornerHarris(gray, 2, 3, 0.04)

dst = cv2.dilate(dst, None)

img[dst > 0.1 * dst.max()] = [0, 0, 255]

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
