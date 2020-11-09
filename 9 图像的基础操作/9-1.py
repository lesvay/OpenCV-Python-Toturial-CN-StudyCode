from cv2 import cv2
import numpy as np
img=cv2.imread('img/bird.jpg')
'''
#获取灰度值和修改灰度值
print(img)#输出该图像的灰度值
px=img[100,100]
print(px)#输出100行100列像素的rgb
img[100,100]=[0,0,0]#改变第100行100列像素的rgb
blue=img[100,100,0]
print(blue)#img[100,100]第0位，即rgb中的r
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
print(img.shape)#形状
print(img.size)#像素数目
print(img.dtype)#数据类型
'''
'''
#ROI
copy=img[280:340,330:390]
img[273:333,100:160]=copy
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
拆分rgb通道
b,g,r=cv2.split(img)

#类似
# b=img[:,:,0]
# g=img[:,:,1]
# r=img[:,:,2]

# cv2.imshow('image',g)
# cv2.imshow('image',b)
cv2.imshow('image',r)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
#去除通道
#openCV按照BGR排序，matplotlib按照RGB排序
img[:,:,0]=0 #去除b蓝色通道
img[:,:,1]=0 #去除g绿色通道
img[:,:,2]=0 #去除r红色通道
img[:,:,:]=0 #去除全部通道，即变成了黑色
'''
'''
#通道合并
b,g,r=cv2.split(img)
img=cv2.merge([b,g,r])#加上[]
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''