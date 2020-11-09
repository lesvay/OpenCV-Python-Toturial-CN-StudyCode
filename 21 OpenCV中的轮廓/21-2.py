import cv2
import numpy as np
img = cv2.imread('img/lunkuo.jpg',0)
ret,thresh = cv2.threshold(img,127,255,0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]

#矩
# result = cv2.moments(cnt)
#面积
# result = cv2.contourArea(cnt)
#周长
# result = cv2.arcLength(cnt,True)
# print(result)
'''
#轮廓近似
epsilon = 0.01*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)
cv2.drawContours(img, [approx], -1, (255, 255, 0), 2)
'''
'''
#凸包
hull = cv2.convexHull(cnt)
cv2.drawContours(img, [hull], -1, (255, 255, 0), 2)
'''
'''
#凸性检测
k = cv2.isContourConvex(cnt)
print(k)
'''
'''
#直边界矩形
x,y,w,h = cv2.boundingRect(cnt)
img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
'''
'''
#最小外接圆
(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
img = cv2.circle(img,center,radius,(255,255,0),2)
'''
'''
#返回旋转边界矩形内切圆
ellipse = cv2.fitEllipse(cnt)
img = cv2.ellipse(img,ellipse,(255,255,0),2)
'''

'''
#直线拟合：为白色点拟合出一条直线
rows,cols = img.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
img = cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)
'''
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindow()


