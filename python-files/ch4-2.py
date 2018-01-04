#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Feb 20 2017

@author amourleey
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('/Users/amourlee/Desktop/main_building.png', 0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')

# to hide tick values on X and Y axis
plt.xticks([]), plt.yticks([])
plt.show()
