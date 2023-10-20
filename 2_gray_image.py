import cv2 as cv

path = "/Users/osmankagan/Desktop/OpenCV/images/"

img = cv.imread(path + "profile.jpg")

cv.namedWindow("colored", cv.WINDOW_AUTOSIZE)

cv.imshow("gray", img)
cv.waitKey(1000)

#cvtColor

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("gray", gray)
cv.waitKey(1000)

#imwrite

cv.imwrite(path + "gray_profile.png", gray)
cv.destroyAllWindows()

# other method
img = cv.imread(path + "profile.jpg", cv.IMREAD_GRAYSCALE)

cv.namedWindow("colored", cv.WINDOW_AUTOSIZE)
cv.imshow("gray", gray)
cv.waitKey(1000)