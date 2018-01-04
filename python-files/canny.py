#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../data/images/football.png', 0)

edges = cv2.Canny(img, 100, 200)

plt.subplot(1,2,1), plt.imshow(img, 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

plt.subplot(1,2,2), plt.imshow(edges, 'gray')
plt.title('Edges Image'), plt.xticks([]), plt.yticks([])

plt.show()
