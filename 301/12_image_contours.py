import cv2 as cv
import numpy as np


def threshold_demo(image):
    dst = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY)
    cv.imshow("binary", binary)
    return binary


def canny_demo(image):
    t = 100
    canny_output = cv.Canny(image, t, t * 2)
    cv.imshow("canny_output", canny_output)
    return canny_output


src = cv.imread("images/profile.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
cv.waitKey(2000)

binary = threshold_demo(src)
cv.imshow("binary", binary)
cv.waitKey(2000)

canny = canny_demo(src)
cv.imshow("canny", canny)
cv.waitKey(2000)

contours, hierarchy = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

for c in range(len(contours)):
    cv.drawContours(src, contours, c, (0, 0, 255), 2, 8)

cv.imshow("contours-demo", src)
cv.waitKey(2000)
