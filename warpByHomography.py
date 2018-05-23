# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 21:39:03 2018

@author: byy
"""

import cv2
import numpy

#源图像的四点坐标
sourceCorner = numpy.array([[0,0],[200,0],[0,200],[200,200]])       #image of 200*200
#目标粘贴处的坐标
goalCorner = numpy.array([[100,100],[200,100],[100,200],[200,200]])  #？？？this can be changed as you want
#calculate the homography
#2 return values, the result and mask. mask???
M,mask = cv2.findHomography(sourceCorner,goalCorner)

source = cv2.imread('LENNA.bmp')
#change the size of the source image for the size200*200. This is related to the size of the image
source = cv2.resize(source,(200,200))
# generate the background image  totally black
back = numpy.ones((300,400,3),dtype=numpy.uint8)

for p in goalCorner:
    #draw circles on the 4 corners of the goal image
    cv2.circle(back,tuple(p),5,(255,255,0))
#in order to keep the back, make a copy
warped = back.copy() 
warped = cv2.warpPerspective(source, M, (warped.shape[1],warped.shape[0]), warped,borderMode=cv2.BORDER_TRANSPARENT)

cv2.imwrite('warped.png',warped)
cv2.imshow('source',source)
cv2.imshow('back',back)
cv2.imshow('warped',warped)

cv2.waitKey(0)
cv2.destroyAllWindows()