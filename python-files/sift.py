#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

img = cv2.imread('/Users/amourlee/Desktop/convex.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT()
kp = sift.detect(img_gray, None)

img = cv2.drawKeyPoints(img_gray, kp)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

