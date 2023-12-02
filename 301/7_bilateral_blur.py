import cv2 as cv
import numpy as np

src = cv.imread("images/profile.jpg")

cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
cv.waitKey(4000)

h, w = src.shape[:2]
dst = cv.bilateralFilter(src, 0, 100, 10)

result = np.zeros([h, w * 2, 3], dtype=src.dtype)
result[0:h, 0:w, :] = src
result[0:h, w : 2 * w, :] = dst

cv.imshow("result", result)
cv.waitKey(4000)
