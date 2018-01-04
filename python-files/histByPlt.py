#/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('data/images/histogram.png')

plt.hist(img.ravel(), 256, [0, 256])

plt.show()
