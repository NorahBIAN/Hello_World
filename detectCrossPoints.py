# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 21:31:56 2018

@author: byy
"""


import numpy
import cv2
import generateChessboard


back =  generateChessboard.chessBoardInScene()

cv2.imwrite('chessBoardInScene.png',back)
chessboard = cv2.imread('chessBoardInScene.png')
#In order to detect the cross points, need to turn to grayscale img
gray = cv2.cvtColor(chessboard,cv2.COLOR_BGR2GRAY) 
#findChessboardCorners used for inner corners position
#input img must be 8bit grayscale or colour img      
found,corners = cv2.findChessboardCorners(gray,(7,5))   #2 return values. flag of whether found and positions
#Chessboard
#cv2.imshow('chessboard',chessboard)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
if found:
    for point in corners:
        #p.append(point)   why here is tuple object?
        p = tuple(point[0])     #make a list of positions
        #python draw circle function(original img,position,radius，color)
        cv2.circle(chessboard, p, 5, (0,255,100))
#Chessboard with cross points
cv2.imshow('chessboard',chessboard)
cv2.waitKey(0)
cv2.destroyAllWindows()

