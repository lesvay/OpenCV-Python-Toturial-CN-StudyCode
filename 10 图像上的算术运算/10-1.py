from cv2 import cv2
import numpy as np
'''
x = np.uint8([250])
y = np.uint8([10])
print(cv2.add(x,y)) # 250+10 = 260 => 255
print(x+y) # 250+10 = 260 % 256 = 4
'''

img1=cv2.imread('img/bird1.jpg')
img2=cv2.imread('img/cat.jpg')

dst=cv2.addWeighted(img1,0.5,img2,0.5,0)
'''
Traceback (most recent call last):
  File "f:/OpenCV-Python-Toturial-CN-StudyCode/10/10-1.py", line 13, in <module>
    dst=cv2.addWeighted(img1,0.7,img2,0.3,0)
cv2.error: OpenCV(4.4.0) xxx.cpp:669: error: (-209:Sizes of input arguments do not match) The operation is neither 'array op array' (where arrays have the same size and the same number of channels), nor 'array op scalar', nor 'scalar op array' in function 'cv::arithm_op'
#必须保证两张图片shape相同
print(img1.shape)
print(img2.shape)
'''
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindow()
