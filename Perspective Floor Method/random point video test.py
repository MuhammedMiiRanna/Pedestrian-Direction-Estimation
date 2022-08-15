import cv2 as cv
import numpy as np
from time import time
from os import listdir
import generalLib as glib
import perspectiveFloorLib as pflib


starting_time = time()


def choosePoint(points):
    p1, p2 = points
    # To be removed
    # p1 = tuple(reversed(p1))
    # p2 = tuple(reversed(p2))

    # return choice(points[0])
    # x = int((p1[0] + p2[0])/2)
    # y = int((p1[1] + p2[1])/2)
    # if y < h//2:
    #     if p1[1] >= h//2:
    #         return p1
    #     return p2
    # return (x, y)

    if p1[1] > p2[1]:
        return p1
    return p2


old_shape, new_shape = pflib.get_new_old_shape()
old_dim, new_dim = pflib.get_new_old_dim()
new_height, new_width = h, w = new_dim
floor, horizons_range, angles_range = pflib.draw_perspective_floor()

main_direc = direc = glib.dataset_directories['B']
waiting_Key = int(1000/25)
history = []


pics = listdir()
for pic in pics:
    if 'png' in pic:
        history.append(pic)
# try:
print('I\'am In')
if 1 == 1:
    pic_direcs = [
        r'GaitDatasetA-silh\hy\00_2',
        r'GaitDatasetA-silh\hy\00_4',
        r'GaitDatasetA-silh\ml\00_4',
        r'GaitDatasetA-silh\wl\00_2',
        r'GaitDatasetA-silh\wl\00_4'
    ]
    # while True:
    for direc in pic_direcs:
        # direc = main_direc
        # # floor_2 = drawPerspectiveFloor()[0]
        # while not isfile(direc):
        #     direc = path(direc, choice(listdir(direc)))
        # direc = picDirec(direc)
        # if direc in history:
        #     continue
        # history.append(direc)
        # print(history)

        # i think there is something missing here

        pictures = listdir(direc)
        pic_info = pictures[0][3:5]
        if not pic_info in ['00']:
            continue
        for _ in range(0, 1):
            try:
                # direc, pic_name, n_frmaes, res_print=False
                # path(direc, pic)
                first__image = cv.imread(path(direc, pictures[0]))
                second_image = cv.imread(path(direc, pictures[-1]))

                first__image = cv.resize(
                    first__image, tuple(reversed(dim[:2])))
                second_image = cv.resize(
                    second_image, tuple(reversed(dim[:2])))

                (oldH, oldW) = second_image.shape[:2]
                index = 0
                again = False
                while True:
                    index += 1
                    first__points = list(interest_points(
                        first__image, reverse=True)[0])
                    if first__points[0][1] >= oldH//2 or first__points[1][1] >= oldH//2:
                        break
                    elif index == len(pictures):
                        again = True
                        break
                    first__image = cv.imread(path(direc, pictures[index]))
                    # print(f'{first__points[0][1]} / {first__points[1][1]} ')
                    # first__image = cv.resize(first__image, (1080, 720))
                if again:
                    continue
                # wth what's that?
                # first__image = cv.resize(first__image, tuple(reversed(dim[:2])))
                second_points = list(interest_points(
                    second_image, reverse=True)[0])

                # ##############################################################""
                point_1 = choosePoint(first__points)
                point_2 = choosePoint(second_points)
                # point_1 = choice(first__points)
                # point_2 = choice(second_points)

                # first__points[0] = newCoordinate(
                #     first__points[0], (oldW, oldH), (newW, newH))
                # first__points[1] = newCoordinate(
                #     first__points[1], (oldW, oldH), (newW, newH))
                # second_points[0] = newCoordinate(
                #     second_points[0], (oldW, oldH), (newW, newH))
                # second_points[1] = newCoordinate(
                #     second_points[1], (oldW, oldH), (newW, newH))
                # ##############################################################""
                # first__image = cv.resize(
                #     first__image, tuple(reversed(dim[:2])))
                # second_image = cv.resize(
                #     second_image, tuple(reversed(dim[:2])))
                scene = cv.bitwise_xor(first__image, second_image)
                scene = cv.bitwise_or(scene, floor)

                # All points: BGR
                # scoop(scene, first__points[0])
                # scoop(scene, first__points[1])
                # scoop(scene, second_points[0])
                # scoop(scene, second_points[1])
                # Chosen point:
                scoop(scene, point_1)
                scoop(scene, point_2)
                cv.circle(scene, first__points[0], 6, (0, 255, 0), -1)
                cv.circle(scene, first__points[1], 6, (255, 0, 0), -1)
                cv.circle(scene, second_points[0], 6, (0, 255, 0), -1)
                cv.circle(scene, second_points[1], 6, (255, 0, 0), -1)
                # cv.circle(scene, point_1, 5, (255, 0, 255), -1)
                # cv.circle(scene, point_2, 5, (255, 0, 255), -1)

                # P1
                horizen = locateHorizen(point_1)
                column = locateAngle(point_1, floor.shape)
                area = locateArea(point_1)
                point_1 = (point_1, (horizen, column), area)
                # P2
                horizen = locateHorizen(point_2)
                column = locateAngle(point_2, floor.shape)
                area = locateArea(point_2)
                point_2 = (point_2, (horizen, column), area)
                delta_coord = delta(point_1[1], point_2[1])
                angle_estm = HorAngle(point_1[2], point_2[2], delta_coord)

                # putInfo(img, p1, p2, cp1, cp2, dh, dc, angle_est, angle)
                putInfo(scene, first__points, second_points, point_1,
                        point_2, delta_coord[0], delta_coord[1], angle_estm, '270', 0)
                # cv.imshow('scene', scene)
                # cv.waitKey()
                # cv.destroyAllWindows()
                cv.imwrite(pictures[0], scene)

            # except Exception as exep:
            #     print('==>', exep)
            #     Beep(550, 3000)
            #     continue
            #     direc = main_direc
            # except KeyboardInterrupt:

            #     print("DoNe!!!!")
            #     print("it toke A Total oF: ", timeToked(time()-starting_time))
            #     exit(0)
            #     direc = main_direc
            except ValueError:
                print('hmmm')
                direc = main_direc

            direc = main_direc
