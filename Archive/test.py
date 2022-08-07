import cv2 as cv
import numpy as np
from os.path import isfile
from os import pwd
from random import choice
from math import acos, degrees, sqrt
# from lib import path, picDirec
from lib import fill, interest_points, newCoordinate, drawPerspectiveFloor
from os import listdir, getcwd, chdir, mkdir
from random import randint


# def choosePoint(points):
#     p1, p2 = points
#     p1 = tuple(reversed(p1))
#     p2 = tuple(reversed(p2))
#     # return choice(points[0])
#     x = int((p1[0] + p2[0])/2)
#     y = int((p1[1] + p2[1])/2)
#     h = old_dim[0]/2
#     if y < h//2:
#         if p1[1] >= h:
#             return p1
#         return p2
#     return (x, y)


# def drawPerspectiveFloor(dim=(720, 1080, 3)):
#     blank = np.zeros(dim, np.uint8)
#     h, w = blank.shape[:2]
#     center = b_point = [72, 540]
#     ribs = dim[0]//2 - center[0]
#     previous_angle = 0
#     colum_angle_range = {}
#     horizen_range = {}
#     fbw = dim[1]//18
#     lbw = dim[1]//14
#     # fbw = 60
#     # lbw = 75
#     # h += 100
#     # Midlle:
#     cv.line(blank, (w//2, h//2), (w//2, h), (0, 0, 255), 1)
#     # Horizen:
#     last = 0
#     adt = 0
#     bg_range = h//2
#     cv.line(blank, (0, h//2+last+adt), (w, h//2+last+adt), (0, 0, 255), 1)
#     # 15
#     for index in range(0, 17):
#         last += 6
#         end_range = h//2+last+adt
#         if end_range >= h:
#             horizen_range[chr(65+index)] = [bg_range, h-1]
#             break
#         else:
#             horizen_range[chr(65+index)] = [bg_range, end_range-1]

#         cv.line(blank, (0, end_range), (w, end_range), (0, 255, 0), 1)
#         bg_range = end_range
#         last += adt
#         adt += 2

#     # Right + Left:
#     for index in range(1, 25):
#         # fbw = 60 / lbw = 75
#         try:
#             # 50*index
#             cv.line(blank,  (w//2 + fbw*index, h//2),
#                     (w//2 + fbw*index + lbw*index, h), (0, 255, 0), 1)
#             # cv.line(blank,  (w//2 + fbw*index, h//2),
#             #         (w//2 + fbw*index - lbw*index, 0), (255, 0, 0), 1)
#             cv.line(blank,  (w//2 - fbw*index, h//2),
#                     (w//2 - fbw*index - lbw*index, h), (0, 255, 0), 1)
#             # cv.line(blank,  (w//2 - fbw*index, h//2),
#             #         (w//2 - fbw*index + lbw*index, 0), (0, 255, 0), 1)

#             base = fbw*index
#             # ribs = dim[0] - center[0]
#             # base = fbw*index
#             tire = sqrt(ribs**2+base**2)
#             curent_angle = degrees(acos(ribs/tire))
#             colum_angle_range[str(index)] = [previous_angle, curent_angle]
#             previous_angle = curent_angle
#         except:
#             print("except")
#         if w//2 + fbw*index >= w:
#             break
#     cv.imshow('Scene', blank)
#     cv.waitKey()
#     cv.destroyAllWindows()
#     # cv.imwrite('horizontal lines.png', blank)
#     # cv.line(blank, (0, h*3//4), (w-1, h*3//4), (0, 0, 255), 1)
#     return blank, horizen_range, colum_angle_range
# /////////////////////////////////////////////////////////////////////////////////////////

# path = r'M:\Documents\Projects\End Of Study\End of Study Project\scripts\GaitDatasetB-silh\001\bg-01\000\001-bg-01-000-001.png'

# img = cv.imread(path)
# old_dim = img.shape[:2]
# new_dim = (720, 1080)
# new_dim = old_dim
# floor = drawPerspectiveFloor()[0]
# points = interest_points(img)
# point_1 = points[0][0]
# # point_2 = points[0][1]
# # point = choosePoint((point_1, point_2))

# cv.circle(img, tuple(reversed(point_1)), 5, (0, 255, 0), -1)
# # cv.circle(img, tuple(reversed(point_2)), 5, (255, 0, 0), -1)
# # cv.circle(img, point, 5, (255, 0, 255), -1)
# # cv.imshow('test', img)
# # cv.waitKey()
# # cv.destroyAllWindows()


# img = cv.resize(img, tuple(reversed(new_dim)))
# point_1 = newCoordinate(tuple(reversed(point_1)), old_dim, new_dim)
# # point_2 = newCoordinate(points[0][1], old_dim, new_dim)
# # point = choosePoint((point_1, point_2))

# # All points:
# # cv.circle(img, point_1, 5, (255, 0, 255), -1)
# # cv.circle(img, tuple(
# # reversed(point_1)), 5, (0, 255, 0), -1)
# # cv.circle(img, tuple(
# #     reversed(point_2)), 5, (255, 0, 0), -1)
# # cv.circle(second_image, tuple(
# #     reversed(second_points[0])), 5, (0, 255, 0), -1)
# # cv.circle(second_image, tuple(
# #     reversed(second_points[1])), 5, (255, 0, 0), -1)
# # Chosen point:
# # cv.circle(img, point, 5, (255, 0, 255), -1)
# # cv.circle(second_image, point_2, 5, (255, 0, 255), -1)

# img = cv.bitwise_or(img, floor)

# cv.imshow('test', img)
# cv.waitKey()
# cv.destroyAllWindows()


# scene = drawPerspectiveFloor()

# path1 = r'GaitDatasetB-silh\001\nm-01\000\001-nm-01-000-001.png'
# path2 = r'GaitDatasetB-silh\001\nm-01\000\001-nm-01-000-096.png'

# img1 = cv.imread(path1)
# img2 = cv.imread(path2)

# img1 = cv.resize(img1, (1080, 720))
# img2 = cv.resize(img2, (1080, 720))

# img = cv.bitwise_xor(img1, img2)
# cv.imshow('Xor Scene', img)
# cv.waitKey()
# cv.destroyAllWindows()

print(pwd())