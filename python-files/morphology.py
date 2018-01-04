#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

img = cv2.imread('data/images/j.png')
kernel = np.ones((5, 5), np.uint8)

erosion = cv2.erode(img, kernel, iterations = 1)
dilation = cv2.dilate(img, kernel, iterations = 1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

cv2.namedWindow('image')
cv2.namedWindow('erosion')
cv2.namedWindow('dilation')
cv2.namedWindow('opening')
cv2.namedWindow('closing')
cv2.namedWindow('gradient')

while(1):
    cv2.imshow('image', img)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)
    cv2.imshow('gradient', gradient)
    k = cv2.waitKey(0)
    if k == ord('q'):
        break;
cv2.destroyAllWindows()
