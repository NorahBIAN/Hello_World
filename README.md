# B3 Training demos


This is my first practice with python under the instruction of lab's senior.
It is a project of B3 training for making some kind of thing like AR application.
Not finished although.

### CIRCUMSTANCE
  WINDOWS 10 64bits, Python 3.6, OpenCV 3

### CONTENTS1

## 1.setCamera.py
  
  It is about how to open camera with OpenCV. A start.

## 2.generateChessBoard.py

  It is about how to generate a image of chessboard.
  
## 3.detectCrossPoints.py

  It imports <generateChessBoard.py>.
  It is about how to detect the cross points of a image of chessboard with a function of
  OpenCV called cv2.findChessboardCorners.

## 4.drawCircles.py

  It is about detecting the cross points of chessboard in the camera view.
  
## 5.warpByHomograpy.py

  It is about warpping a certain image to a specified postion on a black background
  (Of course the back can be anything, just give the coordination and will be fine)
  
## 6.final.py

  This is the final about the 2D warping a random pic onto a chessboard.
  (It has been sometime since my work, so there may be some mistakes in this file.)

### CONTENTS2

## 1.chessboardpic.py

  In this part we generate a cube or axis on chessboard.
  This file is meant for capturing pics of chessboard in real world and saving.
  
## 2.3dcalibration.py

  In this file we can generate a cube on the chessboard, with the parameters from the camera,
  and parameters of relationship between 3d and 2d.
  More information referring to
  https://docs.opencv.org/3.4/d9/db7/tutorial_py_table_of_contents_calib3d.html
