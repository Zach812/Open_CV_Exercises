import os
import numpy as np
import cv2

minion = cv2.imread(os.path.join('.', 'images','bob_minion.png'))

minion_edge = cv2.Canny(minion, 250, 300)
#makes the edge lines larger
minion_edge_d = cv2.dilate(minion_edge, np.ones((3,3), dtype=np.int8))
#makes the edge lines thinner
minion_edge_e = cv2.erode(minion_edge_d, np.ones((3,3), dtype=np.int8))

cv2.imshow('minion', minion)
cv2.imshow('minion_edge',minion_edge)
cv2.imshow('minion_edge_d',minion_edge_d)
cv2.imshow('minion_edge_e',minion_edge_e)


cv2.waitKey(0)