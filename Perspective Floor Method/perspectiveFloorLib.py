from math import sqrt, acos, degrees
from time import time
import numpy as np
import cv2 as cv


default_image_shape = (240, 352, 3)
new_scene_shape = (736, 1080, 3)
h, w = new_scene_shape[:2]

main_area = {
    'N': [(w//2, h//2),     (w-1,    h*3//4-1)],
    'E': [(w//2, h*3//4),   (w-1,    h-1)],
    'S': [(0,    h*3//4),   (w//2-1, h-1)],
    'W': [(0,    h//2),     (w//2-1, h*3//4-1)]
}


def change_main_areas(shape):
    global main_area
    h, w = shape[:2]
    main_area = {
        'N': [(w//2, h//2),     (w-1,    h*3//4-1)],
        'E': [(w//2, h*3//4),   (w-1,    h-1)],
        'S': [(0,    h*3//4),   (w//2-1, h-1)],
        'W': [(0,    h//2),     (w//2-1, h*3//4-1)]
    }

# #################################################################


def get_new_old_dim():
    return (tuple(reversed(new_scene_shape[:2])),
            tuple(reversed(default_image_shape[:2])))

# #################################################################
# locate the posiiotn of a point (area/horizon/angle)
# Return Area, or False


def locate_area(coord):
    for area, ar_range in main_area.items():
        if ar_range[0][0] <= coord[0] <= ar_range[1][0]:
            if ar_range[0][1] <= coord[1] <= ar_range[1][1]:
                return area
    return False

# TODO: find a way to remove 'hrzns_rng' from the parameteres here:
# Return horizen, or False


def locate_horizen(coord, horizons_range):
    for hrz, rng in horizons_range.items():
        if coord[1] in range(rng[0], rng[1]+1):
            return hrz
    return False


# return the column belonged
def locate_angle(coord, shape, angles_range):
    center = [540, 72]
    h, w = shape[:2]
    ribs = coord[1] - center[1]
    base = abs(coord[0] - center[0])
    tire = sqrt(ribs**2+base**2)
    angle = degrees(acos(ribs/tire))
    for column, rng in angles_range.items():
        if rng[0] < angle <= rng[1]:
            if coord[0] >= w//2:
                return "{}{}".format("+", column)
            # elif coord[0] == w//2:
            #     return "{}".format(column)
            else:
                return "{}{}".format("-", column)


# #################################################################
#
def delta_horizen(horizen_1, horizen_2, horizons_range):
    horizens = [key for key in horizons_range.keys()]
    horizen_1 = horizens.index(horizen_1)
    horizen_2 = horizens.index(horizen_2)
    return abs(horizen_1-horizen_2)


def delta_column(column_1, column_2):
    column_1 = int(column_1)
    column_2 = int(column_2)
    column_1 += 1 if column_1 < 0 else 0
    column_2 += 1 if column_2 < 0 else 0
    return abs(column_1-column_2)


def delta(squar_1, squar_2, horizons_range):
    horizen_delta = delta_horizen(squar_1[0], squar_2[0], horizons_range)
    column_delta = delta_column(squar_1[1], squar_2[1])
    return (horizen_delta, column_delta)


def horizone_angle(area_1, area_2, delta_coord):
    # delta_horizen, delta_column
    if delta_coord[0] in [0, 1]:
        # delta_horizen(delta lines) ~= 0
        if area_1 in ['N', 'E'] and area_2 in ['W', 'S']:
            angle = 90
        else:
            angle = 270
    elif delta_coord[1] in [0, 1]:
        # delta_column ~= 0
        if area_1 in ['N', 'W'] and area_2 in ['E', 'S']:
            angle = 0
        else:
            angle = 180
    else:
        ribs = delta_coord[1]
        base = delta_coord[0]
        tire = sqrt(ribs**2+base**2)
        angle = degrees(acos(ribs/tire))
        # if area_1 == 'N' and area_2 == 'S':
        if area_1 in ['N', 'E'] and area_2 == 'S':
            angle = 90 - angle
        elif area_1 in ['N', 'E'] and area_2 == 'W':
            angle = 90 + angle
        elif area_1 in ['S', 'W'] and area_2 == 'N':
            angle = 270 - angle
        elif area_1 in ['S', 'W'] and area_2 == 'E':
            angle = 270 + angle
    return angle


# #################################################################
#

def draw_perspective_floor(dim=(736, 1080, 3)):
    blank = np.zeros(dim, np.uint8)
    h, w = dim[:2]
    center = b_point = [72, int(w//2)]
    ribs = dim[0]//2 - center[0]
    previous_angle = 0
    colum_angle_range = {}
    horizen_range = {}
    fbw = dim[1]//18
    lbw = dim[1]//14
    # fbw = 60
    # lbw = 75
    # h += 100
    # Horizen:
    last = 0
    adt = 0
    bg_range = h//2
    cv.line(blank, (0, h//2+last+adt), (w, h//2+last+adt), (0, 0, 255), 1)
    # 15
    for index in range(0, 17):
        last += 6
        end_range = h//2+last+adt
        if end_range >= h:
            horizen_range[chr(65+index)] = [bg_range, h-1]
            break
        else:
            horizen_range[chr(65+index)] = [bg_range, end_range-1]

        cv.line(blank, (0, end_range), (w, end_range), (0, 255, 0), 1)
        bg_range = end_range
        last += adt
        adt += 2

    # Midlle:
    cv.line(blank, (w//2, h//2), (w//2, h), (0, 0, 255), 1)
    # Right + Left:
    for index in range(1, 25):
        # fbw = 60 / lbw = 75
        try:
            # 50*index
            cv.line(blank,  (w//2 + fbw*index, h//2),
                    (w//2 + fbw*index + lbw*index, h), (0, 255, 0), 1)
            # cv.line(blank,  (w//2 + fbw*index, h//2),
            #         (w//2 + fbw*index - lbw*index, 0), (255, 0, 0), 1)
            cv.line(blank,  (w//2 - fbw*index, h//2),
                    (w//2 - fbw*index - lbw*index, h), (0, 255, 0), 1)
            # cv.line(blank,  (w//2 - fbw*index, h//2),
            #         (w//2 - fbw*index + lbw*index, 0), (0, 255, 0), 1)

            base = fbw*index
            # ribs = dim[0] - center[0]
            # base = fbw*index
            tire = sqrt(ribs**2+base**2)
            curent_angle = degrees(acos(ribs/tire))
            colum_angle_range[str(index)] = [previous_angle, curent_angle]
            previous_angle = curent_angle
        except:
            print("except")
        if w//2 + fbw*index >= w:
            break
    cv.line(blank, (0, h*3//4), (w-1, h*3//4), (0, 0, 255), 1)
    return blank, horizen_range, colum_angle_range


# TODO: decide if u want thos 2 func as one or nah
def drawPerspectiveFloorWithAnimations(dim=(736, 1080, 3)):
    blank = np.zeros(dim, np.uint8)
    # center = v_point = [72, int(w//2)]
    h, w = dim[:2]
    center = v_point = [int(w//2), 72]
    ribs = dim[0]//2 - center[0]
    previous_angle = 0
    colum_angle_range = {}
    horizen_range = {}
    fbw = dim[1]//18
    lbw = dim[1]//14
    # fbw = 60
    # lbw = 75
    # h += 100
    # Horizen:
    last = 0
    adt = 0
    bg_range = h//2
    vplcs = (255, 0, 0)
    line_color = (0, 255, 0)
    main_line_color = (0, 0, 255)
    # v_point_line_colors =
    # Midlle:
    # V
    cv.imshow('Sol', blank)
    cv.waitKey(500)
    # cv.line(blank, v_point, (int(w//2), h), vplcs, 1)
    cv.line(blank, (int(w//2), int(h//2)), (w//2, h), main_line_color, 1)
    cv.imshow('Sol', blank)
    cv.waitKey(500)
    # H
    cv.line(blank, (0, h//2+last+adt), (w, h//2+last+adt), main_line_color, 1)
    cv.imshow('Sol', blank)
    cv.waitKey(500)
    # Zone's line
    cv.line(blank, (0, h*3//4), (w-1, h*3//4), main_line_color, 1)
    cv.imshow('Sol', blank)
    cv.waitKey(500)

    # 15
    for index in range(0, 17):
        last += 6
        end_range = h//2+last+adt
        if end_range >= h:
            horizen_range[chr(65+index)] = [bg_range, h-1]
            break
        else:
            horizen_range[chr(65+index)] = [bg_range, end_range-1]

        cv.line(blank, (0, end_range), (w, end_range), line_color, 1)
        cv.imshow('Sol', blank)
        cv.waitKey(500)
        bg_range = end_range
        last += adt
        adt += 2

    # Right + Left:
    for index in range(1, 25):
        # fbw = 60 / lbw = 75
        try:
            # 50*index
            cv.line(blank,  (w//2 + fbw*index, h//2),
                    (w//2 + fbw*index + lbw*index, h), line_color, 1)
            # cv.line(blank,  (w//2 + fbw*index, h//2), v_point, vplcs, 1)
            cv.imshow('Sol', blank)
            cv.waitKey(200)

            cv.line(blank,  (w//2 - fbw*index, h//2),
                    (w//2 - fbw*index - lbw*index, h), line_color, 1)
            # cv.line(blank,  (w//2 - fbw*index, h//2), v_point, vplcs, 1)
            cv.imshow('Sol', blank)
            cv.waitKey(500)

            base = fbw*index
            # ribs = dim[0] - center[0]
            # base = fbw*index
            tire = sqrt(ribs**2+base**2)
            curent_angle = degrees(acos(ribs/tire))
            colum_angle_range[str(index)] = [previous_angle, curent_angle]
            previous_angle = curent_angle
        except:
            print("except")
        if w//2 + fbw*index >= w:
            break
    cv.waitKey(3000)
    cv.destroyAllWindows()
    return blank, horizen_range, colum_angle_range


def interest_points(img, reverse=False):
    # steps one and two, condition one (function included for clarity)
    def pixel_is_black(arr, x, y):
        if arr[x, y] == 1:
            return True
        return False

    # steps one and two, condition two

    def pixel_has_2_to_6_black_neighbors(arr, x, y):
        # pixel values can only be 0 or 1, so simply check if sum of
        # neighbors is between 2 and 6
        if (2 <= arr[x, y - 1] + arr[x + 1, y - 1] + arr[x + 1, y] + arr[x + 1, y + 1] +
                arr[x, y + 1] + arr[x - 1, y + 1] + arr[x - 1, y] + arr[x - 1, y - 1] <= 6):
            return True
        return False

    # steps one and two, condition three

    def pixel_has_1_white_to_black_neighbor_transition(arr, x, y):
        # neighbors is a list of neighbor pixel values; neighbor P2 appears
        # twice since we will cycle around P1.
        neighbors = [arr[x, y - 1], arr[x + 1, y - 1], arr[x + 1, y], arr[x + 1, y + 1],
                     arr[x, y + 1], arr[x, y + 1], arr[x -
                                                       1, y], arr[x - 1, y - 1],
                     arr[x, y - 1]]
        # zip returns iterator of tuples composed of a neighbor and next neighbor
        # we then check if the neighbor and next neighbor is a 0 -> 1 transition
        # finally, we sum the transitions and return True if there is only one
        transitions = sum((a, b) == (0, 1)
                          for a, b in zip(neighbors, neighbors[1:]))
        if transitions == 1:
            return True
        return False

    # step one condition four

    def at_least_one_of_P2_P4_P6_is_white(arr, x, y):
        # if at least one of P2, P4, or P6 is 0 (white), logic statement will
        # evaluate to false.
        if (arr[x, y - 1] and arr[x + 1, y] and arr[x, y + 1]) == False:
            return True
        return False

    # step one condition five

    def at_least_one_of_P4_P6_P8_is_white(arr, x, y):
        # if at least one of P4, P6, or P8 is 0 (white), logic statement will
        # evaluate to false.
        if (arr[x + 1, y] and arr[x, y + 1] and arr[x - 1, y]) == False:
            return True
        return False

    # step two condition four

    def at_least_one_of_P2_P4_P8_is_white(arr, x, y):
        # if at least one of P2, P4, or P8 is 0 (white), logic statement will
        # evaluate to false.
        if (arr[x, y - 1] and arr[x + 1, y] and arr[x - 1, y]) == False:
            return True
        return False

    # step two condition five

    def at_least_one_of_P2_P6_P8_is_white(arr, x, y):
        # if at least one of P2, P6, or P8 is 0 (white), logic statement will
        # evaluate to false.
        if (arr[x, y - 1] and arr[x, y + 1] and arr[x - 1, y]) == False:
            return True
        return False

    def line_equation(pixel_line_one, pixel_line_two, pixel_to_verify):
        m = (pixel_line_two[0] - pixel_line_one[0]) / \
            (pixel_line_two[1] - pixel_line_one[1])
        return (m * pixel_to_verify[1]) - (m * pixel_line_one[1]) + (pixel_line_one[0])
    ########################################################################
    pTime = time()
    # img = cv.imread('casia.png',0)  # 0 = grayscale
    # img_path = 'casia.png'
    # img = cv.imread(img_path)
    if len(img.shape) > 2:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.bitwise_not(img)

    # """
    retval, orig_thresh = cv.threshold(img, 0, 255, cv.THRESH_BINARY)
    bin_thresh = (orig_thresh == 0).astype(int)

    # make a copy of the binary threshold array, upon which we will apply
    # the thinning algorithm
    thinned_thresh = bin_thresh.copy()

    # if the thinned threshold reaches a steady state, we'll break out of the loop
    while 1:
        # make a copy of the thinned threshold array to check for changes
        thresh_copy = thinned_thresh.copy()
        # step one
        pixels_meeting_criteria = []
        # check all pixels except for border and corner pixels
        # if a pixel meets all criteria, add it to pixels_meeting_criteria list
        for i in range(1, thinned_thresh.shape[0] - 1):
            for j in range(1, thinned_thresh.shape[1] - 1):
                if (pixel_is_black(thinned_thresh, i, j) and
                        pixel_has_2_to_6_black_neighbors(thinned_thresh, i, j) and
                        pixel_has_1_white_to_black_neighbor_transition(thinned_thresh, i, j) and
                        at_least_one_of_P2_P4_P6_is_white(thinned_thresh, i, j) and
                        at_least_one_of_P4_P6_P8_is_white(thinned_thresh, i, j)):
                    pixels_meeting_criteria.append((i, j))

        # change noted pixels in thinned threshold array to 0 (white)
        for pixel in pixels_meeting_criteria:
            thinned_thresh[pixel] = 0

        # step two    #
        pixels_meeting_criteria = []
        # check all pixels except for border and corner pixels
        # if a pixel meets all criteria, add it to pixels_meeting_criteria list
        for i in range(1, thinned_thresh.shape[0] - 1):
            for j in range(1, thinned_thresh.shape[1] - 1):
                if (pixel_is_black(thinned_thresh, i, j) and
                        pixel_has_2_to_6_black_neighbors(thinned_thresh, i, j) and
                        pixel_has_1_white_to_black_neighbor_transition(thinned_thresh, i, j) and
                        at_least_one_of_P2_P4_P8_is_white(thinned_thresh, i, j) and
                        at_least_one_of_P2_P6_P8_is_white(thinned_thresh, i, j)):
                    pixels_meeting_criteria.append((i, j))

        # change noted pixels in thinned threshold array to 0 (white)
        for pixel in pixels_meeting_criteria:
            thinned_thresh[pixel] = 0

        # if the latest iteration didn't make any difference, exit loop
        if np.all(thresh_copy == thinned_thresh) == True:
            break

    # convert all ones (black pixels) to zeroes, and all zeroes (white pixels) to ones
    thresh = (thinned_thresh == 0).astype(np.uint8)
    # convert ones to 255 (white)
    thresh *= 255

    # i = 0
    contour = []
    for i in range(1, thinned_thresh.shape[0] - 1):
        for j in range(1, thinned_thresh.shape[1] - 1):
            if pixel_is_black(thinned_thresh, i, j):
                contour.append((i, j))
    body = contour[0] + contour[-1]
    jambe_i = (body[0] + body[2]) / 1.75
    jambe_j = (body[1] + body[3]) / 1.75
    legs_contour = []
    for (i, j) in contour:
        if (i, j) >= (jambe_i, jambe_j):
            legs_contour.append((i, j))

    legs = thresh.copy()
    for pixel in contour:
        if not (pixel in legs_contour):
            legs[pixel] = 255
    legs2 = legs.copy()
    bottom_right = legs_contour[0]
    bottom_left = legs_contour[0]
    for pixel in reversed(legs_contour):
        if pixel[1] > bottom_right[1]:
            if pixel[0] > bottom_right[0]:
                bottom_right = pixel
    for pixel in reversed(legs_contour):
        if pixel[0] > bottom_right[0] and bottom_right[1] - 4 < pixel[1] < bottom_right[1] + 4:
            bottom_right = pixel
    for pixel in reversed(legs_contour):
        if pixel[1] < bottom_right[1]:
            if pixel[0] > bottom_right[0]:
                bottom_left = pixel
    for pixel in reversed(legs_contour):
        if pixel[0] > bottom_left[0] and bottom_left[1] - 4 < pixel[1] < bottom_left[1] + 4:
            bottom_left = pixel

    # print(bottom_right)
    cv.line(legs2, (1, 1), (bottom_right[1], bottom_right[0]), 0, thickness=1)
    cv.line(legs2, (1, 1), (bottom_left[1], bottom_left[0]), 0, thickness=1)
    legs2 = cv.bitwise_not(legs2)

    orig_thresh = cv.bitwise_not(orig_thresh)
    orig_thresh = cv.cvtColor(orig_thresh, cv.COLOR_GRAY2BGR)
    # cv.circle(orig_thresh, tuple(reversed(bottom_right)), 3, (255, 0, 0), -1)
    # cv.circle(orig_thresh, tuple(reversed(bottom_left)), 3, (255, 0, 0), -1)
    # print("Time==> {}".format(timeToked(time()-pTime)))
    # print([bottom_right, bottom_left])

    # cv.imshow('legs', legs)
    # cv.imshow('legs2', legs2)
    # cv.imshow('original image', orig_thresh)
    # cv.imshow('thinned image', thresh)
    # cv.waitKey(0)
    # cv.destroyAllWindows()
    if reverse:
        bottom_right = tuple(reversed(bottom_right))
        bottom_left = tuple(reversed(bottom_left))
        # bottom_right = bottom_right.reverse()
        # bottom_left = bottom_left.reverse()
    return ((bottom_right, bottom_left), orig_thresh, thresh, legs, legs2)
