import cv2 as cv

img = cv.imread("images/profile.jpg")

type(img)  # numpy.array

cv.namedWindow("opencv_test", cv.WINDOW_AUTOSIZE)

cv.imshow("opencv_test", img)
cv.waitKey(1000)  # An output of -1 means the process is running.

cv.destroyAllWindows()
