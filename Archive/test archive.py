import cv2 as cv
import numpy as np
import winsound
from lib import *
from os import listdir, system, getcwd, chdir
# from os import listdir, system, fork, _exit, getpid
from os.path import abspath, isfile
from pathlib import Path
from time import time, sleep
from random import random, randint
import matplotlib.pyplot as plt
from math import acos, degrees, sqrt

# h == 72 / w == 540
# print(abspath(__file__))

# duration = 1000  # milliseconds
# freq = 500  # Hz
# winsound.Beep(freq, duration)

# # path = Path(r"script\images\walk6.jpg")
# # print(type(Path(__file__).parent.absolute()))

# walkers = []
# # walker = cv.imread(r"images\walk1.jpg")
# walker = cv.imread(r"images\blender.jpeg")
# cv.imshow('Walker', resImg(walker, dim=600))
# # for pic in os.listdir(r"script\images"):
# #     walkers.append(pic)


# gray = cv.cvtColor(walker, cv.COLOR_BGR2GRAY)
# # cv.imshow('Gray Walker', resImg(gray, dim=600))


# # Blur:
# blurred = cv.GaussianBlur(walker, (5, 5), 0)
# cv.imshow('Blurred Walker', resImg(blurred, dim=600))

# # blurred = cv.medianBlur(walker, 5)
# # cv.imshow('Median Blurred Walker', resImg(blurred, dim=600))


# # # laplacion_edge:
# # edges = cv.Laplacian(gray, cv.CV_64F)
# # edges = np.uint8(np.absolute(edges))
# # cv.imshow('Lap Edge', resImg(edges, dim=500))

# # # Canny:
# # edges = cv.Canny(blurred, 150, 175)
# # cv.imshow('Canny Edges', resImg(edges, dim=500))

# # blurred_float = blurred.astype(np.float32) / 255.0
# # edgeDetector = cv.ximgproc.createStructuredEdgeDetection("model.yml")
# # edges = edgeDetector.detectEdges(blurred_float) * 255.0
# # cv.imwrite('edge-raw.jpg', edges)

# #######################################################

# blurred_float = blurred.astype(np.float32) / 255.0
# edgeDetector = cv.ximgproc.createStructuredEdgeDetection("model.yml")
# edges = edgeDetector.detectEdges(blurred_float) * 255.0
# cv.imwrite('edge-raw.jpg', edges)


# def SaltPepperNoise(edgeImg):
#     count = 0
#     lastMedian = edgeImg
#     median = cv.medianBlur(edgeImg, 3)
#     while not np.array_equal(lastMedian, median):
#         zeroed = np.invert(np.logical_and(median, edgeImg))
#         edgeImg[zeroed] = 0
#         count = count + 1
#         if count > 70:
#             break
#         lastMedian = median
#         median = cv.medianBlur(edgeImg, 3)


# edges_u = np.asarray(edges, np.uint8)
# SaltPepperNoise(edges_u)

# cv.imshow('edge.jpg', resImg(edges_u, dim=600))
# # cv.imwrite('edge.jpg', edges_)
# # image_display('edge.jpg')
# # edge = cv.imread('edge.jpg')
# # cv.imshow('Edges', resImg(edge, dim=600))


# #######################################################


# mask = np.zeros_like(edges_u)
# cv.fillPoly(mask, [contour], 255)
# # calculate sure foreground area by dilating the mask
# mapFg = cv.erode(mask, np.ones((5, 5), np.uint8), iterations=10)
# # mark inital mask as "probably background"
# # and mapFg as sure foreground
# trimap = np.copy(mask)
# trimap[mask == 0] = cv.GC_BGD
# trimap[mask == 255] = cv.GC_PR_BGD
# trimap[mapFg == 255] = cv.GC_FGD
# # visualize trimap
# trimap_print = np.copy(trimap)
# trimap_print[trimap_print == cv.GC_PR_BGD] = 128
# trimap_print[trimap_print == cv.GC_FGD] = 255

# cv.imshow('trimap_print', resImg(trimap_print, dim=500))
# # cv.imwrite('trimap.png', trimap_print)
# # image_display('trimap.png')

# #######################################################
# capture = cv.VideoCapture("videos/people 2.mp4")
# # capture variable is an instance of this VideoCapture class
# frames = 0
# f_before = 0

# while True:
#     isTrue, frame = capture.read()
#     frames += 1
#     f_after = time()
#     # print(f"fps: {1/(f_after-f_before)} ")
#     f_before = time()
#     # frame  : is a frame from the video
#     # isTrue : a boolean it says whether the frame was successfully ready or not
#     if not isTrue:
#         break

#     # if cv.waitKey(30) & 0xFF == ord('q'):
#     #     # cv.waitKey(n): here the n represent how much time
#     #     # the frame will be displayed in milliseconde
#     #     break


# print(f"There is : {frames} Frame ")

# capture.release()  # release capture pointer
# cv.destroyAllWindows()


# # cv.waitKey(0)
# # cv.destroyAllWindows()


#######################################################


# # initialize the HOG descriptor/person detector
# hog = cv.HOGDescriptor()
# hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())

# cv.startWindowThread()
# name = "images/walk3.jpg"
# frame = cv.imread(name)
# h, w = frame.shape[:2]

# # frame = cv.GaussianBlur(frame, (5, 5), 7)
# # # resizing for faster detection
# frame = cv.resize(frame, (600, int(600 * h/w)))
# # # using a greyscale picture, also for faster detection
# gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)

# boxes, weights = hog.detectMultiScale(gray, winStride=(8, 8))

# print(boxes)
# print(type(boxes))
# print("*"*30)
# # detect people in the image
# # returns the bounding boxes for the detected objects
# boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

# print(boxes)
# print(type(boxes))


# for (xA, yA, xB, yB) in boxes:
#     # display the detected boxes in the colour picture
#     roi = frame[yA:yB, xA:xB]
#     # cv.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)
#     # roi = frame[xA:yA, xA + xB:yA + yB]
#     # cv.rectangle(frame, (xA, yA), (xB, yB),(0, 255, 0), 2)
#     # cv.rectangle(frame, (xA, yA), (xA + xB, yA + yB),(0, 255, 0), 2)


