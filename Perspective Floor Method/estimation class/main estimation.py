import cv2 as cv
import numpy as np
from time import time
from os import listdir, chdir, getcwd
from os.path import isfile
from random import random, randint, choice
from math import degrees, acos, sqrt
from winsound import Beep
from perspClass import PerspectiveFloor, Point, Scene
from perspLib import timeToked, path, picDirec, BdataSetInfo, interest_points
from perspLib import locateHorizen, locateAngle, locateArea, delta, HorAngle, putInfo


starting_time = time()
with open('Script/PrespectiveFloor/result/totalTime.txt', 'r') as totalTime:
    total_time = float(totalTime.readline())
floor_object = PerspectiveFloor((1080, 720, 3))
floor_sample = floor_object.getFloor()
hrzns_rng = floor_object.getHorizonRange()
angles_rng = floor_object.getColumAngleRange()
main_areas = floor_object.getMainAreas()

old_dim = (240, 352, 3)
new_dim = (720, 1056, 3)
newH, newW = new_dim[:2]

angels = ['000', '018', '036', '054', '072',
          '090', '108', '126', '144', '162', '180']
current_direc = getcwd()
result_direc = 'Script\PrespectiveFloor/result'
main_direc = "GaitDatasetB-silh"
waiting_Key = int(1000/25)
history = []
walk_stats = {
    'nm': 'Normal',
    'cl': 'In Coat',
    'bg': 'In Bag',
}

# saving old pictures
# to avoid them in the next calculations
chdir(result_direc)
pictures_folder = listdir()
for folder in pictures_folder:
    pictures = listdir(folder)
    for picture in pictures:
        if 'png' in picture:
            history.append(picture)

chdir(current_direc)
print('I\'am In')
if 1 == 1:
    while True:
        try:
            direc = main_direc
            while not isfile(direc):
                direc = path(direc, choice(listdir(direc)))
            direc = picDirec(direc)
            if direc in history:
                continue
            history.append(direc)

            # i think there is something missing here
            pictures = listdir(direc)
            BdataSetInfo(direc, pictures[0], len(pictures), res_print=True)
            pic_info = BdataSetInfo(pic_name=pictures[0])
            # if pic_info[3] in ['000', '090', '180']:
            #     continue
            # for index, pic in enumerate(pictures):
            for _ in range(0, 1):
                first__image = cv.imread(path(direc, pictures[0]))
                second_image = cv.imread(path(direc, pictures[-1]))
                first__image = cv.resize(
                    first__image, tuple(reversed(new_dim[:2])))
                second_image = cv.resize(
                    second_image, tuple(reversed(new_dim[:2])))

                (oldH, oldW) = second_image.shape[:2]
                index = 0
                again = False
                while True:
                    index += 1
                    p11, p12 = interest_points(first__image, reverse=True)
                    if p11.getY >= oldH//2 or p12.getY >= oldH//2:
                        break
                    elif index == len(pictures):
                        again = True
                        break
                    first__image = cv.imread(path(direc, pictures[index]))
                    first__image = cv.resize(first__image, (1080, 720))
                if again:
                    continue
                p21, p22 = interest_points(second_image, reverse=True)
                # ##############################################################""
                first__points = p11, p12
                second_points = p21, p22
                point_1 = p11.isLower(p12)
                point_2 = p21.isLower(p22)

                scene = Scene(floor_sample, first__image,
                              second_image, first__points, second_points)
                # scene = cv.bitwise_xor(first__image, second_image)
                # scene = cv.bitwise_or(scene, floor)

                # P1
                horizen = locateHorizen(point_1, hrzns_rng)
                column = locateAngle(point_1, angles_rng)
                area = locateArea(point_1, main_areas)
                point_1 = (point_1, (horizen, column), area)
                # P2
                horizen = locateHorizen(point_2, hrzns_rng)
                column = locateAngle(point_2, angles_rng)
                area = locateArea(point_2, main_areas)
                point_2 = (point_2, (horizen, column), area)
                delta_coord = delta(point_1[1], point_2[1])
                angle_estm = HorAngle(point_1[2], point_2[2], delta_coord)

                # putInfo(img, p1, p2, cp1, cp2, dh, dc, angle_est, angle)
                putInfo(scene, first__points, second_points, point_1, point_2,
                        delta_coord[0], delta_coord[1], angle_estm, pic_info[3], 0)
                cv.imshow('scene', scene)
                cv.waitKey()
                cv.destroyAllWindows()
                cv.imwrite(pictures[0], scene)

        except Exception as exep:
            print('==>', exep)
            Beep(550, 3000)
            continue
            direc = main_direc
        except KeyboardInterrupt:
            print("DoNe!!!!")
            print("it toke A Total oF: ", timeToked(time()-starting_time))
            exit(0)
        except ValueError:
            print('hmmm')
        finally:
            with open('Script/PrespectiveFloor/result/totalTime.txt', 'w') as totalTime:
                totalTime.write(total_time+(time()-starting_time))
