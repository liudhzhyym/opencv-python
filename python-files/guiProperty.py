#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Feb 19 2017

@author: amourleey
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load a color image in grayscale
img = cv2.imread('data/images/meixi.png', 1)
cv2.namedWindow('Image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('Image', img)
k = cv2.waitKey(0)

# Wait for ECS key to exit
if k == 27:
    cv2.destroyWindow('image')

# Wait for 's' key to save and exit
elif k == ord('s'):
    cv2.imwrite('/Users/amourlee/Desktop/gray.png', img)
    cv2.destroyAllWindows()

# Display image by plt
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]),plt.yticks([]) # To hide tick values on X and y axis
plt.show()

