# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 21:18:51 2018

@author: byy
"""

import cv2

imglst = []

camera = cv2.VideoCapture(1)
while True:    
    state,frame = camera.read()
    cv2.imshow('mycamera',frame)
    key = cv2.waitKey(1000)
    imglst.append(frame)

    if key == 27:               #if input == esc
        break
    if len(imglst)>10:
        for i in range(11):
            cv2.imwrite('test'+str(i)+'.jpg',imglst[i])
            i+=1

                    
camera.release()
cv2.destroyAllWindows()