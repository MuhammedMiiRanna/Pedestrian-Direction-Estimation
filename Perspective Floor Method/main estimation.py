import cv2 as cv
import viewfinder
import generalLib as glib
import perspectiveFloorLib as pflib


##############################################################################################
# here we are going to take two pictures one with good point and another not
# pic_path_1 = r'GaitDatasetA-silh\fyc\00_3\fyc-00_3-001.png'
# pic_path_2 = r'GaitDatasetA-silh\fyc\00_3\fyc-00_3-069.png'
# pic_path_1 = r'GaitDatasetA-silh\fyc\45_3\fyc-45_3-001.png'
# pic_path_2 = r'GaitDatasetA-silh\fyc\45_3\fyc-45_3-113.png'
pictures, directory = glib.random_path(
    glib.dataset_directories['A'], history=[], max_counter=50)
pic_path_1 = glib.join_path(directory, pictures[0])
pic_path_2 = glib.join_path(directory, pictures[-1])
del pictures
del directory

floor = pflib.draw_perspective_floor()[0]
new_dim, old_dim = pflib.get_new_old_dim()
##############################################################################################

img_1 = cv.imread(pic_path_1)
img_2 = cv.imread(pic_path_2)

# [0]: to return only (bottom_right, bottom_left)
points_1 = pflib.interest_points(img_1)[0]
points_2 = pflib.interest_points(img_2)[0]

img_1 = cv.resize(img_1, new_dim)
img_2 = cv.resize(img_2, new_dim)


new_point_1_1 = glib.new_coordinate(points_1[0], old_dim, new_dim)
new_point_1_2 = glib.new_coordinate(points_1[1], old_dim, new_dim)
new_point_2_1 = glib.new_coordinate(points_2[0], old_dim, new_dim)
new_point_2_2 = glib.new_coordinate(points_2[1], old_dim, new_dim)

viewfinder.viewfinder(img_1, tuple(reversed(new_point_1_1)))
viewfinder.viewfinder(img_1, tuple(reversed(new_point_1_2)))
viewfinder.viewfinder(img_2, tuple(reversed(new_point_2_1)))
viewfinder.viewfinder(img_2, tuple(reversed(new_point_2_1)))

scene = cv.bitwise_or(img_1, img_2)
scene = cv.bitwise_or(scene, floor)

cv.imshow('Keep Going 1', scene)
scene = cv.resize(scene, new_dim)
cv.imshow('Keep Going', scene)
cv.waitKey()
cv.destroyAllWindows()
