#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

# Read image
img = cv2.imread('../data/images/red-eye.png', cv2.IMREAD_COLOR)

# Output image
imgOut = img.copy()

# Load Haar cascade
eyesCascade = cv2.CascadeClassifier("../data/haarcascades/haarcascade_eye.xml")

# Detect eyes
eyes = eyesCascade.detectMultiScale(img, scaleFactor = 1.3, minNeighbors = 4, minSize=(100, 100))

for (x, y, w, h) in eyes:
    # extract eye from the image.
    eye = img[y:y+h, x:x+w]
    imgOut = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Slipt eye image into 3 channels
    b = eye[:, :, 0]
    g = eye[:, :, 1]
    r = eye[:, :, 2]

    # Add the green and blue channels.
    bg = cv2.add(b, g)

    # Simple red eye detector
    mask = (r > 150) & (r > bg)

    # Convert the mask to uint8 format
    mask = mask.astype(np.uint8) * 255
    

    def fillHoles(mask):
        maskFloodfill = mask.copy()
        h, w = maskFloodfill.shape[:2]
        maskTemp = np.zeros((h+2, w+2), np.uint8)
        cv2.floodFill(maskFloodfill, maskTemp, (0, 0), 255)
        mask2 = cv2.bitwise_not(maskFloodfill)
        return mask2 | mask

    # Clean up mask by filling holes and dilating
    mask = fillHoles(mask)
    mask = cv2.dilate(mask, None, anchor = (-1, -1), iterations = 3, borderType = 1, borderValue = 1)

    mean = bg / 2
    mask = mask.astype(np.bool)[:,:, np.newaxis]
    mean = mean[:,:,np.newaxis]

    # Copy the eye from the original image.
    eyeOut = eye.copy()

    # Copy the mean image to the output image.
    np.copyto(eyeOut, mean, where = mask)
    cv2.imshow('ss', eyeOut)

    # Copy the fixed eye to the output image
    imgOut[y:y+h, x:x+w] = eyeOut

cv2.imshow('image',imgOut)
cv2.waitKey(0)
cv2.destroyAllWindows()
