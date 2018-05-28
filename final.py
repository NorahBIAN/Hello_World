# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 12:12:19 2018

@author: byy
"""

import cv2
import numpy

source = cv2.imread('LENNA.bmp')
source = cv2.resize(source,(350,200))

positions = []
for j in range(0,201,50):
    for i in range(0,351,50):
        position = [i,j]
        positions.append(position)
print(positions)
        
sourceCorner = numpy.array(positions)

cv2.namedWindow('mycamera')
camera = cv2.VideoCapture(0)
while True:    
    state,frame = camera.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #,cv2.CALIB_CB_FAST_CHECK
    found,corners = cv2.findChessboardCorners(gray,(8,5),cv2.CALIB_CB_FAST_CHECK)
    if found:

        goalCorner = numpy.array(corners)
        M,mask = cv2.findHomography(sourceCorner,goalCorner)    #M is like a transformation matrix
        for pp in goalCorner:
            frame = cv2.warpPerspective(source, M, (frame.shape[1],frame.shape[0]),frame,borderMode=cv2.BORDER_TRANSPARENT)
    cv2.imshow('mycamera',frame)
    cv2.imshow('LENNA',source)
    
    key = cv2.waitKey(15)       
    if key == 27:               #if input == esc
        break                                
camera.release()
cv2.destroyAllWindows()