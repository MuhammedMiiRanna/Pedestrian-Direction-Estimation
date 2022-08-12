import cv2 as cv
import numpy as np
import generalLib as glib
import perspectiveFloorLib as pflib
from os import listdir

""" This script make a figure which contain a simple skelton of three pedestrians, 
it connect three skull_points from the first skelton to the 2nd to the last one.
How to select the skull_points:
    1. run the code.
    2. select those 7 skull_points in the exact order:
        1. head(or skull).
        2. neck.
        3. left hand.
        4. right hand.
        5. pelvic.
        6. left leg.
        7. right leg.
    """
# to save a floor scene image:

# floor = pflib.draw_perspective_floor()[0]
# cv.imshow('floor', floor)
# cv.imwrite('floor scene.png', floor)

# cv.waitKey()
# cv.destroyAllWindows()
# ##############################################


def draw_circle(event, x, y, flags, param):
    global skull_points
    if event == cv.EVENT_LBUTTONDOWN:
        skull_points.append((x, y))
        print(x, y)


cv.namedWindow(winname='Silhouette')
cv.setMouseCallback('Silhouette', draw_circle)


new_dim, _ = pflib.get_new_old_dim()
skull_points_set, skull_points, images = [], [], []
direc = "GaitDatasetA-silh/zyf/45_2"
# direc = "GaitDatasetA-silh/fyc/45_2"
# direc = "GaitDatasetA-silh/zc/45_3"
pictures = listdir(direc)
pictures = [pictures[0], pictures[len(pictures)//2], pictures[-1]]


for picture in pictures:
    path = glib.path(direc, picture)
    img = cv.imread(path)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img = cv.resize(img, new_dim)
    images.append(img)
    cv.imshow('Silhouette', img)

    if cv.waitKey() & 0xFF == 113:
        skull_points_set.append(skull_points)
        print("x"*20)
        skull_points = []
        continue
cv.destroyAllWindows()


result = np.zeros(tuple(reversed(new_dim)), np.uint8)
result = cv.cvtColor(result, cv.COLOR_BGR2RGB)
for pic in pictures:
    result = cv.bitwise_or(result, pic)

print(skull_points_set)
for index, point in enumerate(skull_points_set):
    for xy in point:
        cv.circle(result, xy, 4, pflib.random_color(), -1)
    cv.line(result, point[0], point[1], (255, 0, 255), 2)  # A
    cv.line(result, point[1], point[2], (255, 0, 0), 2)
    cv.line(result, point[1], point[3], (0, 255, 0), 2)
    cv.line(result, point[1], point[4], (0, 0, 255), 2)
    cv.line(result, point[4], point[5], (255, 255, 0), 2)
    cv.line(result, point[4], point[6], (230, 150, 255), 2)
    if index < 2:
        cv.line(result, point[0],
                skull_points_set[index+1][0], (0, 255, 0), 2)
        cv.line(result, point[4],
                skull_points_set[index+1][4], (0, 255, 0), 2)
        cv.line(result, point[6],
                skull_points_set[index+1][6], (0, 255, 0), 2)

cv.imshow("Result", result)
cv.imwrite("Pose figure maker.png", result)
cv.waitKey()
cv.destroyAllWindows()


# ############################################################
# pictures = [
#     "GaitDatasetA-silh/yjf/00_2/yjf-00_2-006.png",
#     "GaitDatasetA-silh/yjf/45_2/yjf-45_2-032.png"
# ]

# pictures = [
#     "GaitDatasetA-silh/hy/00_2/hy-00_2-030.png",
#     "GaitDatasetA-silh/hy/45_2/hy-45_2-005.png"
# ]
# ############################################################
# # Resizing image script
# # pic = [
# #     r"M:\Documents\Projects\End Of Study\End of Study Project\graduation thesis\figures\hy-45_2-005.png",
# #     r"M:\Documents\Projects\End Of Study\End of Study Project\graduation thesis\figures\hy-00_2-030.png"
# # ]
# # for pi in pic:
# #     img = cv.imread(pi)
# #     img = cv.resize(img, (1080,720))
# #     cv.imwrite(pi[-15:], img)
# # print("DoNe!!")
