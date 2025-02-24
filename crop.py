import os

import cv2

img = cv2.imread(os.path.join('.', 'images', 'bob_minion.png'))

print(img.shape)
# [height, width]
cropped_img = img[50:300, 50:290]

print(cropped_img.shape)
cv2.imshow("img", img)
cv2.imshow('cropped_img', cropped_img)
cv2.waitKey(0)