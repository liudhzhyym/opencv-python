#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/Users/amourlee/Desktop/convex.png', 0)

# Initiate STAR detector
star = cv2.STAR_create("STAR")

# Initiate BRIEF extractor
brief = cv2.DescriptorExtrctor_create("BRIEF")

# Find the keypoints with STAR
kp = star.detect(img, None)

# computer the descriptors with BRIEF
kp, des = brief.compute(img, kp)

print brief.getInt('bytes')
print res.shape
