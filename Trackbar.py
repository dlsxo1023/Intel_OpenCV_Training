import cv2
import numpy as np

cap = cv2.VideoCapture(0)

topLeft = (0, 300)
bold = 0
fontsize = 0
R, G, B = 0, 0, 0

def on_bold_trackbar(value):
    global bold
    bold = value
def on_fontsize_trackbar(value):
    global fontsize
    fontsize = value
def on_R_trackbar(value):
    global R
    R = value
def on_G_trackbar(value):
    global G
    G = value
def on_B_trackbar(value):
    global B
    B = value

cv2.namedWindow("Camera")
cv2.createTrackbar("bold", "Camera", bold, 10, on_bold_trackbar)
cv2.createTrackbar("size", "Camera", fontsize, 10, on_fontsize_trackbar)
cv2.createTrackbar("R", "Camera", R, 255, on_R_trackbar)
cv2.createTrackbar("G", "Camera", G, 255, on_G_trackbar)
cv2.createTrackbar("G", "Camera", B, 255, on_B_trackbar)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret is False:
        print("Can't receive")
        break

    #Text
    cv2.putText(frame, "TEXT", topLeft, cv2.FONT_HERSHEY_SIMPLEX, 1+fontsize, (B, G, R), 1 + bold)

    #Display
    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
