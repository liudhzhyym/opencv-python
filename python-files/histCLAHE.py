#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/Users/amourlee/Desktop/profile.png', 0)

clahe = cv2.createCLAHE(clipLimit = 2.0, tileGridSize = (8,8))

cl1 = clahe.apply(img)

plt.subplot(111), plt.imshow(img, 'gray')
plt.xticks([]),plt.yticks([])

plt.show()
