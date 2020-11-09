from cv2 import cv2
import numpy as np
'''
#模板
e1 = cv2.getTickCount()
# 你的代码
e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
print(time)
'''
img1 = cv2.imread('img/bird.jpg')
e1 = cv2.getTickCount()

for i in range(5,49,2):
    img1 = cv2.medianBlur(img1,i)

e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print(t)