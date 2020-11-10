import cv2
import numpy as np
img = cv2.imread('img/star.jpg',0)
# Create SURF object. You can specify params here or later.
# Here I set Hessian Threshold to 400
surf = cv2.SURF(400)
# Find keypoints and descriptors directly
kp, des = surf.detectAndCompute(img,None)
print(len(kp))
print(surf.hessianThreshold)
# We set it to some 50000. Remember, it is just for representing in picture.
# In actual cases, it is better to have a value 300-500
surf.hessianThreshold = 50000
# Again compute keypoints and check its number.
kp, des = surf.detectAndCompute(img,None)
print(len(kp))

img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)
plt.imshow(img2),plt.show()

# Check upright flag, if it False, set it to True
print(surf.upright)
surf.upright = True
# Recompute the feature points and draw it
kp = surf.detect(img,None)
img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)
plt.imshow(img2),plt.show()

print(surf.descriptorSize())

# That means flag, "extended" is False.
print(surf.extended)
# So we make it to True to get 128-dim descriptors.
surf.extended = True
kp, des = surf.detectAndCompute(img,None)
print(surf.descriptorSize())
print(des.shape)