import cv2 as cv
import numpy as np
from time import time
from random import randint
from os import getcwd, listdir
import generalLib as glib
import perspectiveFloorLib as pflib


# initialization:
starting_time = time()
floor = pflib.draw_perspective_floor()[0]
new_dim, old_dim = pflib.get_new_old_dim()
main_direc = glib.dataset_directories['A']
waiting_Key = int(1000/35)
path_changed = False
pTime = 0



while True:
    if not path_changed:
        walker_folders = listdir(main_direc)
        choosen_walker = walker_folders[randint(0, len(walker_folders)-1)]
        choosen_angle = glib.dataset_angles['A'][randint(0, len(glib.dataset_angles['A'])-1)]
        # to avoid some angle, as u choose
        # if choosen_angle != "45":
        #     continue
        choosen_set = str(randint(1, 4))
        path = main_direc + "/"+choosen_walker+"/"+choosen_angle+"_"+choosen_set
        pictures = listdir(path)
    else:
        pictures = listdir(path_changed)
        path_changed = False

    print("Path is: >>{:^30}<<".format(path))
    for pic in pictures:
        #############################################
        # fps infos:
        cTime = time()
        latency = cTime-pTime
        fps = 1/(cTime-pTime)
        pTime = cTime
        #############################################
        img = cv.imread(glib.join_path(path, pic))
        img = cv.resize(img, new_dim)
        scene = cv.bitwise_or(floor, img)
        glib.put_fps(scene, fps, latency, put_latency=True)
        cv.imshow('Video test', glib.resize_image(scene, scale=0.8))
        if cv.waitKey(waiting_Key) & 0xFF == 115:
            # press 's' to stop the current video
            break
    if cv.waitKey() & 0xFF == 113:
        # press 'q' to quit the current video.
        # press anyKey to for the next video.
        break
    else:
        continue

print("\a\a\a>> Time: {} Minute!! {:.3f} Second!!".format(
    int((time()-starting_time)/60), (time()-starting_time) % 60))
