# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 12:58:06 2018

@author: byy

"""
#detect chessboards and fraw circles
import cv2
import numpy


camera = cv2.VideoCapture(0)

while True:    
    state,frame = camera.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    found,corners = cv2.findChessboardCorners(gray,(8,5),cv2.CALIB_CB_FAST_CHECK)
    
    if found:
        for point in corners:
            p = tuple(point[0])     #make a list of positions
#python draw circle function(original img,position,radius，color)
            cv2.circle(frame, p, 5, (0,255,100))
    
    cv2.imshow('mycamera',frame)
    key = cv2.waitKey(15)       #if no input in 30ms,show the next frame. if here is 0, one frame only
    if key == 27:               #if input == esc
        break
            
camera.release()
cv2.destroyAllWindows()

