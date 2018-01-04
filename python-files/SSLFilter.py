#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('data/images/dave.png', 0)

# cv2.CV_64F 输出图像的深度（数据类型），可以使用-1, 与原图像保持一致np.uint8
laplacian = cv2.Laplacian(img, cv2.CV_64F)

# 参数1，0为只在x方向求一阶导数，最大可以求2阶导数。
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize = 5)

# 参数1，0为只在y方向求一阶导数，最大可以求2阶导数。
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize = 5)

images = [ img, laplacian, sobelx, sobely]
titles = [ 'Original', 'Laplacian', 'Sobel X', 'Sobel Y']

for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i]), plt.xticks([]), plt.yticks([])

plt.show()
