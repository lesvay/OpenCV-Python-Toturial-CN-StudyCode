import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('img/shudu.jpg',0)
'''
#flatten() 将数组变成一维
hist,bins = np.histogram(img.flatten(),256,[0,256])
# 计算累积分布图
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()

# 构建 Numpy 掩模数组，cdf 为原数组，当数组元素为 0 时，掩盖（计算时被忽略）。
cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
# 对被掩盖的元素赋值，这里赋值为 0
cdf = np.ma.filled(cdf_m,0).astype('uint8')
img2 = cdf[img]

#显示均衡过后的图片
# plt.imshow(img2,cmap = 'gray')
# plt.title('Original Image')
# plt.show()

#flatten() 将数组变成一维
hist,bins = np.histogram(img2.flatten(),256,[0,256])
# 计算累积分布图
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()
'''
'''
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ))
cv2.imshow('result',res)
cv2.waitKey(0)
cv2.destroyAllWindow()
'''

# create a CLAHE object (Arguments are optional).
# 不知道为什么我没好到 createCLAHE 这个模块
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
cv2.imshow('result',cl1)
cv2.waitKey(0)
cv2.destroyAllWindow()