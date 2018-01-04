#!/usr/bin/env python
# -*- coding:utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('data/images/profile.png', 0)

# flatten()将数组变成一维
hist, bins = np.histogram(img.flatten(), 256, [0, 256])

# 计算累积分布图
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max() / cdf.max()

plt.subplot(321),plt.imshow(img, 'gray')
plt.title('Original Image'),plt.xticks([]),plt.yticks([])

plt.subplot(322)
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(), 256, [0, 256], color = 'r')
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'), loc = 'upper left')

# 构建Numpy掩模数组，cdf为原数组，当数组为0时掩盖
cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
# 对被掩盖的元素赋值，这里赋值为0
cdf = np.ma.filled(cdf_m, 0).astype('uint8')
img2 = cdf[img]

plt.subplot(323),plt.imshow(img2, 'gray')
plt.title('Equalization Image'),plt.xticks([]),plt.yticks([])

hist, bins = np.histogram(img2.ravel(), 256, [0, 256])
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max() / cdf.max()

plt.subplot(324)
plt.plot(cdf_normalized, color = 'b')
plt.hist(img2.ravel(), 256, [0, 256], color = 'r')
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'), loc = 'upper left')

clahe = cv2.createCLAHE(clipLimit = 2.0, tileGridSize = (8,8))
cl1 = clahe.apply(img)

plt.subplot(325)
plt.imshow(cl1, cmap = 'gray'),plt.title('CLAHE Image')
plt.xticks([]),plt.yticks([])

hist, bins = np.histogram(cl1.ravel(), 256, [0, 256])
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max() / cdf.max()

plt.subplot(326)
plt.plot(cdf_normalized, color = 'b')
plt.hist(cl1.ravel(), 256, [0, 256], color = 'r')
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'), loc = 'upper left')

plt.show()


