#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('/Users/amourlee/Desktop/head.png', 0)
img2 = cv2.imread('/Users/amourlee/Desktop/meixi.png', 0)

cv2.ocl.setUseOpenCL(False)

# initiate the ORB detector
orb = cv2.ORB_create()

# find the keypoints and descriptors with ORB.
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# create BFMatcher object.
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

# Match descriptors.
matches = bf.match(des1, des2)

# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)

img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:100], None, flags = 2)

plt.imshow(img3), plt.show()
