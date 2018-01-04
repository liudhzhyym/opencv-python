#! /usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow( 'Image' )

cv2.createTrackbar( 'Red', 'Image', 0, 255, nothing)
cv2.createTrackbar( 'Green', 'Image', 0, 255, nothing)
cv2.createTrackbar( 'Blue', 'Image', 0, 255, nothing)

switch = '0:OFF\n1:ON'
cv2.createTrackbar(switch, 'Image', 0, 1, nothing)

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

while (1):
    cv2.imshow('Image', img)
    k = cv2.waitKey(1)
    if k == 27:
        break

    r = cv2.getTrackbarPos('Red', 'Image')
    g = cv2.getTrackbarPos('Green', 'Image')
    b = cv2.getTrackbarPos('Blue', 'Image')
    s = cv2.getTrackbarPos(switch, 'Image')

    if s == 0:
        img[:] = 0
    else:
        img[:]=[b, g, r]

cv2.destroyAllWindows()