# ret, thresh = cv.threshold(cv.cvtColor(
#     roi, cv.COLOR_RGB2GRAY), 127, 255, cv.THRESH_BINARY)
# # adaptive_thresh
# # thresh = cv.adaptiveThreshold(
# #     cv.cvtColor(roi, cv.COLOR_RGB2GRAY), 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)

# # cv.imshow("ROI", resImg(roi, dim=600))
# cv.imshow("ROI", thresh)
# cv.imshow("Frame", resImg(frame))


# print("DONE!!")
# # finally, close the window
# cv.waitKey()
# cv.destroyAllWindows()

#######################################################

# print(abspath(__file__))
# for i in range(5):
#     print(random())
#     print(randint(0,2))
#     print()

#######################################################

# img = np.zeros((500,300,3), np.uint8)
# cv.rectangle(img, (0,50), (50,100),(255), 2)

# # # Draw a Cercle
# # h, w = blank_image.shape[:2]
# cv.circle(img, (250,400), 20, (255), -1)

# cv.imshow("img", img)
# cv.waitKey()
# cv.destroyAllWindows()

#######################################################

# def nearestAngle(angle):
#     difference = []
#     # return min(abs(angle-0),
#     #            abs(angle-45),
#     #            abs(angle-90)
#     #            )
#     difference.append(abs(angle-0))
#     difference.append(abs(angle-45))
#     difference.append(abs(angle-90))
#     return angles[difference.index(min(difference))]


# angles = [0, 45, 90]
# print("Nearest Angle for {} is {}".format(45, nearestAngle(45)))
# print("Nearest Angle for {} is {}".format(43, nearestAngle(43)))
# print("Nearest Angle for {} is {}".format(1, nearestAngle(1)))
# print("Nearest Angle for {} is {}".format(0, nearestAngle(0)))
# print("Nearest Angle for {} is {}".format(80, nearestAngle(80)))
# print("Nearest Angle for {} is {}".format(70, nearestAngle(70)))
# print("Nearest Angle for {} is {}".format(34, nearestAngle(34)))


#######################################################
#######################################################
# from math import acos, cos, sqrt, degrees

# # print(cos(45))
# # print(acos(0.5))
# # print(acos(cos(45)))

# print(degrees(acos(2/sqrt(8))))
#######################################################

# test = [
#     [0, 3, 6, 9],
#     [1, 4, 7, 10],
#     [2, 5, 8, 11]
# ]

# for j in range(0, len(test[0])):
#     for i in range(0, len(test)):
#         print(test[i][j])
#######################################################
#######################################################

# time1 = time()
# # hna rana nahakmo point lowel lfo9 well taht
# # bch n3rfo lmayll wzid na3arfoo asq raw y9areb ella yrooh
# # paths = [
# #     "GaitDatasetA-silh/nhz/00_2/nhz-00_2-001.png",
# #     "GaitDatasetA-silh/nhz/00_2/nhz-00_2-060.png"
# #     "GaitDatasetA-silh/nhz/45_2/nhz-45_2-001.png",
# #     "GaitDatasetA-silh/nhz/45_2/nhz-45_2-111.png"
# #     "GaitDatasetA-silh/nhz/90_2/nhz-90_2-001.png",
# #     "GaitDatasetA-silh/nhz/90_2/nhz-90_2-097.png"
# # ]
# # paths = [
# #     "GaitDatasetA-silh/nhz/00_2/nhz-00_2-001.png",
# #     "GaitDatasetA-silh/nhz/00_2/nhz-00_2-060.png"
# # ]
# paths = [
#     "GaitDatasetA-silh/nhz/45_2/nhz-45_2-001.png",
#     "GaitDatasetA-silh/nhz/45_2/nhz-45_2-111.png"
# ]
# # paths = [
# #     "GaitDatasetA-silh/nhz/90_2/nhz-90_2-001.png",
# #     "GaitDatasetA-silh/nhz/90_2/nhz-90_2-097.png"
# # ]
# blank = np.zeros((240, 352, 3), np.uint8)
# blank2 = np.zeros((240, 352, 3), np.uint8)
# # img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# # print(len(img))
# # print(len(img[0]))
# # print(img[0, 0])
# # print(img.shape)
# coordinate = []

# for index, image_path in enumerate(paths):
#     img = cv.imread(image_path)
#     cv.imshow(f'original{index}', img)
#     img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#     first_white_pixel = 0
#     last_white_pixel = 0
#     found = False

#     contours = cv.findContours(img, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
#     contours = contours[0] if len(contours) == 2 else contours[1]
#     for c in contours:
#         size = cv.contourArea(c)
#         if size > 1000:
#             cv.drawContours(blank2, [c], -1, (255, 255, 255), 2)
#     img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
#     img = cv.bitwise_and(img, blank2)
#     # cv.imshow('blank2', blank2)

#     height, width = img.shape[:2]
#     for y in range(height):
#         for x in range(width):
#             if img[y][x][0] == 255:
#                 found = True
#                 last_white_pixel = (x, y)
#                 if not first_white_pixel:
#                     first_white_pixel = (x, y)

#     a = first_white_pixel
#     b = last_white_pixel
#     coordinate.append(a)
#     coordinate.append(b)
#     img = cv.circle(img, a, 3, (0, 0, 255), -1)
#     img = cv.circle(img, b, 3, (0, 0, 255), -1)
#     cv.imshow(f"simple{index}", img)

#     blank = cv.bitwise_or(blank, img)

# for index in range(2):
#     blank = cv.line(blank, coordinate[index],
#                     coordinate[index+2], (0, 0, 255), 2)

# cv.imshow('Full', blank)


# # for j in range(0, len(test[0])):
# #     for i in range(0, len(test)):
# #         print(test[i][j])

# print("{:0.3}s".format(time()-time1))
# cv.waitKey()
# cv.destroyAllWindows()
#######################################################
# files = []
# text = "test"
# files = open(text+".txt", "w")

