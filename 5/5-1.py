import numpy as np
from cv2 import cv2

cap = cv2.VideoCapture(0)
'''
print(cap.isOpened())
如果false 考虑一下是不是电脑禁用相机了，在设置->隐私那里可以修改
'''

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):#输入q结束
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()