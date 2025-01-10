
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
            lower_green = np.array([40, 80, 110])
            upper_green = np.array([70, 255, 255])

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


def count_frames_manual(video_path):
	# initialize the total number of frames read
    total = 0
    video = cv2.VideoCapture(video_path)
    
    while True:
        grabbed, frame = video.read()
        if not grabbed:
            break
        total += 1
    
    video.release()
    return total


def video2imgs_job(group_number, frame_jump_unit, num_processes, vid_path, save_path):
    vid = cv2.VideoCapture(vid_path)
    pos_frames = int(frame_jump_unit * group_number)
    vid.set(cv2.CAP_PROP_POS_FRAMES, pos_frames)
    proc_frames = 0

    # f = open(f"log{group_number}.txt", "w")


    is_last_seg = False
    if group_number == num_processes-1:
        is_last_seg = True

    while True:
        ret, frame = vid.read()
        if ret:
            if not is_last_seg and proc_frames >= frame_jump_unit:
                break
            cur_frame = pos_frames + proc_frames
            # print(f"{group_number}: {cur_frame:08d}.png")
            # f.write(f"{group_number}: {cur_frame:08d}.png\n")
            proc_frames += 1
        else:
            # if not ret:
            #     print(f"{group_number}: no ret")
            # if proc_frames >= frame_jump_unit:
            #     print(f"{group_number}: proc_frames >= frame_jump_unit")
            break

    vid.release()
    # f.close()
    return None


def video2imgs(vid_path, save_path):
    num_processes = 4

    video_frame_cnt = 5762
    # video_frame_cnt = count_frames_manual(vid_path)

    cap = cv2.VideoCapture(vid_path)
    
    pool = Pool(num_processes)

    frame_jump_unit = video_frame_cnt // num_processes

    print(f"frame_jump_unit: {frame_jump_unit}")

    
    pool.starmap(video2imgs_job, zip(range(num_processes), repeat(frame_jump_unit), repeat(num_processes), repeat(vid_path), repeat(save_path) ))

    cap.release()

video2imgs("./data/example/huangjinbiao/huang1080p.30fps.mov", "./tmp/nocomp")

# a_args = ['a', 'b', 'c']
# fal = zip(range(4), repeat(2), repeat(3))
# print(list(fal))

print(5762/4)