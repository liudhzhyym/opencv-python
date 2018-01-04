#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread('../data/images/football.png', 0)

cv2.namedWindow('Canny')

cv2.createTrackbar('minVal', 'Canny', 100, 300, nothing)
cv2.createTrackbar('maxVal', 'Canny', 200, 400, nothing)

switch = '0:OFF\n1:ON'
cv2.createTrackbar(switch, 'Canny', 0, 1, nothing)

while(1):
    min_val = cv2.getTrackbarPos('minVal', 'Canny')
    max_val = cv2.getTrackbarPos('maxVal', 'Canny')
    s = cv2.getTrackbarPos(switch, 'Canny')

    if s == 0:
        img2 = cv2.Canny(img, 100, 200)
    else:
        img2 = cv2.Canny(img, min_val, max_val)
    
    cv2.imshow('Canny', img2)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
