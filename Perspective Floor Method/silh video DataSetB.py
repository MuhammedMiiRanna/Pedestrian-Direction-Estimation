import cv2 as cv
from time import time
from os import listdir
from random import choice
import generalLib as glib
from os.path import isfile
import perspectiveFloorLib as pflib


direc = main_direc = glib.dataset_directories['B']
floor = pflib.draw_perspective_floor()[0]
new_dim = tuple(reversed(floor.shape[:2]))
waiting_Key = int(1000/25)
history = []
pTime = time()


while True:
    # get a random pic directorie which isn't in the directorie
    while not isfile(direc):
        direc = glib.path(direc, choice(listdir(direc)))
    direc = glib.pic_direc(direc)
    if direc in history:
        continue
    history.append(direc)  # append the direc in the history

    pictures = listdir(direc)
    glib.B_dataset_details(
        direc, pictures[0], len(pictures), print_res=True)

    for index, pic in enumerate(pictures):
        if index == 0:
            print('Calculating!')
            img = cv.imread(glib.path(direc, pic))
            cv.imshow('img', img)
            cv.waitKey()
            cv.destroyAllWindows()
            first_points = pflib.interest_points(img)[0]
            # new_coordinate(oldCoord, oldDim, newDim)
            first_points = (glib.new_coordinate(first_points[0], tuple(reversed(img.shape)), new_dim), 
                            glib.new_coordinate(first_points[1], tuple(reversed(img.shape)), new_dim))
            img = cv.resize(img, new_dim)
            scene = cv.bitwise_or(floor, img)
            # floor = cv.bitwise_or(pflib.draw_perspective_floor()[0], img)
            print('Done Calculating!')
            # scene = floor
            # scene = prepareScene(pic, floor, direc, 1 /
            #                      (cTime-pTime), cTime-pTime)
        elif index == len(pictures)-1:
            print('Calculating!')
            img = cv.imread(
                glib.path(direc, pictures[-1]))
            last_points, img = pflib.interest_points(img)[0:2]
            last_points = (glib.new_coordinate(last_points[0], img.shape, floor.shape), 
                            glib.new_coordinate(last_points[1], img.shape, floor.shape))

            img = cv.resize(img, (1080, 720))
            scene = cv.bitwise_or(floor, img)
            print('Done Calculating!')

            scene = cv.circle(scene, tuple(
                reversed(first_points[0])), 3, (255, 0, 0), 3)
            scene = cv.circle(scene, tuple(
                reversed(first_points[1])), 3, (255, 0, 0), 3)
            scene = cv.circle(scene, tuple(
                reversed(last_points[0])), 3, (255, 0, 0), 3)
            scene = cv.circle(scene, tuple(
                reversed(last_points[1])), 3, (255, 0, 0), 3)
        else:
            cTime = time()
            img = cv.imread(glib.path(direc, pic))
            img = cv.resize(img, new_dim)
            # floor = cv.bitwise_or(floor, img)
            scene = glib.prepare_scene(pic, floor, direc, 1 /
                                       (cTime-pTime), cTime-pTime)

        cTime = time()
        cv.imshow('data Set B', glib.resize_image(scene, scale=1))
        pTime = cTime
        if cv.waitKey(waiting_Key) & 0xFF == 115:
            break

    cv.waitKey(4000)
    cv.destroyAllWindows()
    direc = main_direc


cv.destroyAllWindows()