# files.write("test")
# files.write("test2")
# files.writelines("3")
# files.writelines("34")

# files.close()

# test = open("00.txt", "r")
# line = test.readline()
# while line:
#     print(line, end="")
#     line=test.readline()
# test.close()
########################################################
# angles = ["00", "45", "90"]

# for index, angle_file in enumerate(angles):
#     file = open(angle_file+".txt", "r")
#     angle = file.readline()[:-2]
#     min_ang = max_ang = float(angle)
#     average = []
#     while angle:
#         angle = float(angle)
#         average.append(angle)
#         min_ang = min(angle, min_ang)
#         max_ang = max(angle, max_ang)
#         angle = file.readline()
#     print(f">>>>>>>>> {angle_file} <<<<<<<<<")
#     print(f"Min Angle  ==>{min_ang}")
#     print(f"Max Angle  ==>{max_ang}")
#     print(f"Average is ==>{sum(average)/len(average)}")
#     print("*"*30)
#     file.close()
#######################################################
# system('say "your program has finished"')
#######################################################
# with open("abnormal.txt", "r") as abnormal:
#     names = []
#     line = abnormal.readline()[:-1]
#     while line:
#         names.append(line.split('/')[-1])
#         line = abnormal.readline()[:-1]

#     names = sorted(set(names))
#     print(">> Names:")
#     for name in names:
#         print("{:>20}".format(name))
#######################################################
# def child():
#    print('\nA new child ',  getpid())
#    _exit(0)
# def parent():
#    while True:
#       newpid = fork()
#       if newpid == 0:
#          child()
#       else:
#          pids = (getpid(), newpid)
#          print("parent: %d, child: %d\n" % pids)
#       reply = input("q for quit / c for new fork")
#       if reply == 'c':
#           continue
#       else:
#           break

# parent()
#######################################################
# try:
#     print(5/0)
# except:
#     print("hh")
#######################################################
# print("-"*30)
# direc = getcwd()
# print("1", direc)

# chdir("M:\Documents\Projects\End Of Study\End of Study Project\scripts\script")
# print("2", getcwd())

# chdir(direc)
# print("3", getcwd())

# print("-"*30)

#######################################################

# def deepestPoint(img):
#     # img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#     last_pixel = 0, 0
#     height, width = img.shape[:2]
#     for y in range(height):
#         for x in range(width):
#             if img[y][x][0] == img[y][x][1] == img[y][x][2] == 255:
#                 # if img[y][x] == 255:
#                 last_pixel = (x, y)
#     return last_pixel


# img = cv.imread("zc-00_3-001.png")
# img = cv.imread("GaitDatasetA-silh/lsl/90_2/lsl-90_2-086.png")
# print(img.shape, len(img))
# print(img[0][0])
# blank = np.zeros((240, 352, 3), np.uint8)
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# print(gray[0][0])
# # img = cv.bitwise_or(img, gray)
# point = deepestPoint(img)
# print(point)
# cv.circle(img, point, 3, (255), -1)
# cv.imshow("img", img)

# cv.waitKey()
# cv.destroyAllWindows()

#######################################################
# pictures = []
# with open("primary result/abnormal.txt", "r") as file:
#     pic = file.readline()
#     while pic:
#         pictures.append(pic[:-1])
#         pic = file.readline()
# print(pictures)
# print(len(pictures))


# for pic in pictures:
#     img = cv.imread(pic)
#     # no_noise_pic = noiseRemover(img)
#     no_noise_pic = img
#     point = deepestPoint(no_noise_pic)
#     cv.circle(no_noise_pic, point, 3, (255), -1)

#     while True:
#         cv.imshow(pic[-16:-1], no_noise_pic)
#         if cv.waitKey(20) & 0xFF == 110:
#             break
# cv.destroyAllWindows()

#######################################################

# import pyttsx3
# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()

#######################################################
# # How to Copy a File in Python

# import shutil

# original = r'original path where the file is currently stored\file name.file extension'
# target = r'target path where the file will be copied\file name.file extension'

# shutil.copyfile(original, target)
######################################################
# img_test = np.zeros((5,3, 1), np.uint8)
# print(img_test.shape)
# print(img_test)
# print(len(img_test))
# print(len(img_test[0]))
# print(len(img_test[1]))
# print(len(img_test[2]))
# print(len(img_test[3]))
# print(len(img_test[4]))
#######################################################
#######################################################
# blank = np.zeros((3, 5), np.uint8)
# print(blank[0])
# print(blank.shape)
# print(blank)

# for line in range(len(blank)):
#     for colon in range(len(blank[0])):
#         print(blank[line][colon])

#######################################################
# # bluring te3 pic mel sillh
# img = cv.imread('DataSetASamples/zc-00_3-001.png')
# img = cv.resize(img, (1080, 720))
# img2 = cv.GaussianBlur(img, (7, 7), 0)
# result = cv.subtract(img, img2)

# cv.imshow('img', img)
# cv.imshow('img2', img2)
# cv.imshow('result', result)


# cv.waitKey()
# cv.destroyAllWindows()
#######################################################
# # habit nsayi ze3ma bch nkhyyr ana kima nhab 9falli
# img = cv.imread('DataSetASamples/zc-00_3-001.png')
# cv.imshow('img', img)

# while cv.waitKey():
#     if 0xFF == 115:
#         print('it is s')
#     if 0xFF == 110:
#         print('it is n')

