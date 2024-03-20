import cv2
import numpy as np

src = cv2.imread("loopy.jpeg", cv2.IMREAD_COLOR)

#b, g, r = cv2.split(src)
b = src[:, :, 0]
g = src[:, :, 1]
r = src[:, :, 2]

inverse = cv2.merge((r, g, b))

cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)

cv2.imshow("inverse", inverse)
cv2.waitKey()
cv2.destroyAllWindows()