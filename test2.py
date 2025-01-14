
import cv2
import numpy as np
from itertools import repeat
from multiprocessing import Pool


def video2imgs_old(vid_path, save_path, ext = '.png',cut_frame = 10):
    cap = cv2.VideoCapture(vid_path)
    count = 0
    while True:
        if count > cut_frame:
            break
        ret, frame = cap.read()
        if ret:
            #cv2.imwrite(f"{save_path}/{count:08d}.png", frame, [int(cv2.IMWRITE_PNG_COMPRESSION),9])
            # frame_nobg = remove(frame)

            # Adjusted green color range
            lower_green = np.array([40, 60, 130])
            upper_green = np.array([77, 255, 255])

            # Convert the frame to HSV color space for better color detection
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, lower_green, upper_green)

            # Improve the mask using morphological operations
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
            mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))

            # Create the inverse mask
            mask_inv = cv2.bitwise_not(mask)

            # Use the mask to extract the foreground (original frame) and the background (replacement image)
            frame_final = cv2.bitwise_and(frame, frame, mask=mask_inv)
            # bg = cv2.bitwise_and(image, image, mask=mask)

            # cv2.imwrite("output_opencv.png", output_image)


            cv2.imwrite(f"{save_path}/{count:08d}.png", frame_final, [int(cv2.IMWRITE_PNG_COMPRESSION),9])
            count += 1
        else:
            break

video2imgs_old("./data/example/huangjinbiao6/huang720p.25fps.170s.mov", "./tmp/nocomp")

# a_args = ['a', 'b', 'c']
# fal = zip(range(4), repeat(2), repeat(3))
# print(list(fal))

print(5762/4)