
# def img_to_white(img):
#     # Read image and convert it to grayscale.
#     # img = cv.imread(img)
#     # white = cv.imread('white.jfif')
#     white = np.zeros(img.shape, np.uint8)
#     gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#     blur = cv.GaussianBlur(gray, (5, 5), 0)
#     # cv.imshow('blur',blur)
#     # Search for edges in the image with cv.Canny().
#     edges = cv.Canny(blur, 150, 200)
#     # edges = cv.resize(edges, (300, 200))
#     # cv.imshow('canny image', edges)

#     # Search for contours in the edged image with cv.findContour().
#     contours = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
#     contours = contours[0] if len(contours) == 2 else contours[1]
#     # Filter out contours that are not in your interest by applying size criterion.
#     for cnt in contours:
#         size = cv.contourArea(cnt)
#         if size > 50:
#             cv.drawContours(white, [cnt], -1, (0, 0, 0), 3)

#     return white


# # steps one and two, condition one (function included for clarity)
# def pixel_is_black(arr, x, y):
#     if arr[x, y] == 1:
#         return True
#     return False


# # steps one and two, condition two
# def pixel_has_2_to_6_black_neighbors(arr, x, y):
#     # pixel values can only be 0 or 1, so simply check if sum of
#     # neighbors is between 2 and 6
#     if (2 <= arr[x, y - 1] + arr[x + 1, y - 1] + arr[x + 1, y] + arr[x + 1, y + 1] +
#             arr[x, y + 1] + arr[x - 1, y + 1] + arr[x - 1, y] + arr[x - 1, y - 1] <= 6):
#         return True
#     return False


# # steps one and two, condition three
# def pixel_has_1_white_to_black_neighbor_transition(arr, x, y):
#     # neighbors is a list of neighbor pixel values; neighbor P2 appears
#     # twice since we will cycle around P1.
#     neighbors = [arr[x, y - 1], arr[x + 1, y - 1], arr[x + 1, y], arr[x + 1, y + 1],
#                  arr[x, y + 1], arr[x, y + 1], arr[x - 1, y], arr[x - 1, y - 1],
#                  arr[x, y - 1]]
#     # zip returns iterator of tuples composed of a neighbor and next neighbor
#     # we then check if the neighbor and next neighbor is a 0 -> 1 transition
#     # finally, we sum the transitions and return True if there is only one
#     transitions = sum((a, b) == (0, 1)
#                       for a, b in zip(neighbors, neighbors[1:]))
#     if transitions == 1:
#         return True
#     return False


# # step one condition four
# def at_least_one_of_P2_P4_P6_is_white(arr, x, y):
#     # if at least one of P2, P4, or P6 is 0 (white), logic statement will
#     # evaluate to false.
#     if (arr[x, y - 1] and arr[x + 1, y] and arr[x, y + 1]) == False:
#         return True
#     return False


# # step one condition five
# def at_least_one_of_P4_P6_P8_is_white(arr, x, y):
#     # if at least one of P4, P6, or P8 is 0 (white), logic statement will
#     # evaluate to false.
#     if (arr[x + 1, y] and arr[x, y + 1] and arr[x - 1, y]) == False:
#         return True
#     return False


# # step two condition four
# def at_least_one_of_P2_P4_P8_is_white(arr, x, y):
#     # if at least one of P2, P4, or P8 is 0 (white), logic statement will
#     # evaluate to false.
#     if (arr[x, y - 1] and arr[x + 1, y] and arr[x - 1, y]) == False:
#         return True
#     return False


# # step two condition five
# def at_least_one_of_P2_P6_P8_is_white(arr, x, y):
#     # if at least one of P2, P6, or P8 is 0 (white), logic statement will
#     # evaluate to false.
#     if (arr[x, y - 1] and arr[x, y + 1] and arr[x - 1, y]) == False:
#         return True
#     return False


# def line_equation(pixel_line_one, pixel_line_two, pixel_to_verify):
#     m = (pixel_line_two[0] - pixel_line_one[0]) / \
#         (pixel_line_two[1] - pixel_line_one[1])
#     return(m * pixel_to_verify[1]) - (m * pixel_line_one[1]) + (pixel_line_one[0])


# def interest_points(img_path):
#     # img = cv.imread('casia.png',0)  # 0 = grayscale
#     # img_path = 'casia.png'
#     # casia = cv.imread(img_path)
#     # cv.imshow('casia', casia)
#     img = casia = img_path
#     # cv.imshow('ka7el2', casia)
#     # img = img_to_white(img_path)
#     ##########################################################
#     white = np.zeros(img.shape, np.uint8)
#     gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#     blur = cv.GaussianBlur(gray, (5, 5), 0)
#     edges = cv.Canny(blur, 150, 200)
#     contours = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
#     contours = contours[0] if len(contours) == 2 else contours[1]
#     for cnt in contours:
#         size = cv.contourArea(cnt)
#         if size > 50:
#             cv.drawContours(white, [cnt], -1, (0, 0, 0), 3)

