#! /usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

# Mouse callback function
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 10, (250, 0, 0), -1)

img = np.zeros( (512, 512, 3), np.uint8)
cv2.namedWindow( 'Example' )
cv2.setMouseCallback( 'Example', draw_circle )

while( 1 ):
    cv2.imshow('Example', img)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break;

cv2.destroyAllWindows()
