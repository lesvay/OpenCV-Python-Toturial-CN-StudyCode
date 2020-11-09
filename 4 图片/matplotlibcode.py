import numpy as np
from cv2 import cv2
from matplotlib import pyplot as plt

img = cv2.imread('4/4-1.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()

'''
ImportError: cannot import name 'pyplot' from 'matplotlib' 
自己的名字不可以命名为matplotlib
'''