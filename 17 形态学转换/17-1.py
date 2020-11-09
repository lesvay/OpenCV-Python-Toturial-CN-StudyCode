from cv2 import cv2
import numpy as np
img = cv2.imread('img/j.jpg',0)
#正常形状
# kernel = np.ones((5,5),np.uint8)
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
#一个椭圆形的kernel
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
#十字形
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
#腐蚀
# result = cv2.erode(img,kernel,iterations = 1)
#膨胀
# result = cv2.dilate(img,kernel,iterations = 1)
#开运算：先腐蚀后膨胀
# result = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
#闭运算：先膨胀后腐蚀
# result = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
#形态学梯度：膨胀减腐蚀
# result = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
#礼帽：原始图像减开运算
# result = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
#黑帽：闭运算减原始图像
result = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow('img',img)
cv2.imshow('erosion',result)
cv2.waitKey(0)
cv2.destroyAllWindow()