import cv2

src = cv2.imread("c:/images/picture01.jpg")

#dst = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

dst = cv2.cvtColor(src, cv2.IMREAD_GRAYSCALE)
dst = cv2.Canny(dst, 100, 200, apertureSize=3, L2gradient=True)


cv2.imshow("", src)
cv2.imshow("", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
