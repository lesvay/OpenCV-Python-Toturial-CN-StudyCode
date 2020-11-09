import numpy as np
import cv2

img = cv2.imread('img/bird.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
'''
ValueError: not enough values to unpack (expected 3, got 2)
原因是 cv2.findContours的opencv旧版本返回3个值：
'''
#绘制独立轮廓，如第四个轮廓
#imag = cv2.drawContour(img,contours,-1,(0,255,0),3)
#但是大多数时候，下面方法更有用
imag = cv2.drawContours(img,contours,3,(0,255,0),3)

cv2.imshow('img',img)
cv2.imshow('imgray',imgray)
cv2.imshow('imag',imag)
cv2.imshow('thresh',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()