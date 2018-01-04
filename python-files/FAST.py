#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/Users/amourlee/Desktop/convex.png', 0)

# Initiate FAST object with default values
# fast = cv2.FastFeatureDetector()
fast = cv2.FastFeatureDetector_create()

# find and draw the keys
kp = fast.detect(img, None)
img2 = cv2.drawKeypoints(img, kp, None, color=(255,0,0))

#print all default params
# print('Threshold: %s') % fast.getInt('threshold')
print('Threshold: %s') % fast.getThreshold()
# print('nonmaxSuppression: %s') % fast.getBool('nonmaxSuppression')
print('nonmaxSuppression: %s') % fast.getNonmaxSuppression()
# print('heighborhood: %s') % fast.getInt('type')
print('heighborhood: %s') % fast.getType()
print('Total key points with nonmaxSuppression: %s') % len(kp)

# disable nonmaxSuppression
fast.setNonmaxSuppression(0)
kp = fast.detect(img, None)

print('Total key points without nonmaxSuppression: %s') % len(kp)

img3 = cv2.drawKeypoints(img, kp, None, color = (0, 255, 0))

plt.subplot(221),plt.imshow(img, 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(img2, 'gray')
plt.title('Image with nonmaxSuppression'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(img3, 'gray')
plt.title('Image without nonmaxSuppression'), plt.xticks([]), plt.yticks([])


plt.show()
