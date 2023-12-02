import cv2 as cv
import numpy as np

img1 = cv.imread("images/left_img.png")
img2 = cv.imread("images/right_img.png")

cv.namedWindow("image", cv.WINDOW_AUTOSIZE)

cv.imshow("spider_man_1", img1)
cv.waitKey(1000)

cv.imshow("spider_man_2", img2)
cv.waitKey(1000)

horizontal = np.hstack((img1, img2))
cv.imshow("spider_man", horizontal)
cv.waitKey(1000)

cv.destroyAllWindows()
