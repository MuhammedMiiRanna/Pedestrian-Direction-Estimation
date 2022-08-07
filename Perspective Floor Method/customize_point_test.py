import cv2 as cv
from random import choice
from os import listdir
from os.path import isfile
import generalLib as glib
import perspectiveFloorLib as pflib


def draw_circle(event, x, y, flags, param):
    global coord_1, coord_2, both_coord
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(scene, (x, y), 3, (255, 0, 255), -1)
        horizen = pflib.locate_horizen((x, y), horizons_range)
        column = pflib.locate_angle((x, y), scene.shape, angles_range)
        area = pflib.locate_area((x, y))
        print(">> x: {:^3} y: {:^4} ==> {}/{:<2} -- Area : {}".format(x,
                                                                      y, horizen, column, area))
        coord_1 = coord_1
        if not coord_1:
            coord_1 = [(x, y), (horizen, column), area]
        else:
            coord_2 = [(x, y), (horizen, column), area]
        if all([coord_1, coord_2]):
            delta_coord = pflib.delta(coord_1[1], coord_2[1], horizons_range)
            angle_estm = pflib.horizone_angle(
                coord_1[2], coord_2[2], delta_coord)
            print(">> Delta columnY: {}\n>> Delta LineX: {} ".format(
                delta_coord[1], delta_coord[0]))
            if int(angle_estm-10) < int(inf[3]) < int(angle_estm+10):
                print("<< HERE YOU GOO !! >>")
            print(" << Estimation is : {:.3f} >>".format(angle_estm))
            print(" << The pedesterian direction in between >>{:^5}<< & >>{:^5}<<".format(
                int(angle_estm-10), int(angle_estm+10)))
            both_coord = True


# Initialization:
main_direc = glib.dataset_directories['B']
floor, horizons_range, angles_range = pflib.draw_perspective_floor()
shape = floor.shape
standard_dim = (1080, 720)
quit = False

# TODO: add an option to save the pictures

# angles = [0,18,36,54,72,90,108,126,144,162,180]
# angles_result_files = {}
# for angle in angles:
#     angles_result_files[angle] = open("{angle}.txt".format, "a")


# # show list :
# for hrz, rng in hrzns_rng.items():
#     print(">> hrz {:<2} ==> [{:<4} : {:>4}] ".format(hrz, rng[0], rng[1]))
# print("*"*30)
# for column, rng in angles_rng.items():
#     print(">> column {:>2} ==> {} ".format(column, rng))

while not quit:
    both_coord = False
    coord_1 = False
    coord_2 = False
    cv.namedWindow(winname='Silhouette')
    cv.setMouseCallback('Silhouette', draw_circle)
    direc = main_direc

    # locate random pics folder
    while not isfile(direc):
        direc = glib.path(direc, choice(listdir(direc)))
    pic_direc = glib.pic_direc(direc)
    pictures = listdir(pic_direc)
    # return the direc details: ['001', 'nm', '01', '090', '047.']
    inf = pictures[0][:-3].split("-")
    # if inf[3] not in ['000', '090', '180', '270']:
    # TODO: check if this means to ignore those angle
    if inf[3] not in ['108', '072']:
        continue
    glib.B_dataset_details(direc, inf, len(pictures), print_res=True)

    img_1 = cv.imread(glib.path(pic_direc, pictures[0]))
    img_1 = cv.resize(img_1, standard_dim)

    img_2 = cv.imread(glib.path(pic_direc, pictures[-1]))
    img_2 = cv.resize(img_2, standard_dim)
    scene = cv.bitwise_or(img_1, img_2)
    scene = cv.bitwise_or(scene, floor)

    next_sample = False
    while True:
        cv.imshow('Silhouette', scene)
        cv.waitKey(20)
        # if cv.waitKey(20) & 0xFF == 110:
        # if cv.waitKey(20) & both_coord:
        if both_coord:
            break

    print(">> PS: From the scene window:")
    print(">> press C key to continue!")
    print(">> press Q key to Quit? ")

    # another while here to avoid quiting before choosing another point.
    while True and not quit:
        cv.imshow('Silhouette', scene)
        if cv.waitKey(100) & 0xFF == 113:
            quit = True
        elif cv.waitKey(100) & 0xFF == 99:
            break

    # while True:
    #     cv.imshow('Silhouette', scene)
    #     # delta(coord_1, coord_2)
    #     k = cv.waitKey(100) & 0xFF
    #     # press 'q' to exit
    #     if k == ord('q'):
    #         quit = True
    #     elif k == ord('c'):
    #         break
    cv.destroyAllWindows()
    print("*"*30)