# cv.destroyAllWindows()
#######################################################
# def drawPerspectiveFloor(dim=(720, 1080, 3)):
#     blank = np.zeros(dim, np.uint8)
#     h, w = blank.shape[:2]
#     fbw = 60
#     lbw = 75
#     # h += 100
#     # Midlle:
#     cv.line(blank, (w//2, h//2), (w//2, h), (0, 0, 255), 1)
#     # Right:
#     for index in range(1, 25):
#         try:
#             #
#             cv.line(blank,  (w//2 + fbw*index, h//2),
#                     (w//2 + fbw*index + lbw*index, h), (0, 255, 0), 1)
#             cv.line(blank,  (w//2 + fbw*index, h//2),
#                     (w//2 + fbw*index - lbw*index, 0), (255, 0, 0), 1)
#         except:
#             print("except")
#     # Left:
#     for index in range(1, 25):
#         try:
#             cv.line(blank,  (w//2 - fbw*index, h//2),
#                     (w//2 - fbw*index - lbw*index, h), (0, 255, 0), 1)
#             cv.line(blank,  (w//2 - fbw*index, h//2),
#                     (w//2 - fbw*index + lbw*index, 0), (0, 255, 0), 1)
#         except:
#             print("except")
#     # Horizen:
#     last = 0
#     adt = 0
#     cv.line(blank, (0, h//2+last+adt), (w, h//2+last+adt), (0, 0, 255), 1)
#     for index in range(0, 220):
#         last += 7
#         cv.line(blank, (0, h//2+last+adt), (w, h//2+last+adt), (0, 255, 0), 1)
#         last = last+adt
#         adt += 1
#     return blank


# img_1 = cv.imread('DataSetASamples/zc-00_3-001.png')
# img_2 = cv.imread('DataSetASamples/zc-00_3-044.png')
# floor = drawPerspectiveFloor((720, 1080, 3))
# img_1 = cv.resize(img_1, (1080, 720))
# scene = cv.bitwise_or(img_1, floor)
# scene[72][540] = [255,255,255]
# ROI = scene[69:77,530:550] # h == 72 / w == 540
# plt.imshow(ROI)
# # plt.imshow(scene)
# plt.show()
# print("hh")
#######################################################
# img = cv.imread('DataSetASamples/zc-00_3-001.png')
# h,w = img.shape[:2]
# print(img[h-1][w-1])


#######################################################
#
# def drawPerspectiveFloor(dim=(720, 1080, 3)):
#     blank = np.zeros(dim, np.uint8)
#     h, w = blank.shape[:2]
#     center = b_point = [72, 540]
#     ribs = dim[0]//2 - center[0]
#     previous_angle = 0
#     colum_angle_range = {}
#     horizen_range = {}
#     fbw = 60
#     lbw = 75
#     # h += 100
#     # Horizen:
#     last = 0
#     adt = 0
#     cv.line(blank, (0, h//2+last+adt), (w, h//2+last+adt), (0, 0, 255), 1)
#     bg_range = h//2
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
#         last = last+adt
#         adt += 2

#     # Midlle:
#     cv.line(blank, (w//2, h//2), (w//2, h), (0, 0, 255), 1)

#     # Right + Left:
#     for index in range(1, 25):
#         # fbw = 60
#         # lbw = 75
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

#     return blank, horizen_range, colum_angle_range


# def deepestPoint(img):
#     # img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#     last_pixel = 0, 0
#     height, width = img.shape[:2]
#     for y in range(height):
#         for x in range(width):
#             if img[y][x][0] == img[y][x][1] == img[y][x][2] == 255:
#                 # if img[y][x] == 255:
#                 last_pixel = (x, y)
#     return last_pixel


# def rangeLocation(horizen_range, point):
#     x = point[0]
#     for horizen, horizen_range in horizen_range.items():
#         if x in range(*horizen_range):
#             return horizen
#     else:
#         return False


# def pickHorizen(horizen_range, occupied_ranges, img):
#     horizen_range2 = horizen_range
#     occupied_ranges = [[horizen, pixels]
#                        for horizen, pixels in occupied_ranges.items()]
#     horizen_range = [[horizen, hrz_rng]
#                      for horizen, hrz_rng in horizen_range.items()]
#     last_pixel = deepestPoint(img)
#     last_pixel_horizen = rangeLocation(horizen_range2, last_pixel)
#     last_horizen_range = horizen_range[-1][-1]
#     pixel_deep_in_horizen = last_pixel[0]-last_horizen_range[0]
#     last_horizen_range2 = last_horizen_range
#     last_horizen_range = last_horizen_range[1] - last_horizen_range[0]

#     # if occupied_ranges[-1][-1] >= (1/3)*horizen_range.get(occupied_ranges[-1][0]):
#     # if occupied_ranges[-1][0] == 'A' or occupied_ranges[-1][-1] >= (1/3)*(horizen_range.get(occupied_ranges[-1][0])[1]-horizen_range.get(occupied_ranges[-1][0])[0]):
#     if occupied_ranges[-1][0] == 'A' or pixel_deep_in_horizen >= (1/3)*last_horizen_range:
#         print('>> occupied_ranges:\n', occupied_ranges)
#         print('>> horizen_range:\n', horizen_range)
#         print('>> last_pixel:\n', last_pixel)
#         print('>> last_pixel_horizen:\n', last_pixel_horizen)
#         print('>> last_horizen_range:\n', last_horizen_range2)
#         print('>> pixel_deep_in_horizen:\n', pixel_deep_in_horizen)
#         print()
#         return occupied_ranges[-1][0]
#     # elif len(occupied_ranges)>=2:
#     else:
#         print("else")
#         return occupied_ranges[-2][0]
#     # else:
#     #     pass


# def equalColors(color_1, color_2):
#     for index in range(3):
#         if int(color_1[index]) != int(color_2[index]):
#             return False
#     return True
#     # if color_1[0] == color_1[1] == color_1[2] == 255:
#     #     colors_set.append(list(color_1))
#     # return color_1 == color_2


# # colors_set = []
# floor, horizen_range = drawPerspectiveFloor()[:2]
# h, w = floor.shape[:2]
# cv.rectangle(floor, (w//2, h//2+50), (w//4*3, h//2+80-12), (255, 255, 255), -1)
# ranges = [area_range for area_range in horizen_range.items()]
# print(len(ranges))
# print(ranges, '\n')

# horizen_range_occupied = {}

# for horizen, hrz_rng in horizen_range.items():
#     print(horizen, hrz_rng)
#     # break


# for horizen, hrz_rng in horizen_range.items():
#     for line in range(*hrz_rng):
#         for colon in range(w):
#             if all(floor[line][colon]):
#                 # if equalColors(floor[line][colon], [255, 255, 255]):
#                 horizen_range_occupied[horizen] = horizen_range_occupied.get(
#                     horizen, 0) + 1


