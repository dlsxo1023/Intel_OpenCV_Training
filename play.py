import cv2
import numpy as np

cap = cv2.VideoCapture("soccer.mp4")

idx = 0

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret is False:
        print("Can't receive frame")
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue
    
   # Resize
    resized = cv2.resize(frame, (0,0), fx = 0.5, fy = 0.5)
        
    cv2.imshow("Frame", frame)
    cv2.imshow("Frame", resized)

    key = cv2.waitKey(33)
    
    # 'q' 입력시 종료
    if key & 0xFF == ord('q'):
        break
    
    # 'c' 입력시 frame save
    if key & 0xFF == ord('c'):
        cv2.imwrite("{0:03}.jpg". format(idx), frame)
        idx += 1

cap.release()
cv2.destroyAllWindows()