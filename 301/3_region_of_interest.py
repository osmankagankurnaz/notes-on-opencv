import cv2 as cv

src = cv.imread("images/profile.jpg")

h, w = src.shape[:2]

img = src.copy()

roi = img[300:750, 950:1300, :]

cv.imshow("roi", roi)
cv.waitKey(1000)

img[0:450, 0:350, :] = roi

cv.imshow("img + roi", img)
cv.waitKey(1000)
