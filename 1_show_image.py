import cv2 as cv

path = "/Users/osmankagan/Desktop/OpenCV/images/"

img = cv.imread(path + "profile.jpg")

type(img) # numpy.array

cv.namedWindow("opencv_test", cv.WINDOW_AUTOSIZE)

cv.imshow("opencv_test", img)
cv.waitKey(1000) # -1 outputu işlemin çalıştığı anlamına gelir.

cv.destroyAllWindows()