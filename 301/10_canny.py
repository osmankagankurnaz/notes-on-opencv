import cv2 as cv

src = cv.imread("images/profile.jpg")

cv.imshow("profile", src)
cv.waitKey(2000)

edge = cv.Canny(src, 100, 200)

cv.imshow("canny", edge)
cv.waitKey(2000)
