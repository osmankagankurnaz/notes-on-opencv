# HSV Colorspace

import cv2 as cv

img = cv.imread("images/profile.jpg")

cv.namedWindow("rgb", cv.WINDOW_AUTOSIZE)

cv.imshow("rgb", img)
cv.waitKey(1000)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("gray", gray)
cv.waitKey(1000)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

cv.imshow("hsv", hsv)
cv.waitKey(1000)

cv.destroyAllWindows()
