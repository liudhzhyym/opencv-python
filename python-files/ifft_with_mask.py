#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('data/images/football.png', 0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

magnitude_spectrum = 20 * np.log(np.abs(fshift))

f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back_no_mask = np.abs(img_back)

# use 60*60 mask to decline lower frequency
rows, cols = img.shape
crow, ccol = rows/2, cols/2
fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
magnitude_spectrum_mask = 20 * np.log(np.abs(fshift))
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back_mask = np.abs(img_back)



plt.subplot(321), plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(323), plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]),plt.yticks([])
plt.subplot(324), plt.imshow(img_back_no_mask, cmap = 'gray')
plt.title('Image Back'), plt.xticks([]),plt.yticks([])
plt.subplot(325), plt.imshow(magnitude_spectrum_mask, cmap = 'gray')
plt.title('Magnitude Spectrum with Mask'), plt.xticks([]), plt.yticks([])
plt.subplot(326), plt.imshow(img_back_mask, cmap = 'gray')
plt.title('Image Back With Mask'), plt.xticks([]),plt.yticks([])
plt.show()
