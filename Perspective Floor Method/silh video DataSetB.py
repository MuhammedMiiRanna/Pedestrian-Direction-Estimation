import cv2 as cv
from time import time
import generalLib as glib
import perspectiveFloorLib as pflib
from sys import exit


floor = pflib.draw_perspective_floor()[0]
new_dim, old_dim = pflib.get_new_old_dim()
directory = main_direc = glib.dataset_directories['B']
waiting_Key = int(1000/25)
history = []
pTime = time()


while True:
    # we used here different logic then A_video to get a random
    # pic directorie which isn't in the directories history.
    pictures, directory = glib.random_path(directory, history)
    if pictures is None:
        # sys.exit(): in case we didn't find any new image folder.
        exit('all image folders has been seen.')
    glib.print_B_dataset_details(
        directory, pictures[0], len(pictures), print_res=True)

    for index, pic in enumerate(pictures):
        if index == 0:
            print('Calculating!')
            img = cv.imread(glib.join_path(directory, pic))
            # this comment will be removed when new_coordinate func is fixed.
            # first_points = pflib.interest_points(img)[0]
            # first_points = (glib.new_coordinate(first_points[0], old_dim, new_dim),
            #                 glib.new_coordinate(first_points[1], old_dim, new_dim))
            img = cv.resize(img, new_dim)
            scene = cv.bitwise_or(floor, img)
            print('Done Calculating!')
        elif index == len(pictures)-1:
            print('Calculating!')
            img = cv.imread(glib.join_path(directory, pictures[-1]))
            # this comment will be removed when new_coordinate func is fixed.
            # last_points, img = pflib.interest_points(img)[0:2]
            # last_points = (glib.new_coordinate(last_points[0], old_dim, new_dim),
            #                glib.new_coordinate(last_points[1], old_dim, new_dim))
            img = cv.resize(img, new_dim)
            scene = cv.bitwise_or(floor, img)
            print('Done Calculating!')

            # this part draw a viewfinder (see viewfinder.py) on the foot points
            # which me our interest points.
            # there is an issue with the new_coord function (check glib.new_coordinate())
            # it gives a margin of error, we can avoid that by resizing the image so
            # we don't need that function, but it will take a large ammount of time.
            # viewfinder.viewfinder(scene, tuple(reversed(first_points[0])))
            # viewfinder.viewfinder(scene, tuple(reversed(first_points[1])))
            # viewfinder.viewfinder(scene, tuple(reversed(last_points[0])))
            # viewfinder.viewfinder(scene, tuple(reversed(last_points[1])))
        else:
            img = cv.imread(glib.join_path(directory, pic))
            img = cv.resize(img, new_dim)
            cTime = time()
            scene = glib.prepare_scene(pic, floor, directory, 1 /
                                       (cTime-pTime), cTime-pTime)

        cv.imshow('dataSet B', glib.resize_image(scene, scale=1))
        pTime = time()
        if cv.waitKey(waiting_Key) & 0xFF == 115:
            # press 's' to stop the current video
            break

    if cv.waitKey(4000) & 0xFF == 113:
        # press 'q' to quit
        break
    cv.destroyAllWindows()
    directory = main_direc

cv.destroyAllWindows()
