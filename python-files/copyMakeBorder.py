#! /usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

BLUE = [255, 0, 0]

img1 = cv2.imread('data/images/opencv.png')
b, g, r = cv2.split(img1)
img2 = cv2.merge([r, g, b])

replicate = cv2.copyMakeBorder(img2, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img2, 10, 10, 10, 10, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img2, 10, 10, 10, 10, cv2.BORDER_REFLECT101)
wrap = cv2.copyMakeBorder(img2, 10, 10, 10, 10, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img2, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value = BLUE)

plt.subplot(231),plt.imshow(img2, 'gray'), plt.title('Original')
plt.subplot(232),plt.imshow(replicate,'gray'), plt.title('Replicate')
plt.subplot(233),plt.imshow(reflect,'gray'), plt.title('Reflect')
plt.subplot(234),plt.imshow(reflect101,'gray'), plt.title('Reflect101')
plt.subplot(235),plt.imshow(wrap,'gray'), plt.title('Wrap')
plt.subplot(236),plt.imshow(constant, 'gray'), plt.title('Constant')

plt.show()

cv2.destroyAllWindows()

