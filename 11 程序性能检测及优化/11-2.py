from cv2 import cv2
import numpy as np
# check if optimization is enabled
img = cv2.imread('img/bird.jpg')
print(cv2.useOptimized())
res = cv2.medianBlur(img,49)
print(res)
cv2.setUseOptimized(False)
print(cv2.useOptimized())
res = cv2.medianBlur(img,49)
print(res)
'''
命令行
%timeit 语句
检测语句效率
'''