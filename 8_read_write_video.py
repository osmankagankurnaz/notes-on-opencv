import cv2 as cv
import numpy as np

video = cv.VideoCapture("/Users/osmankagan/Desktop/OpenCV/videos/video.mp4")

height = video.get(cv.CAP_PROP_FRAME_HEIGHT)
width = video.get(cv.CAP_PROP_FRAME_WIDTH)
count = video.get(cv.CAP_PROP_FRAME_COUNT)
fps = video.get(cv.CAP_PROP_FPS)

print(height, width, count, fps)

out = cv.VideoWriter("/Users/osmankagan/Desktop/OpenCV/videos/ds_path_save.mp4",
                     cv.VideoWriter.fourcc('D', 'I', 'V', 'X'), 60,
                     (np.int64(width), np.int64(height)), True)

# yukarıdaki 60 değeri kayıt edilen videonun fps değerini ifade eder

while True:
    # kameradan görüntü al
    ret, frame = video.read()

    # görüntü başarıyla alındı mı kontrol et
    if ret is True:
        # okunan görüntüyü ekranda göster
        cv.imshow("video-input", frame)
        out.write(frame)

        # 10 saniye sonra çık
        c = cv.waitKey(10)
        
        if c == 27: # ESC tuşuna basılırsa döngü kırılır
            break
    else:
        break

video.release()