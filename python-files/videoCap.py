#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Feb 20 2017
@author amourleey
"""

import cv2
import numpy as np

# Get video from file 
# cap = cv2.VideoCapture( "/Users/amourlee/SJTU-Graduate/Programming/ComputerVision/OpenCV/learningOpenCV/NBA.mp4")

# Get video from camera
cap = cv2.VideoCapture(0)


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break;

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
