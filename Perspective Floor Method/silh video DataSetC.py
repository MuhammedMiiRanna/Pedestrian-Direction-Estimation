import cv2 as cv
import numpy as np
from time import time
from os import listdir
from random import choice
import generalLib as glib
import perspectiveFloorLib as pflib
# from lib import path, walkStatuFilter, drawPerspectiveFloor, resImg, putFps, fill


# initialization:
main_direc = glib.dataset_directories['C']
walk_stats = glib.dataset_walker_status['C']
subjects = listdir(main_direc)

floor = pflib.draw_perspective_floor()[0]
waiting_Key = int(1000/25)
history = []
pTime = 0

while True:
    chosen_subject = str(choice(subjects))
    # cause the folders are all in numbers
    walking_status_samples = listdir(glib.path(main_direc, chosen_subject))
    walking_status = choice(list(walk_stats.keys()))
    walking_status_samples = glib.walk_statu_filter(
        walking_status_samples, walking_status)
    sequence = choice(walking_status_samples)
    # sequence_number = "{:02}".format(randint(0,1)) if walking_status != "fn" else "{:02}".format(randint(0,3))
    full_path = glib.path(main_direc, chosen_subject, sequence)
    if full_path in history:
        continue
    history.append(full_path)
    pictures = listdir(full_path)

    print("Path is:>>{:^33}<<".format(full_path))
    for pic in pictures:
        cTime = time()
        latency = cTime-pTime
        fps = 1/(cTime-pTime)
        pTime = cTime
        #############################################
        img = cv.imread(full_path+"/"+pic)
        img = cv.resize(img, tuple(reversed(floor.shape[:2])))
        # img = fill(img)
        scene = cv.bitwise_or(floor, img)
        scene = glib.put_fps(scene, fps, latency, put_latency=True)
        cv.imshow(walk_stats[walking_status],
                  glib.resize_image(scene, scale=0.9))
        if cv.waitKey(waiting_Key) & 0xFF == 115:
            # press 's' to stop the current video
            break
        #############################################
    if cv.waitKey(4000) & 0xFF == 113:
        # press 'q' to quit
        break
    cv.destroyAllWindows()

cv.destroyAllWindows()