# # print(colors_set)
# print(horizen_range_occupied.items())
# for horizen, occupied_pixels in horizen_range_occupied.items():
#     print(f"{horizen} ==> {occupied_pixels} Pixel")

# print("*"*30)
# print(pickHorizen(horizen_range, horizen_range_occupied, floor))

# cv.imshow("floor", floor)
# cv.waitKey()
# cv.destroyAllWindows()


# #######################################################
# sampels = [
#     "GaitDatasetA-silh/zc/90_3/zc-90_3-080.png",
#     "GaitDatasetA-silh/zl/00_4/zl-00_4-008.png",
#     "GaitDatasetA-silh/zl/00_4/zl-00_4-031.png",
#     "GaitDatasetA-silh/zl/00_4/zl-00_4-044.png",
#     "GaitDatasetA-silh/xxj/45_3/xxj-45_3-021.png",
#     "GaitDatasetA-silh/yjf/90_4/yjf-90_4-001.png",
#     "GaitDatasetA-silh/yjf/90_4/yjf-90_4-044.png",
#     "GaitDatasetA-silh/yjf/90_4/yjf-90_4-047.png"
# ]


# def findSignificantContour(edgeImg):
#     contours, hierarchy = cv.findContours(
#         edgeImg,
#         cv.RETR_TREE,
#         cv.CHAIN_APPROX_SIMPLE
#     )
#     # Find level 1 contours
#     level1Meta = []
#     for contourIndex, tupl in enumerate(hierarchy[0]):
#         # Filter the ones without parent
#         if tupl[3] == -1:
#             tupl = np.insert(tupl.copy(), 0, [contourIndex])
#             level1Meta.append(tupl)
# # From among them, find the contours with large surface area.
#     contoursWithArea = []
#     for tupl in level1Meta:
#         contourIndex = tupl[0]
#         contour = contours[contourIndex]
#         area = cv.contourArea(contour)
#         contoursWithArea.append([contour, area, contourIndex])

#     contoursWithArea.sort(key=lambda meta: meta[1], reverse=True)
#     largestContour = contoursWithArea[0][0]
#     return largestContour


# for sample in sampels:
#     img = cv.imread(sample)
#     img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#     canny = cv.Canny(img, 125, 175)
#     Contours, hierarchies = cv.findContours(
#         canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
#     blank = np.zeros(img.shape, dtype='uint8')
#     cv.drawContours(blank, Contours, 0,
#                     (0, 255, 0), 2, cv.LINE_AA, maxLevel=1)
#     cv.imshow('Sample Pic', img)
#     cv.imshow('Contour result', blank)

#     # contour = findSignificantContour(img)
#     # # Draw the contour on the original image
#     # contourImg = np.copy(contour)
#     # cv.drawContours(contourImg, [contour], 0,
#     #                 (0, 255, 0), 2, cv.LINE_AA, maxLevel=1)

#     # cv.imshow('Sample Pic', contourImg)
#     # cv.imshow('Contour result', contourImg)

#     # cv.imwrite('contour.jpg', contourImg)
#     # image_display('contour.jpg')
#     if cv.waitKey(20) & 0xFF == 110:
#         continue

# cv.destroyAllWindows()

#######################################################
# # in order to split the ranges into 4 main areas
# # def mainAreas(img):
# #     h, w = img.shape[:2]
# #     # 'N': [ (w//2, h//2), (w-1, int(h*(3/4))-1) ],
# #     main_area = {
# #         'N': [(w//2, h//2),         (w-1,    h//2+h//4-1)],
# #         'E': [(w//2, h//2+h//4),    (w-1,    h-1)],
# #         'S': [(0,    h//2+h//4),    (w//2-1, h-1)],
# #         'W': [(0,    h//2),         (w//2-1, h//2+h//4-1)]
# #     }

# img = np.zeros((720, 1080, 3), np.uint8)
# h, w = img.shape[:2]
# main_area = {
#     'N': [(w//2, h//2),         (w-1,    h//2+h//4-1)],
#     'E': [(w//2, h//2+h//4),    (w-1,    h-1)],
#     'S': [(0,    h//2+h//4),    (w//2-1, h-1)],
#     'W': [(0,    h//2),         (w//2-1, h//2+h//4-1)]
# }
# colors = [
#     (255, 255, 255),
#     (255, 0, 0),
#     (0, 255, 0),
#     (0, 0, 255)
# ]

# for index, coord in enumerate(main_area.values()):
#     cv.rectangle(img, coord[0], coord[1], colors[index], -1)

# cv.imshow('Areas', img)
# cv.waitKey()
# cv.destroyAllWindows()
#######################################################

# def test():
#     global y
#     y = 9
#     x = 6


# x, y = 1, 2
# print(x,y)
# test()
# print(x,y)

# def test2():
#     global teh
#     teh = [97]
#     teh2 = [96]

# teh = []
# teh2 = []
# print(">> 1 ", teh)
# print(">> 2 ", teh2)
# test2()
# print(">> 1 ", teh)
# print(">> 2 ", teh2)
#######################################################
#######################################################
# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except IOError as (errno, strerror):
#     print "I/O error({0}): {1}".format(errno, strerror)
# except ValueError:
#     print "Could not convert data to an integer."
# except:
#     print "Unexpected error:", sys.exc_info()[0]
#     raise
# #######################################################
# import traceback
# import logging

# try:
#     whatever()
# except Exception as e:
#     logging.error(traceback.format_exc())
#     # Logs the error appropriately.

# #######################################################
# try:
#     something()
# except BaseException as error:
#     print('An exception occurred: {}'.format(error))
# #######################################################
# try:
#     a = 2/0
# except Exception as e:
#     print e.__doc__
#     print e.message
#######################################################
# try:
#     print("Performing an action which may throw an exception.")
# except Exception, error:
#     print("An exception was thrown!")
#     print(str(error))
# else:
#     print("Everything looks great!")
# finally:
#     print()


