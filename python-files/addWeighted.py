#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('data/images/orange.png')

img2 = cv2.imread('data/images/apple.png')

def nothing( value ):
    pass

cv2.namedWindow('Image')
cv2.createTrackbar('Messing rate', 'Image', 1, 9, nothing)

while(1):
    a = cv2.getTrackbarPos('Messing rate', 'Image')
    img = cv2.addWeighted(img1, np.float32(a)/10, img2, 1-np.float32(a)/10, 0)

    cv2.imshow('Image', img)
    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()