#     img = white
#     ##########################################################
#     print(img.shape)
#     # cv.imshow('ka7el', img)
#     cv.waitKey()
#     img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#     # """
#     retval, orig_thresh = cv.threshold(img, 0, 255, cv.THRESH_BINARY)
#     bin_thresh = (orig_thresh == 0).astype(int)

#     # make a copy of the binary threshold array, upon which we will apply
#     # the thinning algorithm
#     thinned_thresh = bin_thresh.copy()

#     # if the thinned threshold reaches a steady state, we'll break out of the loop
#     while 1:
#         # make a copy of the thinned threshold array to check for changes
#         thresh_copy = thinned_thresh.copy()
#         # step one
#         pixels_meeting_criteria = []
#         # check all pixels except for border and corner pixels
#         # if a pixel meets all criteria, add it to pixels_meeting_criteria list
#         for i in range(1, thinned_thresh.shape[0] - 1):
#             for j in range(1, thinned_thresh.shape[1] - 1):
#                 if (pixel_is_black(thinned_thresh, i, j) and
#                         pixel_has_2_to_6_black_neighbors(thinned_thresh, i, j) and
#                         pixel_has_1_white_to_black_neighbor_transition(thinned_thresh, i, j) and
#                         at_least_one_of_P2_P4_P6_is_white(thinned_thresh, i, j) and
#                         at_least_one_of_P4_P6_P8_is_white(thinned_thresh, i, j)):
#                     pixels_meeting_criteria.append((i, j))

#         # change noted pixels in thinned threshold array to 0 (white)
#         for pixel in pixels_meeting_criteria:
#             thinned_thresh[pixel] = 0

#         # step two    #
#         pixels_meeting_criteria = []
#         # check all pixels except for border and corner pixels
#         # if a pixel meets all criteria, add it to pixels_meeting_criteria list
#         for i in range(1, thinned_thresh.shape[0] - 1):
#             for j in range(1, thinned_thresh.shape[1] - 1):
#                 if (pixel_is_black(thinned_thresh, i, j) and
#                         pixel_has_2_to_6_black_neighbors(thinned_thresh, i, j) and
#                         pixel_has_1_white_to_black_neighbor_transition(thinned_thresh, i, j) and
#                         at_least_one_of_P2_P4_P8_is_white(thinned_thresh, i, j) and
#                         at_least_one_of_P2_P6_P8_is_white(thinned_thresh, i, j)):
#                     pixels_meeting_criteria.append((i, j))

#         # change noted pixels in thinned threshold array to 0 (white)
#         for pixel in pixels_meeting_criteria:
#             thinned_thresh[pixel] = 0

#         # if the latest iteration didn't make any difference, exit loop
#         if np.all(thresh_copy == thinned_thresh) == True:
#             break

#     # convert all ones (black pixels) to zeroes, and all zeroes (white pixels) to ones
#     thresh = (thinned_thresh == 0).astype(np.uint8)
#     # convert ones to 255 (white)
#     thresh *= 255

#     # i = 0
#     contour = []
#     for i in range(1, thinned_thresh.shape[0] - 1):
#         for j in range(1, thinned_thresh.shape[1] - 1):
#             if (pixel_is_black(thinned_thresh, i, j)):
#                 contour.append((i, j))
#     body = contour[0] + contour[-1]
#     pied_i = (body[0] + body[2]) / 1.75
#     pied_j = (body[1] + body[3]) / 1.75
#     pieds = (pied_i, pied_j)
#     legs_contour = []
#     for (i, j) in contour:
#         if (i, j) >= (pied_i, pied_j):
#             legs_contour.append((i, j))

#     ####################################################
#     # pTime = time()
#     legs = thresh.copy()
#     len_contour = len(contour)
#     print("*"*25)
#     print("dim legs:", legs)
#     print("len(contour):", len(contour))
#     print("len(legs_contour)", len(legs_contour))
#     print("*"*25)
#     for index, pixel in enumerate(contour):
#         # clear()
#         # print("=+> {:.1f} %".format((index*100)/len_contour))
#         if not (pixel in legs_contour):
#             legs[pixel] = 255
#         # print("type(legs):", type(legs), legs)
#         # print("type(pixel):", type(pixel), pixel)
#         # print("type(thresh):", type(thresh), thresh)

