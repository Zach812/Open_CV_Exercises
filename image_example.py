import os

import cv2

#reading image
image_path = os.path.join(".", "images", "bob_minion.png")

img = cv2.imread(image_path)

#Writing the image
cv2.imwrite(os.path.join(".", "images", "bob_out.png"), img)

#visualizing the image

cv2.imshow("image", img)
cv2.waitKey(0)