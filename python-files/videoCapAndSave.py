#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Feb 20 2017

@amourleey
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('/Users/amourlee/Desktop/output.mp4', fourcc, 20.0, (640, 480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('frame', frame)

        # write the flipped frame
        frame = cv2.flip(frame, 0)
        out.write( frame )


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
