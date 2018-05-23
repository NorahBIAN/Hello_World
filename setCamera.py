# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 21:18:51 2018

@author: byy
"""

import cv2

camera = cv2.VideoCapture(0)

cv2.namedWindow('mycamera')

while True:    
    state,frame = camera.read()
    cv2.imshow('mycamera',frame)
    key = cv2.waitKey(30)       #if no input in 30ms,show the next frame. if here is 0, one frame only
    if key == 27:               #if input == esc
        break
    
camera.release()
cv2.destroyAllWindows()