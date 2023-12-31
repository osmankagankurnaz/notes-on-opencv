import cv2 as cv
import numpy as np

img = cv.imread("images/profile.jpg")

type(img)  # numpy.array

cv.namedWindow("create_image", cv.WINDOW_AUTOSIZE)
cv.imshow("create_image", img)
cv.waitKey(1000)

m1 = np.copy(img)
m2 = img

img[100:-100, 800:-100, :] = 255  # Sets the selected area to white.
cv.imshow("m2", m2)
cv.waitKey(1000)

m3 = np.zeros(img.shape, img.dtype)  # A black image appears.
cv.imshow("m3", m3)
cv.waitKey(1000)

m4 = np.zeros([512, 512], np.uint8)
cv.imshow("m4", m4)
cv.waitKey(1000)

m5 = np.zeros([512, 512], np.uint8)
m5[:, :] = 127
cv.imshow("m5", m5)
cv.waitKey(1000)

cv.destroyAllWindows()
