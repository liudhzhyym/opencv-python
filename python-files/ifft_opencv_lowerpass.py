#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('data/images/football.png', 0)

# dft
dft = cv2.dft(np.float32(img), flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

# idft no mask
n_shift = np.fft.ifftshift(dft_shift)
image = cv2.idft(n_shift)
image = cv2.magnitude(image[:,:,0], image[:,:,1])
# end

# idft with mask
rows, cols = img.shape
crow, ccol = rows/2, cols/2
# create a mask first, center square is 1, remaining all zeros
mask = np.zeros((rows, cols, 2), np.uint8)
mask[ crow-30:crow+30, ccol-30:ccol+30 ] = 1

# apply mask and inverse DFT
fshift = dft_shift * mask
f_shift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_shift)
img_back = cv2.magnitude(img_back[:,:,0], img_back[:,:,1])


plt.subplot(221), plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]),plt.yticks([])
plt.subplot(223), plt.imshow(img_back, cmap = 'gray')
plt.title('Image Back'), plt.xticks([]),plt.yticks([])
plt.subplot(224), plt.imshow(image, cmap = 'gray')
plt.title('Image No Maks'), plt.xticks([]),plt.yticks([])

plt.show()