#######################################################
#######################################################
#######################################################
# def picDirec(path):
#     direc = path.split("/")
#     return "/".join(direc[:-1])


# def path(*paths):
#     return "/".join(paths)


# def drawPerspectiveFloor(dim=(720, 1080, 3)):
#     blank = np.zeros(dim, np.uint8)
#     h, w = blank.shape[:2]
#     center = b_point = [72, 540]
#     ribs = dim[0]//2 - center[0]
#     previous_angle = 0
#     angle_range = {}
#     horizen_range = {}
#     fbw = 60
#     lbw = 75
#     # h += 100
#     # Horizen:
#     last = 0
#     adt = 0
#     cv.line(blank, (0, h//2+last+adt), (w, h//2+last+adt), (0, 0, 255), 1)
#     bg_range = h//2
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
#         last = last+adt
#         adt += 2

#     # Midlle:
#     cv.line(blank, (w//2, h//2), (w//2, h), (0, 0, 255), 1)

#     # Right + Left:
#     for index in range(1, 25):
#         # fbw = 60
#         # lbw = 75
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
#             angle_range[str(index)] = [previous_angle, curent_angle]
#             previous_angle = curent_angle
#         except:
#             print("except")

#     return blank, horizen_range, angle_range


# def deepestPoint(img):
#     # img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#     last_pixel = 0, 0
#     height, width = img.shape[:2]
#     for y in range(height):
#         for x in range(width):
#             if img[y][x][0] == img[y][x][1] == img[y][x][2] == 255:
#                 # if img[y][x] == 255:
#                 last_pixel = (x, y)
#     cv.circle(img, last_pixel, 2, (255, 0, 0), -1)
#     # cv.circle(img, (last_pixel[1], last_pixel[0]), 2, (0,0,255), -1)
#     return last_pixel


# def rangeLocation(point, horizen_range):
#     y = point[1]
#     for horizen, horizen_range in horizen_range.items():
#         if y in range(horizen_range[0], horizen_range[1]+1):
#             return horizen
#     else:
#         return False


# def angleLocation(point, angle_range, dim=(720, 1080), center=(72, 540)):
#     # Mode line, column
#     ribs = point[0] - center[0]
#     base = abs(center[1] - point[1])
#     tire = sqrt(ribs**2+base**2)
#     angle = degrees(acos(ribs/tire))

#     for column, angle_rng in angle_range.items():
#         if angle_rng[0] < angle <= angle_rng[1]:
#             return column
#     print("*"*20)
#     print('ribs', ribs)
#     print('base', base)
#     print('tire', tire)
#     print('angle', angle)
#     return False


# def pickAngle(angle_range, occupied_angles, img):
#     pass


# def pickHorizen(horizen_range, occupied_ranges, img):
#     horizen_range2 = horizen_range
#     horizen_range = [[horizen, hrz_rng]
#                      for horizen, hrz_rng in horizen_range.items()]
#     # [['A',[360,366]], ['B',[365,375]], ['C',[376,366]]]
#     occupied_ranges = [[horizen, pixels]
#                        for horizen, pixels in occupied_ranges.items()]
#     # [['A',xxx_1], ['B',xxx_2], ['C',xxx_3]]
#     last_pixel = deepestPoint(img)
#     last_pixel_horizen = rangeLocation(last_pixel, horizen_range2)

#     last_occupied_horizen_range = horizen_range2[last_pixel_horizen]
#     pixel_deep_in_horizen = last_pixel[1]-last_occupied_horizen_range[0]
#     last_occupied_horizen_range2 = last_occupied_horizen_range
#     last_occupied_horizen_range = last_occupied_horizen_range[1] - \
#         last_occupied_horizen_range[0]

#     # if occupied_ranges[-1][-1] >= (1/3)*horizen_range.get(occupied_ranges[-1][0]):
#     # if occupied_ranges[-1][0] == 'A' or occupied_ranges[-1][-1] >= (1/3)*(horizen_range.get(occupied_ranges[-1][0])[1]-horizen_range.get(occupied_ranges[-1][0])[0]):
#     print('>> horizen_range:\n', horizen_range)
#     print('>> occupied_ranges:\n', occupied_ranges)
#     print('>> last_pixel:\n', last_pixel)
#     print('>> last_pixel_horizen:\n', last_pixel_horizen)
#     print('>> last_horizen_range:\n', last_occupied_horizen_range)
#     print('>> pixel_deep_in_horizen:\n', pixel_deep_in_horizen)
#     print()
#     if occupied_ranges[-1][0] == 'A' or pixel_deep_in_horizen >= (1/3)*last_occupied_horizen_range:
#         # return last_pixel_horizen
#         return occupied_ranges[-1][0]
#     # elif len(occupied_ranges)>=2:
#     else:
#         print("else")
#         return occupied_ranges[-2][0]
#     # else:
#     #     pass


# def equalColors(color_1, color_2):
#     for index in range(3):
#         if int(color_1[index]) != int(color_2[index]):
#             return False
#     return True
#     # if color_1[0] == color_1[1] == color_1[2] == 255:
#     #     colors_set.append(list(color_1))
#     # return color_1 == color_2


# #############################################################################################
# # initialization
# # colors_set = []
# direc = "GaitDatasetB-silh"
# while not isfile(direc):
#     direc = path(direc, choice(listdir(direc)))
# direc = picDirec(direc)
# picture = listdir(direc)[0]
# picture = cv.imread(path(direc, picture))
# picture = cv. resize(picture, (1080, 720))


# floor, horizen_range, angel_range = drawPerspectiveFloor()[:3]
# h, w = floor.shape[:2]
# floor = cv.bitwise_or(floor, picture)
# # cv.rectangle(floor, (w//2, h//2+40), (w//4*3, h//2+80), (255, 255, 255), -1)
# horizen_range_occupied = {}
# angle_range_occupied = {}


