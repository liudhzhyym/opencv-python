#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

img = cv2.imread('data/images/meixi.png', 0)

rows, cols = img.shape

M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 0.6)

dst = cv2.warpAffine(img, M, (2*cols, 2*rows))

cv2.imshow('Image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
