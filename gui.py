import cv2
import numpy as np


cap = cv2.VideoCapture(0)

topLeft = (50, 50)
bottomRight = (300, 300)

point = (200, 200)
radius = 50

def click(event, x, y, flags, param):
    global point, pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Pressed", x, y)
        point = (x, y)

cv2.namedWindow("Camera")
cv2.setMouseCallback("Camera", click)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret is False:
        print("Can't receive")
        break
    #Line
    cv2.line(frame, topLeft, bottomRight, (0, 255, 0), 5)

    #Rectangle
    cv2.rectangle(frame,
                  [pt+30 for pt in topLeft],
                  [pt-30 for pt in bottomRight],
                  (0, 0, 255), 5
                  )
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, 'me',
                [pt+80 for pt in topLeft],
                font, 2, (0, 255, 255), 10
                )
    
    #Circle
    cv2.circle(frame, point, radius, (255, 0, 255), 3)

    #Display
    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()