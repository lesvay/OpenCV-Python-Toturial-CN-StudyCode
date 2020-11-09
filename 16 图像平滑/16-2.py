from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('img/bird.jpg')
#卷积核
# blur = cv2.blur(img,(5,5))
#高斯核，是指根据窗口大小（5,5）来计算高斯函数标准差
# blur = cv2.GaussianBlur(img,(5,5),0)
#中值模糊
# blur = cv2.medianBlur(img,5)
#双边滤波
blur = cv2.bilateralFilter(img,9,75,75)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('result')
plt.xticks([]), plt.yticks([])
plt.show()
