import cv2 as cv
import numpy as np

src = cv.imread("images/profile.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
cv.waitKey(2000)

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
cv.waitKey(2000)

ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

print(ret)

h, w = src.shape[:2]

cv.imshow("binary", binary)
cv.waitKey(2000)
