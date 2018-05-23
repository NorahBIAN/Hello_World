# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 21:22:27 2018

@author: byy
"""

import numpy
import cv2

def generate_chessboard(domainWidth,domainHeight,cols,rows):
    # numpy.ones are arrays for 1. Here every pixel is 255 (white)
    # if not announced, the created matrix are float numbers.Here is unsigned int numbers)
    # three dimention martix,RGB matrix
    board = numpy.ones((domainHeight*rows,domainWidth*cols,3),dtype=numpy.uint8)*255
    for j in range(rows):           #(i,j)
        for i in range(cols):
            if (i + j)%2 == 0:
                continue
            leftTop = (i*domainWidth,j*domainHeight)
            rightBottom = ((i + 1) * domainWidth,(j + 1) * domainHeight)
            cv2.rectangle(board,leftTop,rightBottom,0,-1)       #rectangle函数，指定左上右下坐标
    return board


def chessBoardInScene():
    #generate a background.(but it is also ok to not generate this?)
    back = numpy.zeros((400,600,3),dtype=numpy.uint8)
    back[:,:,0] = numpy.ones((400,600))*205    #order is B,G,R, generate beautiful blue backgroud
    back[:,:,1] = numpy.ones((400,600))*120
    #create the chessboard
    cboard = generate_chessboard(50,50,8,6)
    #create image translation matrix. M([1,0,x],[0,1,y]) 1 means in x direction or y direction and x,y for move distance
    x, y = 100,50
    M = numpy.float32([[1,0,x],[0,1,y]])
    #cv2.warpAffine(original image,translation matrix,dsize--the size of the output img, output image desized,borderMode)
    #back.shape[0] read the 1D length of back. back.shape[1] read the 2D length of back
    #actually this is in case for automatic resize
    #borderMode pixel extrapolation method像素外插法
    #BORDER_TRANSPARENT means the pixels in the destination image corresponding 
    #to the “outliers” in the source image are not modified by the function
    back = cv2.warpAffine(cboard,M,(back.shape[1],back.shape[0]),
                          back,borderMode = cv2.BORDER_TRANSPARENT)
    return back

image = chessBoardInScene()
cv2.imshow('chessboard',image)
k = cv2.waitKey(0)