#     # localTime = localtime(time()-pTime)
#     # print("\nTime : %dh:%dm:%ds" %
#     #       (localTime.tm_hour, localTime.tm_min, localTime.tm_sec))

#     squellette = legs.copy()
#     retval, origin_thresh = cv.threshold(
#         squellette, 0, 255, cv.THRESH_BINARY)
#     squ_thresh = (origin_thresh == 0).astype(int)
#     for pixel in legs_contour:
#         i = pixel[0]
#         j = pixel[1]

#     last_pixel = legs_contour[-1]
#     final_leg = []
#     for pixel in legs_contour:
#         if last_pixel[0] - 20 < pixel[0] < last_pixel[0] + 1:
#             final_leg.append(pixel)

#     for pixel in legs_contour:
#         if not (pixel in final_leg):
#             squellette[pixel] = 255

#     bottom_left = final_leg[0]
#     bottom_right = final_leg[0]
#     for pixel in final_leg:
#         if pixel[0] > bottom_left[0]:
#             if pixel[1] < bottom_left[1]:
#                 bottom_left = pixel
#     for pixel in final_leg:
#         if pixel[1] > bottom_right[1]:
#             if pixel[0] > bottom_right[0]:
#                 bottom_right = pixel

#     final_pixels = [bottom_left, bottom_right]
#     for pixel in final_leg:
#         if not (pixel in final_pixels):
#             squellette[pixel] = 255
#     retval, origin_thresh = cv.threshold(
#         squellette, 0, 255, cv.THRESH_BINARY)
#     squ_thresh = (origin_thresh == 0).astype(int)
#     coordinates = []
#     for i in range(1, squ_thresh.shape[0] - 1):
#         for j in range(1, squ_thresh.shape[1] - 1):
#             coordinates.append((i, j))
#     middle = legs_contour[-1]
#     for pixel in legs_contour:
#         if pixel[0] < middle[0]:
#             if bottom_left[1] + 5 < pixel[1] < bottom_right[1] - 5:
#                 middle = pixel

#     # middle[0]=min(bottom_right[0], bottom_left[0])-40
#     # middle[1]=(bottom_right[1]+bottom_left[1])/2
#     # for pixel in coordinates:
#     #     # print(int(line_equation(bottom_left,bottom_right,pixel)))
#     #     if min(bottom_right[0], middle[0]) < pixel[0] < max(bottom_right[0], middle[0]):
#     #         # squellette[pixel]=0
#     #         if pixel[0] == int(line_equation(middle, bottom_right, pixel)):
#     #             # bottom_left=pixel
#     #             # print('fond')
#     #             squellette[pixel] = 0
#     # for pixel in coordinates:
#     #     # print(int(line_equation(bottom_left,bottom_right,pixel)))
#     #     if min(bottom_left[0], middle[0]) < pixel[0] < max(bottom_left[0], middle[0]):
#     #         # squellette[pixel]=0
#     #         if pixel[0] == int(line_equation(middle, bottom_left, pixel)):
#     #             # bottom_left=pixel
#     #             # print('fond')
#     #             squellette[pixel] = 0
#     # print(coordinates)
#     x1 = bottom_left[1]
#     y1 = bottom_left[0]
#     x2 = bottom_right[1]
#     y2 = bottom_right[0]
#     x3 = middle[1]
#     y3 = middle[0]
#     x0 = contour[0][1]
#     y0 = contour[0][0]
#     cv.line(squellette, (x1, y1), (x3, y3), (0), thickness=1)
#     cv.line(squellette, (x2, y2), (x3, y3), (0), thickness=1)
#     cv.line(squellette, (x0, y0), (x3, y3), (0), thickness=1)
#     squellette = cv.bitwise_not(squellette)

#     # cv.imshow('legs', legs)
#     # cv.imshow('original image', orig_thresh)
#     # cv.imshow('thinned image', thresh)
#     # cv.imshow('squellette', squellette)
#     # cv.waitKey(0)
#     # cv.destroyAllWindows()
#     # print(final_pixels)
#     return [final_pixels, casia, orig_thresh, thresh, legs,  squellette]