# # angel_range
# # {
# #     '1':  [0, 11.768288932020628],                   '2': [11.768288932020628,22.61986494804042],
# #     '3':  [22.61986494804042, 32.0053832080835],     '4': [32.0053832080835,  39.80557109226519],
# #     '5':  [39.80557109226519, 46.16913932790742],    '6': [46.16913932790742, 51.34019174590991],
# #     '7':  [51.34019174590991, 55.56101069119639],    '8': [55.56101069119639, 59.03624346792648],
# #     '9':  [59.03624346792648, 61.92751306414704],   '10': [61.92751306414704, 64.35899417569472],
# #     '11': [64.35899417569472, 66.42529379808738],   '12': [66.42529379808738, 68.19859051364818],
# #     '13': [68.19859051364818, 69.7343025290525],    '14': [69.7343025290525,  71.07535558394876],
# #     '15': [71.07535558394876, 72.25532837494306],   '16': [72.25532837494306, 73.30075576600639],
# #     '17': [73.30075576600639, 74.23281745752432],   '18': [74.23281745752432, 75.06858282186246],
# #     '19': [75.06858282186246, 75.8219355852931],    '20': [75.8219355852931,  76.5042667192042],
# #     '21': [76.5042667192042 , 77.12499844038753],   '22': [77.12499844038753, 77.69198418257209],
# #     '23': [77.69198418257209, 78.21181670089238],   '24': [78.21181670089238, 78.69006752597979]
# # }

# # ranges = [area_range for area_range in horizen_range.items()]
# ranges = [
#     ('A', [360, 365]), ('B', [366, 373]), ('C', [374, 383]),
#     ('D', [384, 395]), ('E', [396, 409]), ('F', [410, 425]),
#     ('G', [426, 443]), ('H', [444, 463]), ('I', [464, 485]),
#     ('J', [486, 509]), ('K', [510, 535]), ('L', [536, 563]),
#     ('M', [564, 593]), ('N', [594, 625]), ('O', [626, 659]),
#     ('P', [660, 695]), ('Q', [696, 719])]


# # Printing horizens and it's ranges:
# for horizen, hrz_rng in horizen_range.items():
#     print(horizen, hrz_rng)
#     # break

# # calculating how many pixel in every horizen
# for horizen, hrz_rng in horizen_range.items():
#     for line in range(hrz_rng[0], hrz_rng[1]+1):
#         for column in range(w//2, w):
#             if all(floor[line][column]):
#                 # if equalColors(floor[line][colon], [255, 255, 255]):
#                 horizen_range_occupied[horizen] = horizen_range_occupied.get(
#                     horizen, 0) + 1

# # print(colors_set)
# # Printing occupied pixels in every Horizens
# print(horizen_range_occupied.items())
# for horizen, occupied_pixels in horizen_range_occupied.items():
#     print(f"{horizen} ==> {occupied_pixels} Pixel")

# print("*"*30)
# # printing the choosen horizen:
# picked_horizen = pickHorizen(horizen_range, horizen_range_occupied, floor)
# print("the horizen Picked is ==>", picked_horizen)


# print("*"*30)
# # calculating how many pixel in every angle
# picked_range = horizen_range[picked_horizen]

# for line in range(picked_range[0], picked_range[1]+1):
#     for column in range(w//2+20, w):
#         if all(floor[line][column]):
#             # print("lol")
#             point_angle = angleLocation((line, column), angel_range)
#             if column < w//2:
#                 point_angle = "-"+point_angle
#                 # angle_range_occupied["-"+point_angle] = angle_range_occupied.get(
#                 #     "-"+point_angle, 0)+1
#             else:
#                 point_angle = "+"+point_angle
#                 # angle_range_occupied["-"+point_angle] = angle_range_occupied.get(
#                 #     "-"+point_angle, 0)+1
#             angle_range_occupied[point_angle] = angle_range_occupied.get(
#                 point_angle, 0)+1

# print(angle_range_occupied)
# for column, pixels in angle_range_occupied.items():
#     print(f"{column} ==> {pixels} Pixel")

# img = listdir(direc)[-1]
# picture = cv.imread(path(direc, img))
# picture = cv. resize(picture, (1080, 720))
# floor = cv.bitwise_or(floor, picture)
# cv.imshow(img, floor)
# cv.waitKey()
# cv.destroyAllWindows()
######################################################
#######################################################
#######################################################
#######################################################
#######################################################

# chdir(r'C:\Users\Mii_Ranna\Desktop')
# mkdir(getcwd()+'/test/test2/ttt/ssss')

# import traceback
# import logging
# try:
#     int('s')
# except Exception as e:
#     logging.error(traceback.format_exc())
#     # Logs the error appropriately.
#     print('hh')

# try:
#     int('s')
# except Exception as error:
#     # print('An exception occurred: {}'.format(error))
#     print('hh')

####################################################################
# def putInfo(img, p1, p2, cp1, cp2, dh, dc, angle):
#     h,w = img.shape[:2]
#     color = (255, 0, 255)
#     font = cv.FONT_HERSHEY_PLAIN
#     fontscale = 2
#     thickness = 2
#     p1r, p1l = p1
#     p2r, p2l = p2

#     cv.putText(img, f"{str(p1l)}-{str(p1r)} | {cp1} H\C",
#                (10, 30), font, fontscale, color, thickness)
#     cv.putText(img, f"{str(p2l)}-{str(p2r)} | {cp2} H\C",
#                (10, 65), font, fontscale, color, thickness)
#     cv.putText(img, f"dH :{dh}", (w//2, 30), font, fontscale, color, thickness)
#     cv.putText(img, f"dC :{dc}", (w//2, 65), font, fontscale, color, thickness)
#     cv.putText(img, f"Angel : {angle}deg", (w//2, 95),
#                font, fontscale, color, thickness)
#     return img


# floor = drawPerspectiveFloor()[0]
# img1 = cv.imread('DataSetASamples/zc-45_3-001.png')
# img2 = cv.imread('DataSetASamples/zc-45_3-087.png')
# img1 = cv.resize(img1, (1080, 720))
# img2 = cv.resize(img2, (1080, 720))
# scene = cv.bitwise_or(img1, img2)
# scene = cv.bitwise_or(scene, floor)

