import cv2
import numpy as np
img = cv2.imread('img/star.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
sift = cv2.SIFT()
kp = sift.detect(gray,None)
# img=cv2.drawKeypoints(gray,kp)
img=cv2.drawKeypoints(gray,kp,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()