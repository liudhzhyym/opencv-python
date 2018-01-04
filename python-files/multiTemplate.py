#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

def find_img(background,target,threshold=0.85,method='cv2.TM_CCOEFF_NORMED'):
    '''
        background:背景图
        target：想要在背景图中找出的图片

        method：如果cv2.TM_CCOEFF_NORMED效果不好可以尝试：
                ['cv2.TM_CCOEFF','cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED',
                    'cv2.TM_SQDIFF','cv2.TM_SQDIFF_NORMED'] 
    '''
    #backIMG = ''
    method = eval('%s'%method)
    arr = background.split(".")
    resultFile = "%s_result.%s" % (arr[0] , arr[1])
    img_rgb = cv2.imread(background)
    background = cv2.imread(background,0)
    target = cv2.imread(target,0)
    result = cv2.matchTemplate(background,target,method)
    w, h = target.shape[::-1]

    #匹配度loc
    loc = cv2.minMaxLoc(result)[1]
    if loc > threshold and loc <=1:
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = cv2.minMaxLoc(result)[2]
        else:
            top_left = cv2.minMaxLoc(result)[3]

        bottom_right = (int(top_left[0] + w) , int(top_left[1] + h) )

        #可以查看找到的结果
        #cv2.rectangle(background, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)
        cv2.rectangle(img_rgb,top_left, bottom_right,(0, 0, 255), 1)
        cv2.imwrite(resultFile,img_rgb)
        # cv2.imshow('RES', img_rgb)
        # cv2.waitKey(0)

        x1,y1 = top_left
        x2,y2 = bottom_right
        centre_x = (x1+x2)/2
        centre_y = (y1+y2)/2
        return (centre_x,centre_y)
    return (None,None)
x , y = find_img('data/mari1.png' , 'data/mari2.png')
print x , y
x , y = find_img('data/images/mario.png' , 'data/images/mario_coin.png')
print x , y
x , y = find_img('data/sg1.png' , 'data/sg4.png')
print x , y
# img_rgb = cv2.imread('data/images/mario.png')
# img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
# template = cv2.imread('data/images/mario_coin.png', 0)

# w, h = template.shape[::-1]

# res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
# start = max_loc[0]+w/2, max_loc[1]+h/2
# print("start:", start)

# thresh = 0.9

# loc = np.where( res >= thresh)
# for pt in zip(*loc[::-1]):
#     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)

# cv2.imshow('RES', img_rgb)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
