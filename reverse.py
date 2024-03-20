import cv2

src = cv2.imread("loopy.jpeg",cv2.IMREAD_COLOR)
#src2 = cv2.imread("NewJeans.jpg",cv2.IMREAD_COLOR)
dst = cv2.bitwise_not(src)
dst1 = cv2.bitwise_and(src, src)
dst2 = cv2.bitwise_or(src, dst)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.waitKey()
cv2.destroyAllWindows()