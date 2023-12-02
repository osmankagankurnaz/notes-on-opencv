import cv2 as cv

cap = cv.VideoCapture("videos/gly.mp4")

fgbg = cv.createBackgroundSubtractorMOG2(history=250, varThreshold=20)

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    background = fgbg.getBackgroundImage()
    cv.imshow("input", frame)
    cv.imshow("mask", fgmask)
    cv.imshow("background", background)
    k = cv.waitKey(10) & 0xFF
    if k == 27:
        break

cap.release()
