# -*- coding: utf-8 -*-
"""
Created on Sat May  5 15:55:04 2018

@author: byy
"""

import numpy as np
import cv2
import glob

# termination criteria
# 设置寻找亚像素角点的参数，采用的停止准则是最大循环次数30和最大误差容限0.001
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
# 获取标定板角点的位置
objp = np.zeros((8*5,3), np.float32)
 # 将世界坐标系建在标定板上，所有点的Z坐标全部为0，所以只需要赋值x和y  
objp[:,:2] = np.mgrid[0:8,0:5].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = glob.glob('test*.jpg')
#to get the calibration of 2D to 3D
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (8,5),None)

    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners)

        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, (8,5), corners,ret)
#        cv2.imshow('img',img)
        cv2.waitKey(1)

        cv2.destroyAllWindows()


    ret, camMat, dist, rotVects, transVects = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
print('successfully calibrate')

def drawAxis(img, corners, imgpts):
    corner = tuple(corners[0].ravel())
    img = cv2.line(img, corner, tuple(imgpts[0].ravel()), (255,0,0), 5)
    img = cv2.line(img, corner, tuple(imgpts[1].ravel()), (0,255,0), 5)
    img = cv2.line(img, corner, tuple(imgpts[2].ravel()), (0,0,255), 5)
    return img

def drawCube(img, corners, imgpts):
    imgpts = np.int32(imgpts).reshape(-1,2)
    # draw ground floor in green
    img = cv2.drawContours(img, [imgpts[:4]],-1,(0,255,0),-3)

    # draw pillars in blue color
    for i,j in zip(range(4),range(4,8)):
        img = cv2.line(img, tuple(imgpts[i]), tuple(imgpts[j]),(255),3)

    # draw top layer in red color
    img = cv2.drawContours(img, [imgpts[4:]],-1,(0,0,255),3)
    return img

axis = np.float32([[0,0,0], [0,3,0], [3,3,0], [3,0,0],
                   [0,0,-3],[0,3,-3],[3,3,-3],[3,0,-3] ]) 
    
print('draw defined')
    

camera = cv2.VideoCapture(1)

while True:    
    state,frame = camera.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret,corners = cv2.findChessboardCorners(gray,(8,5),cv2.CALIB_CB_FAST_CHECK)
    if ret == True:
        _, rotVects, transVects, inliers = cv2.solvePnPRansac(objp, corners, camMat, dist)
#        # project 3D points to image plane
        imgpts, jac = cv2.projectPoints(axis, rotVects, transVects, camMat, dist)
    
        frame = drawCube(frame,corners,imgpts) 
    cv2.imshow('img',frame)
    key = cv2.waitKey(1)
    if key == 27:               #if input == esc
        break
camera.release()
cv2.destroyAllWindows()