######################## Silh Video DataSet A-B-C ########################
# # version 3:
# def drawPerspectiveFloor(dim=(720, 1080, 3)):
#     horizen_range = {}
#     blank = np.zeros(dim, np.uint8)
#     h, w = blank.shape[:2]
#     # h += 100
#     # Horizen:
#     last = 0
#     adt = 0
#     cv.line(blank, (0, h//2+last+adt), (w, h//2+last+adt), (0, 0, 255), 1)
#     bg_range = 0
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
#     # Right:
#     for index in range(1, 25):
#         try:
#             # 50*index
#             cv.line(blank,  (w//2 + 30*index, h//2),
#                     (w//2 + 30*index + 30*index, h), (0, 255, 0), 1)
#             # cv.line(blank,  (w//2 + 30*index, h//2),
#             #         (w//2 + 30*index - 30*index, 0), (255, 0, 0), 1)
#         except:
#             print("except")
#     # Left:
#     for index in range(1, 25):
#         try:
#             cv.line(blank,  (w//2 - 30*index, h//2),
#                     (w//2 - 30*index - 30*index, h), (0, 255, 0), 1)
#             # cv.line(blank,  (w//2 - 30*index, h//2),
#             #         (w//2 - 30*index + 30*index, 0), (0, 255, 0), 1)
#         except:
#             print("except")
#     return blank, horizen_range

# # Version 2:
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


# # Version 01:
# def drawPerspectiveFloor(dim=(720, 1080, 3)):
#     blank = np.zeros(dim, np.uint8)
#     h, w = blank.shape[:2]
#     # h += 100
#     # Midlle:
#     cv.line(blank, (w//2, h//2), (w//2, h), (0, 0, 255), 1)
#     # Right:
#     for index in range(1, 25):
#         try:
#             cv.line(blank,  (w//2 + 30*index, h//2),
#                     (w//2 + 30*index + 50*index, h), (0, 255, 0), 1)
#             # cv.line(blank,  (w//2 + 30*index, h//2),
#             #         (w//2 + 30*index - 50*index, 0), (255, 0, 0), 1)
#         except:
#             print("except")
#     # Left:
#     for index in range(1, 25):
#         try:
#             cv.line(blank,  (w//2 - 30*index, h//2),
#                     (w//2 - 30*index - 50*index, h), (0, 255, 0), 1)
#             # cv.line(blank,  (w//2 - 30*index, h//2),
#             #         (w//2 - 30*index + 50*index, 0), (0, 255, 0), 1)
#         except:
#             print("except")
#     # Horizen:
#     last = 0
#     adt = 0
#     cv.line(blank, (0, h//2+last+adt), (w, h//2+last+adt), (0, 0, 255), 1)
#     for index in range(0, 15):
#         last += 5
#         cv.line(blank, (0, h//2+last+adt), (w, h//2+last+adt), (0, 255, 0), 1)
#         last = last+adt
#         adt += 3
#     return blank


# # Random Version
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
#             # cv.line(blank,  (w//2 + fbw*index, h//2),
#             #         (w//2 + fbw*index - 50*index, 0), (255, 0, 0), 1)
#         except:
#             print("except")
#     # Left:
#     for index in range(1, 25):
#         try:
#             cv.line(blank,  (w//2 - fbw*index, h//2),
#                     (w//2 - fbw*index - lbw*index, h), (0, 255, 0), 1)
#             # cv.line(blank,  (w//2 - 30*index, h//2),
#             #         (w//2 - 30*index + 50*index, 0), (0, 255, 0), 1)
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


# # # version 4:
# def drawPerspectiveFloor(dim=(720, 1080, 3)):
#     blank = np.zeros(dim, np.uint8)
#     h, w = dim[:2]
#     center = b_point = [72, int(w//2)]
#     ribs = dim[0]//2 - center[0]
#     previous_angle = 0
#     colum_angle_range = {}
#     horizen_range = {}
#     fbw = dim[1]//18
#     lbw = dim[1]//14
#     # fbw = 60
#     # lbw = 75
#     # h += 100
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

#     # Midlle:
#     cv.line(blank, (w//2, h//2), (w//2, h), (0, 0, 255), 1)
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
#     cv.line(blank, (0, h*3//4), (w-1, h*3//4), (0, 0, 255), 1)
#     return blank, horizen_range, colum_angle_range




# def newCoordinate(oldCoord, oldDim, newDim):
#     original_width, original_height = oldDim
#     resized_width, resized_height = newDim
#     # original_height = 2592
#     # resized_height = 300;
#     width_ratio = int(original_width/resized_width)
#     height_ratio = int(original_height/resized_height)
#     original_x1 = round(x1 * width_ratio)
#     original_y1 = round(y1 * height_ratio)
#     original_x2 = round(x2 * width_ratio)
#     original_y2 = round(y2 * height_ratio)


# def newCoordinate(point, oldDim, newDim):
#     # To be removed
#     # x, y = tuple(reversed(point))
#     x, y = point
#     oldY, oldX = oldDim
#     newY, newX = newDim
#     Rx = int(newX/oldX)
#     Ry = int(newY/oldY)
#     new_x, new_y = (round(Rx * x), round(Ry * y))
#     return new_x, new_y