# info = ([(1, 2), (2, 1)], [(3, 4), (4, 3)],
#         '(5, 6)', '(7, 8)', '3', '4', '63.12')
# scene = putInfo(scene, *info)

# cv.imshow('Mii_Ranna Scene', scene)
# cv.waitKey()
# cv.destroyAllWindows()


####################################################################
# # def pointArea(x, y, dim=(720, 1080)):
# #     h, w = dim
# #     if x < w//2:
# #         if y < h//2:
# #             return 'A'
# #         else:
# #             return 'B'
# #     else:
# #         if y < h//2:
# #             return 'D'
# #         else:
# #             return 'C'
# #     return False


# # def farFromCenter(x, y, dim=(720, 1080)):
# #     h, w = dim
# #     center_x, center_y = int(w/2), int(h/2)
# #     return (abs(x-center_x), abs(y-center_y))


# # def newPoint(dx, dy, area, scale, dim=(720, 1080)):
#     # h, w = dim
#     # center_x, center_y = int(w/2), int(h/2)
#     # dx *= int(scale/2)
#     # dy *= int(scale/2)
#     # if area == 'A':
#     #     new_x, new_y = center_x-dx, center_y-dy
#     # elif area == 'B':
#     #     new_x, new_y = center_x-dx, center_y+dy
#     # elif area == 'C':
#     #     new_x, new_y = center_x+dx, center_y+dy
#     # else:
#     #     new_x, new_y = center_x+dx, center_y-dy
#     # return new_x, new_y
# #########################################""""
# the old method
# x += int((x+(w2/w))/2)
# y += int((x+(h2/h))/2)
# point_area = pointArea(x, y, (h,w))
# dx, dy = farFromCenter(x, y, reversed((350*3, 250*3)))
# new_x, new_y = newPoint(dx, dy, point_area, 3, reversed((350*3, 250*3)))
# print(f'point_area: {x, y} ==> {point_area}')
# print(f'dx, dy ==> { dx, dy}')
# print(f'new_x, new_y ==> {new_x, new_y}')
# #########################################""""
def newCoordinate(oldDim, newDim, oldCoord):
    oldY, oldX = oldDim
    newY, newX = newDim
    x, y = oldCoord

    Rx = newX/oldX
    Ry = newY/oldY
    new_x, new_y = (round(Rx * x), round(Ry * y))
    return new_x, new_y


# Locating a pixel in resized image:
oldY, oldX = h, w = 250, 350
blank = np.zeros((h, w, 3), np.uint8)

pixel = x, y = (randint(10, 330), randint(10, 240))
old_center = (int(w/2), int(h/2))
cv.circle(blank, old_center, 2, (255, 0, 255), -1)
cv.circle(blank, pixel, 2, (0, 255, 0), -1)
cv.line(blank, old_center, pixel, (255, 0, 0), 1)

resized_pic = cv.resize(blank, (1056, 720))
newY, newX = h2, w2 = resized_pic.shape[:2]


Rx = newX/oldX
Ry = newY/oldY  # on the y-axis.
# , and by a ratio
# Therefore, your new coordinates for point (x,y) are
new_x, new_y = (round(Rx * x), round(Ry * y))
new_x, new_y = newCoordinate((x, y), (oldY, oldX), (newY, newX))
# """"

cv.circle(resized_pic, (new_x, new_y), 3, (0, 0, 255), -1)
cv.line(resized_pic, (int(w2/2), int(h2/2)), (new_x, new_y), (0, 0, 255), 2)

cv.imshow('pixel in image', blank)
cv.imshow('pixel in resized image', resized_pic)
cv.waitKey()
cv.destroyAllWindows()
####################################################################
# fill and Give interest points
# fill, interest_points

# path = "M:/Documents/Projects/End Of Study/End of Study Project/scripts/DataSetASamples/"
# pic = "nhz-90_4-033.png"
# pictures = [
#     'zc-45_3-001.png',
#     'zc-45_3-087.png',
#     'zc-90_3-001.png',
#     'xch-45_4-026.png',
#     'zc-00_3-001.png',
#     'zc-00_3-044.png',
#     'zc-90_3-080.png',
#     'zl-00_2-019.png',
#     'nhz-90_4-033.png',
#     'rj-90_3-018.png',
#     'wl-45_1-050.png',
#     'wl-90_3-058.png'
# ]

# for pic in pictures:
#     img = cv.imread(path+pic)
#     img = fill(img)
#     interest_points(img)

# img1 = cv.imread(r'script\DataSetASamples\zc-45_3-001.png')
# img2 = cv.imread(r'script\DataSetASamples\zc-45_3-087.png')

# img1 = cv.imread(r'GaitDatasetB-silh\031\nm-05\144\031-nm-05-144-050.png')
# img2 = cv.imread(r'GaitDatasetB-silh\031\nm-05\144\031-nm-05-144-126.png')

# img1 = cv.imread(r'GaitDatasetB-silh\031\nm-05\144\031-nm-05-144-050.png')
# img2 = cv.imread(r'GaitDatasetB-silh\031\nm-05\144\031-nm-05-144-126.png')

# img1 = cv.imread(r'GaitDatasetA-silh\zyf\45_4\zyf-45_4-001.png')
# img2 = cv.imread(r'GaitDatasetA-silh\zyf\45_4\zyf-45_4-096.png')


# dim = (img1.shape)
# dim = (720, 1080, 3)
# img1 = cv.resize(img1, tuple(reversed(dim[:2])))
# img2 = cv.resize(img2, tuple(reversed(dim[:2])))

# floor = drawPerspectiveFloor(dim)
# print(*floor[1].items(), sep='\n')
# print('><'*20)
# print(*floor[2].items(), sep='\n')


# scene = cv.bitwise_or(floor[0], img1)
# scene = cv.bitwise_or(scene, img2)
# # cv.imwrite('rendred scene.png', scene)

# cv.imshow('floor', scene)
# cv.waitKey()
# cv.destroyAllWindows()

# direc = getcwd()
# chdir('DataSetASamples')
# print(getcwd())
# chdir(direc)

#######################################################
