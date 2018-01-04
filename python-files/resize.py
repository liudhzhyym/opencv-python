#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

img = cv2.imread('/Users/amourlee/Desktop/test.jpg')

# res=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)

height,width=img.shape[:2]
res_2 = cv2.resize(img, (2 * width, 2 * height), interpolation = cv2.INTER_CUBIC)

while(1):
    cv2.imshow( 'img', img )
    # cv2.imshow( 'res', res )
    cv2.imshow( 'res_2', res_2)

    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
