#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/Users/amourlee/Desktop/convex.png', 0)

cv2.ocl.setUseOpenCL(False)
# Initiate STAR detector
orb = cv2.ORB_create()

# find the keypoints with ORB
kp = orb.detect(img, None)

# compute the descriptors with ORB
kp, des = orb.compute(img, kp)

img2 = cv2.drawKeypoints(img, kp, None, color=(0, 0, 255), flags = 0)
plt.imshow(img2), plt.show()
