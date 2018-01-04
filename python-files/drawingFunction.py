#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw a diagonal blue line with thickness of 5px
cv2.line(img, (0, 0), (511, 511), (250, 0, 0), 5)

# Draw a rectangle
cv2.rectangle(img, (384, 0), (512, 128),  (0, 250, 0), 3)

# Draw a circle
cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)

# Draw a ellipse
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)

# Draw polygon
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape( (-1, 1, 2) )
# cv2.fillPoly(img, pts, 1)
cv2.fillConvexPoly(img, pts, (122, 250, 250), 1)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2)

cv2.namedWindow('Image')
cv2.imshow('Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
