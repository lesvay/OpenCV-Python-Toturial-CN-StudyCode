import numpy as np
from cv2 import cv2

# Create a black image
img=np.zeros((512,512,3), np.uint8)

'''
画线
'''
# Draw a diagonal blue line with thickness of 5 px
# 图片 起点 终点 颜色RGB 粗细
cv2.line(img,(0,0),(511,511),(255,255,0),1)
'''
画矩形
'''
cv2.rectangle(img,(0,0),(510,128),(0,255,0),2)
'''
画圆
'''
# 圆心 半径 颜色 -1表实心
cv2.circle(img,(447,63), 63, (0,0,255), -1)
'''
画椭圆
'''
# （中心点）（水平轴 垂直轴），角度，画出的起始度数，结束度数，颜色，粗细
cv2.ellipse(img,(256,256),(100,50),0,10,360,(0,255,0),-1)
'''
画多边形
'''
pts=np.array([[400,5],[200,300],[150,20],[500,100]], np.int32)
pts=pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(255,125,0))
# 这里 reshape 的第一个参数为-1, 表明这一维的长度是根据后面的维度的计算出来的。
'''
添加文字
'''
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'LESVAY',(10,500), font, 4,(255,255,255),2)

'''
显示结果
'''
cv2.namedWindow('image')
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()