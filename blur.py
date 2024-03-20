import cv2

src = cv2.imread("loopy.jpeg", cv2.IMREAD_COLOR)
dst = cv2.blur(src, (12,12), anchor=(-1, -1), borderType =cv2.BORDER_REFLECT)

cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()