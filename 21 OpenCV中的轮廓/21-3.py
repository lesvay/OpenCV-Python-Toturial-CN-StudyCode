import cv2
import numpy as np
img = cv2.imread('img/lunkuo.jpg',0)
ret,thresh = cv2.threshold(img,127,255,0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]
'''
#长宽比
x,y,w,h = cv2.boundingRect(cnt)
aspect_ratio = float(w)/h
print(aspect_ratio)
#轮廓面积与边界矩形面积的比Extent
area = cv2.contourArea(cnt)
x,y,w,h = cv2.boundingRect(cnt)
rect_area = w*h
extent = float(area)/rect_area
print(extent)
#轮廓面积与凸包面积的比Solidity
area = cv2.contourArea(cnt)
hull = cv2.convexHull(cnt)
hull_area = cv2.contourArea(hull)
solidity = float(area)/hull_area
print(solidity)
#与轮廓面积相等的圆形的直径Equivalent Diameter
area = cv2.contourArea(cnt)
equi_diameter = np.sqrt(4*area/np.pi)
print(equi_diameter)
#方向
(x,y),(MA,ma),angle = cv2.fitEllipse(cnt)
print((x,y),(MA,ma),angle)
'''

'''
#最大值和最小值及它们的位置
mask = np.zeros(img.shape,np.uint8)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img,mask = mask)
print(min_val, max_val, min_loc, max_loc)
#平均颜色及平均灰度
mask = np.zeros(img.shape,np.uint8)
mean_val = cv2.mean(img,mask = mask)
print(mean_val)
'''
'''
mask = np.zeros(img.shape,np.uint8)
# 这里一定要使用参数-1, 绘制填充的的轮廓
cv2.drawContours(mask,[cnt],0,255,-1)
pixelpoints = np.transpose(np.nonzero(mask))
print(pixelpoints)
cv2.imshow('img',mask)
cv2.waitKey(0)
cv2.destroyAllWindow()
'''
'''
#极点:一个对象最上面，最下面，最左边，最右边的点
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
print(leftmost,rightmost,topmost,bottommost)
'''
