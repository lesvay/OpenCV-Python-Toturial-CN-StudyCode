from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
BLUE=[255,0,0]
img1=cv2.imread('img/bird.jpg')

replicate  = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
reflect    = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap       = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
constant   = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

#subplot(231)2行3列第1个
plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')#复制
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')#映射
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')#包裹
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')#连续
plt.show()
