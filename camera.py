import cv2
import numpy as np

idx = 0
cap = cv2.VideoCapture(0)

w = 640
h = 480

cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = 'output.mp4'
fps = 30
out = cv2.VideoWriter(output_file, fourcc, fps, (w,h))

# 성공적으로 video device 가 열렸으면 while문 반복
while(cap.isOpened()):
    #한 프레임을 읽어옴
    ret, frame = cap.read()
    if ret is False:
        print("Can't receive frame")
        break
    
    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()