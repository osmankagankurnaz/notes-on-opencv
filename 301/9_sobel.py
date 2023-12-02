import cv2 as cv
import numpy as np

src = cv.imread("images/profile.jpg")

h, w = src.shape[:2]

x_grad = cv.Sobel(src, cv.CV_32F, 1, 0)
y_grad = cv.Sobel(src, cv.CV_32F, 0, 1)

x_grad = cv.convertScaleAbs(x_grad)
y_grad = cv.convertScaleAbs(y_grad)

cv.imshow("x_grad", x_grad)
cv.waitKey(2000)

cv.imshow("y_grad", y_grad)
cv.waitKey(2000)

dst = cv.add(x_grad, y_grad)
dst = cv.convertScaleAbs(dst)

cv.imshow("gradient", dst)
cv.waitKey(2000)
