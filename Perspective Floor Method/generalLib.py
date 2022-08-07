from time import time, sleep, localtime
from os import name, system
import numpy as np
import cv2 as cv


# dataset link: http://www.cbsr.ia.ac.cn/users/szheng/?page_id=71


A_dataset_walker_status = None

B_dataset_walker_status = {
    'nm': 'Normal',
    'cl': 'In Coat',
    'bg': 'In Bag',
}

C_dataset_walker_status = {
    'fn': "normal",
    'fq': "fast walk",
    'fs': "slow walk",
    'fb': "with a bag"
}


dataset_walker_status = {
    'A': None,
    'B': {
        'nm': 'Normal',
        'cl': 'In Coat',
        'bg': 'In Bag',
    },
    'C': {
        'fn': "normal",
        'fq': "fast walk",
        'fs': "slow walk",
        'fb': "with a bag"
    }
}


A_angles = ["00", "45", "90"]
B_angles = ['000', '018', '036', '054', '072', '090', '108', '126', '144', '162', '180']
C_angles = None

dataset_directories = {
    'A': '',
    'B': "Pedestrian Direction Estimation\GaitDatasetB-silh",
    'C': ''
}


def doNothing(nothing):
    pass


# define clear screen function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def B_dataset_details(direc='', pic_name='', n_frmaes='', print_res=False):
    inf = pic_name[:-4].split("-")
    if print_res:
        print("Path is >>{:^35}<<".format(direc))
        print("       >> {} Frame <<".format(n_frmaes))
        print(">>{:>15} : {:>03}".format('Subject Id', inf[0]))
        print(">>{:>15} : {:>03}".format('Status number', inf[2]))
        print(">>{:>15} : {:<8}".format(
            'Walking status', B_dataset_walker_status[inf[1]]))
        print(">>{:>15} : {:>03} deg".format('Walking Angel', inf[3]))
    # def B_dataset_details(direc, inf, n_frmaes):
    #     print("Path is >>{:^35}<<".format(direc))
    #     print("       >> {} Frame <<".format(n_frmaes))
    #     print(">>{:>15} : {:>03}".format('Subject Id', inf[0]))
    #     print(">>{:>15} : {:>03}".format('Status number', inf[2]))
    #     print(">>{:>15} : {:<8}".format(
    #         'Walker status', B_dataset_walker_status[inf[1]]))
    #     print(">>{:>15} : {:>03} deg".format('Walking Angel', inf[3]))
    return inf


def path(*paths):
    return "/".join(paths)


def pic_direc(path):
    direc = path.split("/")
    return "/".join(direc[:-1])


def pic_name(path):
    direc = path.split("/")
    return direc[-1]


def put_info(img, point, cp, delta, angle, version='1'):
    # def put_info(img, p1, p2, cp1, cp2, dh, dc, angle_est, angle, version='1'):
    h, w = img.shape[:2]
    color = (255, 0, 255)
    font = cv.FONT_HERSHEY_PLAIN
    fontscale = 2
    thickness = 2

    (p1r, p1l), (p2r, p2l) = point
    p1l, p1r = str(p1l), str(p1r)
    p2l, p2r = str(p2l), str(p2r)

    cp1, cp2 = cp
    dh, dc = delta
    angle_est, angle = angle

    if version == '1':
        cv.putText(img, "{:<10}-{:<10} | {} H\C".format(p1l, p1r, cp1),
                   (10, 30), font, fontscale, color, thickness)
        cv.putText(img, "{:<10}-{:<10} | {} H\C".format(p2l, p2r, cp2),
                   (10, 65), font, fontscale, color, thickness)
        cv.putText(img, f"dH: {dh}", (10, 95), font,
                   fontscale, color, thickness)
        cv.putText(img, f"dC: {dc}", (10, 130),
                   font, fontscale, color, thickness)
        cv.putText(img, "     Angel : {}deg".format(angle), (10, 155),
                   font, fontscale, color, thickness)
        cv.putText(img, "Estimation : {:.2f}deg".format(angle_est), (10, 190),
                   font, fontscale, color, thickness)
    else:
        cv.putText(img, "Coord Point1: '{},{}' | Zone_1: {}".format(cp1[1][0], cp1[1][1], cp1[2]),
                   (10, 30), font, fontscale, color, thickness)
        cv.putText(img, "Coord Point2: '{},{}' | Zone_2: {}".format(cp2[1][0], cp2[1][1], cp2[2]),
                   (10, 65), font, fontscale, color, thickness)
        cv.putText(img, f"deltaHor: {dh} / deltaCol: {dc}", (10, 95),
                   font, fontscale, color, thickness)
        cv.putText(img, "         Angel : {}deg".format(angle), (10, 125),
                   font, fontscale, color, thickness)
        cv.putText(img, "    Estimation : {:.0f}deg".format(angle_est), (6, 150),
                   font, fontscale, color, thickness)
        # if not str(dc) == '0' or not str(dh) == '0':
        # if not int(angle) in [0,90,180,270] :
        #     cv.putText(img, "Walking Range : '{:.0f}' -> '{:.0f}'".format(angle_est-10, angle_est+10), (10, 175),
        #                font, fontscale, color, thickness)
        if angle == '000':
            cv.putText(img, "Walking Range : '{:.0f}' -> '{:.0f}'".format(360-10, angle_est+10), (10, 175),
                       font, fontscale, color, thickness)
        else:
            cv.putText(img, "Walking Range : '{:.0f}' -> '{:.0f}'".format(angle_est-10, angle_est+10), (10, 175),
                       font, fontscale, color, thickness)

    return img


