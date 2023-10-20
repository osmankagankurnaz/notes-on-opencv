import cv2 as cv

path = "/Users/osmankagan/Desktop/OpenCV/images/"
img = cv.imread(path + "profile.jpg")

T = 127 # gri rengi

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

for i in range(5):
    ret, binary = cv.threshold(gray, T, 255, i)
    cv.imshow("binary_" + str(i), binary)
    cv.waitKey(1000)