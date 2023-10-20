import cv2 as cv

path = "/Users/osmankagan/Desktop/OpenCV/images/"
img = cv.imread(path + "profile.jpg")

cv.namedWindow("image", cv.WINDOW_AUTOSIZE)

h, w, ch = img.shape

print(h, w, ch)

for row in range(h):
    for col in range(w):
        b, g, r = img[row, col]
        b = 255 - b
        g = 255 - g
        r = 255 - r
        img[row, col] = [b, g, r]

cv.imshow("output", img)
cv.waitKey(1000)