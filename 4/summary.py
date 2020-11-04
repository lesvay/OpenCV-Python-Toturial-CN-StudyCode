import numpy as np
from cv2 import cv2

img = cv2.imread('4/4-1.jpg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27: # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('4/4-1-save.png',img)
    cv2.destroyAllWindows()