#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('data/images/wiki.jpg', 0)

equ = cv2.equalizeHist(img)

# Stacking images side-by-side
res = np.hstack((img, equ))

#plt.subplot(121),plt.imshow(img, 'gray')
plt.subplot(111),plt.imshow(res, 'gray')

plt.show()