def time_toked(seconds):
    day = seconds // 86400
    seconds %= 86400
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    toked = ''
    if day:
        toked += f'{int(day)}day - '
    if hours:
        toked += f'{int(hours)}h - '
    if hours:
        toked += f'{int(minutes)}m - '
    toked += '{:.2f}s'.format(seconds)
    return toked


def view_finder(img, coord):
    y, x = coord
    img = cv.circle(img, coord, 10, (0, 0, 255), thickness=0)
    img = cv.circle(img, coord, 15, (0, 0, 255), thickness=1)
    cv.line(img, (y, x+3), (y, x+7), (255, 255, 0), thickness=1)
    cv.line(img, (y, x-3), (y, x-7), (255, 255, 0), thickness=1)
    cv.line(img, (y+3, x), (y+7, x), (255, 255, 0), thickness=1)
    cv.line(img, (y-3, x), (y-7, x), (255, 255, 0), thickness=1)
    # ####
    cv.line(img, (y, x+11), (y, x+18), (0, 0, 255), thickness=2)
    cv.line(img, (y, x-11), (y, x-18), (0, 0, 255), thickness=2)
    cv.line(img, (y+11, x), (y+18, x), (0, 0, 255), thickness=2)
    cv.line(img, (y-11, x), (y-18, x), (0, 0, 255), thickness=2)


def put_fps(img, fps, late, put_fps=True, put_latency=False, color=(0, 255, 0), font=cv.FONT_HERSHEY_PLAIN, fontscale=3, thickness=2):
    if put_latency:
        late = int(str(late).split(".")[-1][:4])
        cv.putText(img, 'Latency: {:4} ms'.format(
            late), (10, 40), font, fontscale, color, thickness)
    if put_fps:
        cv.putText(img, 'FPS: {:0.1f}'.format(
            fps), (10, 80), font, fontscale, color, thickness)
    return img


def prepare_scene(pic, floor, direc, fps, late):
    img = cv.imread(path(direc, pic))
    # img = pic
    img = cv.resize(img, tuple(reversed(floor.shape[:2])))
    scene = cv.bitwise_or(img, floor)
    scene = put_fps(scene, fps, late, put_latency=True)
    return scene


# ##############################################################
def fill(img, Gkernal=(5, 5)):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, Gkernal, 0)
    canny = cv.Canny(blur, 200, 150)
    kernel = np.ones((5, 5), np.uint8)
    dilation = cv.dilate(img, kernel, iterations=2)
    canny2 = cv.Canny(dilation, 200, 200)
    canny2 = cv.cvtColor(canny2, cv.COLOR_GRAY2BGR)
    return canny2


def resize_image(image, scale=0.3, dim=0):
    h, w = image.shape[:2]
    if dim and w > dim:
        dim = dim, int(dim*(h/w))
    elif not h < 600 and not w < 800:
        dim = int(w*scale), int(h*scale)
    else:
        dim = w, h
    return cv.resize(image, dim, interpolation=cv.INTER_LINEAR)


def new_coordinate(oldCoord, oldDim, newDim):
    oldX, oldY = oldDim[:2]
    newX, newY = newDim[:2]
    x, y = oldCoord

    # Rx = int(newX/oldX)
    # Ry = int(newY/oldY)
    Rx = int(oldX/newX)
    Ry = int(oldY/newY)
    new_x, new_y = (round(Rx * x), round(Ry * y))
    return new_x, new_y