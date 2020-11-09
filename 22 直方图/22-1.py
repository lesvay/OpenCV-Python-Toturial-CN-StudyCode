import numpy as np
import cv2
'''
# img = cv2.imread('img/bird.jpg',0)
# 别忘了中括号 [img],[0],None,[256],[0,256]，只有 mask 没有中括号
# hist = cv2.calcHist([img],[0],None,[256],[0,256])

#img.ravel() 将图像转成一维数组，这里没有中括号。
# hist,bins = np.histogram(img.ravel(),256,[0,256])
# print(hist)
'''
from matplotlib import pyplot as plt
'''
# 绘制直方图
plt.hist(img.ravel(),256,[0,256]);
plt.show()
'''
'''
#绘制多通道直方图
color = ('b','g','r')
# 对一个列表或数组既要遍历索引又要遍历元素时
# 使用内置 enumerrate 函数会有更加直接，优美的做法
#enumerate 会将数组或列表组成一个索引序列。
# 使我们再获取索引和索引内容的时候更加方便
img = cv2.imread('img/bird.jpg')
#注意：如果需要显示彩色直方图，imread不能加0
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()
'''
img = cv2.imread('img/bird.jpg',0)
# create a mask
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:300, 100:400] = 255
masked_img = cv2.bitwise_and(img,img,mask = mask)
# Calculate histogram with mask and without mask
# Check third argument for mask
hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])
plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask,'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0,256])
plt.show()
