import cv2 as cv
import numpy as np
from time import time
from os import listdir
from random import randint, random, choice
from lib import path, walkStatuFilter, drawPerspectiveFloor, resImg, putFps, fill


# initialization:
main_direc = "GaitDatasetC-silh"
subjects = listdir(main_direc)
walk_stats = {
    "fn": "Normal Walk",
    "fq": "Fast Walk",
    "fs": "Slow Walk",
    "fb": "with a bag",
}
history = []
waiting_Key = int(1000/25)
floor = drawPerspectiveFloor()[0]
pTime = 0

while True:
    chosen_subject = str(choice(subjects))
    # cause the folders are all in numbers
    walking_status_samples = listdir(path(main_direc, chosen_subject))
    walking_status = choice(list(walk_stats.keys()))
    walking_status_samples = walkStatuFilter(
        walking_status_samples, walking_status)
    sequence = choice(walking_status_samples)
    # sequence_number = "{:02}".format(randint(0,1)) if walking_status != "fn" else "{:02}".format(randint(0,3))
    full_path = path(main_direc, chosen_subject, sequence)
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
        scene = putFps(scene, fps, latency, pLate=True)
        cv.imshow(walk_stats[walking_status], resImg(scene, scale=0.9))
        cv.waitKey(waiting_Key)
        #############################################
    # print(">> Continue (y/n) r (c)!")
    # decision = input("==> ")
    decision = "y"
    cv.destroyAllWindows()
