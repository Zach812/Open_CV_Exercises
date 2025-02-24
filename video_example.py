import os

import cv2

# importing the video
video_path = os.path.join(".", "images", "3644945-hd_1920_1080_25fps.mp4")

video = cv2.VideoCapture(video_path)

#visualizing the video
ret = True
while ret:
    ret, frame = video.read()
    
    if ret:
        cv2.imshow('frame', frame)
        cv2.waitKey(40)
        
video.release()
cv2.destroyAllWindows()    
