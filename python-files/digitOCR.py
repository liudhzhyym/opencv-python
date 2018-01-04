#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/Users/amourlee/Desktop/digits.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Now we splite the image to 5000 cells, each 20x20 size
cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]

# Make it into a Numpy array. It size will be (50, 100, 20, 20)
x = np.array(cells)

# Now we prepare train_data and test_data
train = x[:, :50].reshape(-1, 400).astype(np.float32) # size = (2500, 400)
test = x[:, 50:100].reshape(-1, 400).astype(np.float32) # size = (2500, 400)

# Create labels for train and test data
k = np.arange(10)
train_label = np.repeat(k, 250)[:, np.newaxis]
test_label = train_label.copy()

# Initiate KNN, train the data, then test it with test data for k = 1
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_label)
ret, result, neighbours, dist = knn.findNearest(test, k = 5)

# Now we check the accuracy of classification
# for that, compare the result with test_label and check which are wrong
matches = result == test_label
correct = np.count_nonzero(matches)
accuracy = correct * 100.0 / result.size

print accuracy
