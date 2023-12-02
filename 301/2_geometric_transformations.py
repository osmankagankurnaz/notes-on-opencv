import cv2 as cv
import numpy as np

# shifting

img = cv.imread("images/profile.jpg")

rows = img.shape[0]
cols = img.shape[1]

print(rows, cols)

M = np.float32([[1, 0, 300], [0, 1, 90]])
shifted = cv.warpAffine(img, M, (cols, rows))

cv.imshow("original", img)
cv.waitKey(1000)

cv.imshow("shifted", shifted)
cv.waitKey(1000)

# rotation

M = cv.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
dst = cv.warpAffine(img, M, (cols, rows))
cv.imshow("rotation", dst)
cv.waitKey(1000)

# scaling

res = cv.resize(img, None, fx=0.2, fy=0.2, interpolation=cv.INTER_CUBIC)

cv.imshow("scaling", res)
cv.waitKey(1000)

cv.destroyAllWindows()
