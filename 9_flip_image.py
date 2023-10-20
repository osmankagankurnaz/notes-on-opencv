import cv2 as cv

path = "/Users/osmankagan/Desktop/OpenCV/images/"

img = cv.imread(path + "profile.jpg")

cv.imshow("image", img)
cv.waitKey(1000)

# X flip

dst1 = cv.flip(img, 0)
cv.imshow("x-flip", dst1)
cv.waitKey(1000)

# Y flip

dst2 = cv.flip(img, 1)
cv.imshow("y-flip", dst2)
cv.waitKey(1000)

# XY flip

dst3 = cv.flip(img, -1)
cv.imshow("yx-flip", dst3)
cv.waitKey(1000)