import os

import cv2

img = cv2.imread(os.path.join('.','images','bob_minion.png'))

resize_img = cv2.resize(img, (460, 359))

print(img.shape)
print(resize_img.shape)

cv2.imshow('img',img)
cv2.imshow('resize', resize_img)
cv2.waitKey(0)