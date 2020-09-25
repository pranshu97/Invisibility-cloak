import cv2 
import numpy as np 
import time   

capture_video = cv2.VideoCapture(0) 

width = int(capture_video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(capture_video.get(cv2.CAP_PROP_FPS))
codec = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('out.mp4', codec, fps, (width, height))

time.sleep(1)
background = None
  

for i in range(60): 
    return_val, background = capture_video.read() 
    if return_val == False : 
        continue 
  
while (capture_video.isOpened()): 
    return_val, img = capture_video.read() 
    if not return_val : 
        break 

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  
  
    lower_white = np.array([0,0,130])
    upper_white = np.array([120,120,255])
    mask = cv2.inRange(hsv, lower_white, upper_white) 
    mask1 = mask 
  
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations = 2) 
    mask1 = cv2.dilate(mask1, np.ones((3, 3), np.uint8), iterations = 1) 
    mask = cv2.bitwise_not(mask1) 

    res1 = cv2.bitwise_and(background, background, mask = mask1) 
    res2 = cv2.bitwise_and(img, img, mask = mask) 
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0) 
  
    cv2.imshow("INVISIBLE MAN", final_output) 
    out.write(final_output)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break