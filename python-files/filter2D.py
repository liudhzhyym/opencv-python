#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/Users/amourlee/Desktop/test.jpg')
b, g, r = cv2.split(img)

# create rgb image
img2 = cv2.merge([r, g, b]);

# filter2D kernel
kernel = np.ones((5, 5), np.float32) / 25
dst = cv2.filter2D(img2, -1, kernel)

# Average
blur = cv2.blur(img2, (5,5))

# Gaussian 
Gaussian_blur = cv2.GaussianBlur(img2, (5, 5), 0)

# Median
Median_blur = cv2.medianBlur(img2, 5)

# bilateralFilter
bilateral_blur = cv2.bilateralFilter(img2, 9, 75, 75)

plt.subplot(2, 3, 1), plt.imshow(img2), plt.title('Original')
plt.xticks([]),plt.yticks([])

plt.subplot(2, 3, 2), plt.imshow(dst), plt.title('Average')
plt.xticks([]),plt.yticks([])

plt.subplot(2, 3, 3), plt.imshow(blur), plt.title('Blur')
plt.xticks([]),plt.yticks([])

plt.subplot(2, 3, 4), plt.imshow(Gaussian_blur), plt.title('Gaussian_blur')
plt.xticks([]),plt.yticks([])

plt.subplot(2, 3, 5), plt.imshow(Median_blur), plt.title('Median_blur')
plt.xticks([]),plt.yticks([])

plt.subplot(2, 3, 6), plt.imshow(bilateral_blur), plt.title('BilateralFilter')
plt.xticks([]),plt.yticks([])

plt.show()
