import cv2 as cv
import generalLib as glib
import perspectiveFloorLib as pflib



##############################################################################################
# here we are going to take two pictures one with good point and another not
# pic_path_1 = r'M:\Documents\Projects\End Of Study\End of Study Project\scripts\GaitDatasetA-silh\fyc\00_3\fyc-00_3-001.png'
# pic_path_2 = r'M:\Documents\Projects\End Of Study\End of Study Project\scripts\GaitDatasetA-silh\fyc\00_3\fyc-00_3-069.png'
pic_path_1 = r'GaitDatasetA-silh\fyc\45_3\fyc-45_3-001.png'
pic_path_2 = r'GaitDatasetA-silh\fyc\45_3\fyc-45_3-113.png'
img1 = cv.imread(pic_path_1)
img2 = cv.imread(pic_path_2)

points1 = pflib.interest_points(img1)
points2 = pflib.interest_points(img2)
# showCopy(img1, poipflibnts1, img2, points2)

oldDim = img1.shape[:2]
newDim = (720, 1056)

img1 = cv.resize(img1, tuple(reversed(newDim)))
img2 = cv.resize(img2, tuple(reversed(newDim)))

# newCoordinate(oldCoord, oldDim, newDim)
new_point1_1 = pflib.newCoordinate(points1[0], oldDim, newDim)
new_point1_2 = pflib.newCoordinate(points1[1], oldDim, newDim)
new_point2_1 = pflib.newCoordinate(points2[0], oldDim, newDim)
new_point2_2 = pflib.newCoordinate(points2[1], oldDim, newDim)

cv.circle(img1, tuple(reversed(new_point1_1)), 4, (255, 0, 255), -1)
cv.circle(img1, tuple(reversed(new_point1_2)), 4, (255, 0, 255), -1)
cv.circle(img2, tuple(reversed(new_point2_1)), 4, (255, 0, 255), -1)
cv.circle(img2, tuple(reversed(new_point2_1)), 4, (255, 0, 255), -1)

floor = pflib.draw_perspective_floor((*newDim, 3))[0]
scene = cv.bitwise_or(img1, img2)
print(floor.shape)
print(scene.shape)
scene = cv.bitwise_or(scene, floor)

cv.imshow('Keep Going 1', scene)
scene = cv.resize(scene, (1100,720))
cv.imshow('Keep Going', scene)
cv.waitKey()
cv.destroyAllWindows()

##############################################################################################
# history = []
# # Test:
# main_direc = "M:/Documents/Projects/End Of Study/End of Study Project/scripts/script/GaitDatasetB-silh"
# while True:
#     direc = main_direc
#     while not isfile(direc):
#         direc = "/".join((direc, choice(listdir(direc))))
#         # direc = test(direc, choice(listdir(direc)))
#     pic_direc = picDirec(direc)
#     pictures = listdir(pic_direc)
#     if pic_direc in history:
#         direc = main_direc
#         continue

#     history.append(pic_direc)
#     for index in range(0, len(pictures), 10):
#         interest_points(pic_direc+"/"+pictures[index])
#         choice = input(">> ")
#         print(choice)
#         if choice == 'q':
#             break


# print(history)