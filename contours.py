import os

import cv2

img = cv2.imread(os.path.join('.', 'images', 'bob_minion.png'))


img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 254, 250, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cont in contours:
    # Isolating each white image within thresh
    if cv2.contourArea(cont) > 200:
        # Removing noise
        # Can see dots around the img (green little dots)
        # cv2.drawContours(img,cont, -1, (0,255, 0), 1)
        x1, y1, w, h = cv2.boundingRect(cont)
        # Building Object Detector
        cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)
cv2.imshow('img', img)
cv2.imshow('thresh', thresh)
cv2.waitKey(2000)