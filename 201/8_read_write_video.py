import cv2 as cv
import numpy as np

video = cv.VideoCapture("videos/video.mp4")

height = video.get(cv.CAP_PROP_FRAME_HEIGHT)
width = video.get(cv.CAP_PROP_FRAME_WIDTH)
count = video.get(cv.CAP_PROP_FRAME_COUNT)
fps = video.get(cv.CAP_PROP_FPS)

print(height, width, count, fps)

out = cv.VideoWriter(
    "videos/ds_path_save.mp4",
    cv.VideoWriter.fourcc("D", "I", "V", "X"),
    60,
    (np.int64(width), np.int64(height)),
    True,
)

# The value 60 above refers to the fps value of the recorded video.

while True:
    # Taking images from camera.
    ret, frame = video.read()

    # Checking if the image was received successfully.
    if ret is True:
        # Displaying the read image on the screen.
        cv.imshow("video-input", frame)
        out.write(frame)

        # Exit after 10 seconds.
        c = cv.waitKey(10)

        if c == 27:  # If the ESC key is pressed, the loop is broken.
            break
    else:
        break

video.release()
