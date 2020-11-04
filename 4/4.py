import numpy as np
from cv2 import cv2
'''
读入图像

关于直接使用书上代码出现Module 'cv2' has no 'imread' member的错误.
其实代码是没有错误的,可以直接运行的,就是vscode的插件检测不到模块而已, 主要原因是cv2模块下还有cv2模块
引用时改成from cv2 import cv2就不会出现红色波浪
'''
img = cv2.imread('4-1.jpg',0)

'''
显示图像
'''
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''
保存图像
'''
cv2.imwrite('4-1-save.png',img)


'''
总结
'''
img = cv2.imread('4-1.jpg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27: # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('4-1-save.png',img)
    cv2.destroyAllWindows()