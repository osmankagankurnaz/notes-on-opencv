import cv2 as cv

img = cv.imread("images/profile.jpg")

T = 127  # gray color code

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

for i in range(5):
    ret, binary = cv.threshold(gray, T, 255, i)
    cv.imshow("binary_" + str(i), binary)
    cv.waitKey(1000)
