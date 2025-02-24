import os

import cv2

img = cv2.imread(os.path.join('.', 'images', 'whiteboard.png'))

print(img.shape)
# (x,y) are swiched for shape

# line
cv2.line(img, (100, 150), (200, 220), (0,255, 0), 3)

# rectangle
# last number is thickness, -1 means fill
cv2.rectangle(img, (10, 250), (100,100), (0, 0 , 255), -1)

#circle
cv2.circle(img, (168, 56), 52, (255, 0,0), 10 )

# text
cv2.putText(img, 'Hello!', (28,112), cv2.FONT_HERSHEY_SIMPLEX, 1,(255, 255, 0), 4)

cv2.imshow('whiteboard', img)
cv2.waitKey(0)