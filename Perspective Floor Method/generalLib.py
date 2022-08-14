from time import time, sleep, localtime
from os import name, system
from random import choice
from os import listdir
from os.path import isfile
import numpy as np
import cv2 as cv


# dataset link: http://www.cbsr.ia.ac.cn/users/szheng/?page_id=71
"""
    this library contain general function for manipulating paths and
    returning general informations about the dataset images.
    """

# we replaceed this with the dictionary below
# if you change this again you need to
# change it in B_dataset_details function below.
# A_dataset_walker_status = None

# B_dataset_walker_status = {
#     'nm': 'Normal',
#     'cl': 'In Coat',
#     'bg': 'In Bag',
# }

# C_dataset_walker_status = {
#     'fn': "normal",
#     'fq': "fast walk",
#     'fs': "slow walk",
#     'fb': "with a bag"
# }


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


dataset_angles = {
    'A': ['00', '45', '90'],
    'B': ['000', '018', '036', '054', '072',
          '090', '108', '126', '144', '162', '180'],
    'C': None
}


dataset_directories = {
    'A': "GaitDatasetA-silh",
    'B': "GaitDatasetB-silh",
    'C': "GaitDatasetC-silh"
}


fps_lat_color = (0, 255, 0)
default_font = cv.FONT_HERSHEY_PLAIN
default_fontscale = 3
default_thickness = 2

# ######################################################


def doNothing(nothing):
    pass


# define clear screen function
def clear():
    """ function that clear screen(terminal).
    """
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def print_A_dataset_details(direc='', pic_name='', n_frmaes='', print_res=False):
    inf = pic_name[:-4].split("-")
    if print_res:
        print("Path is >>{:^35}<<".format(direc))
        print("       >> {} Frame <<".format(n_frmaes))
        print(">>{:>15} : {:>03}".format('Subject Id', inf[0]))
        print(">>{:>15} : {:>03}".format('Status number', inf[2]))
        print(">>{:>15} : {:<8}".format(
            'Walking status', dataset_walker_status['B'][inf[1]]))
        print(">>{:>15} : {:>03} deg".format('Walking Angel', inf[3]))


def print_B_dataset_details(direc='', pic_name='', n_frmaes='', print_res=False):
    inf = pic_name[:-4].split("-")
    if print_res:
        print("Path is >>{:^35}<<".format(direc))
        print("       >> {} Frame <<".format(n_frmaes))
        print(">>{:>15} : {:>03}".format('Subject Id', inf[0]))
        print(">>{:>15} : {:>03}".format('Status number', inf[2]))
        print(">>{:>15} : {:<8}".format(
            'Walking status', dataset_walker_status['B'][inf[1]]))
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


def join_path(*paths):
    return "/".join(paths)


def pic_direc(path):
    """ function that returns the path of a picture directory.

    Args:
        path (str): Absolute/relative path of the picture.

    Returns:
        str: path of a picture directory.
    """
    direc = path.split("/")
    return "/".join(direc[:-1])


def pic_name(path):
    """ function that returns the name of a picture.

    Args:
        path (str): Absolute/relative path of the picture.

    Returns:
        str: name of a picture.
    """
    direc = path.split("/")
    return direc[-1]


def random_path(path, history=[], max_counter=50):
    """
    Returns (pictures list, directory path) from a random pictures(samples) directory path.

    This function gives you a list of images from a random folder path from a main path(or dataset)
    along with the path of the images,
    which the path of images isn't in the history list (if any is given).

    Parameters
    ----------
    path : string
        dataset("GaitDatasetA-silh" for exp) or dataset char ("A" for exp).

    history : list
        default = None, 
        history of visited paths.

    max_counter : int
    default = 50

    Returns
    -------
    string
        random images list(from a random path).
    string
        images folder path.
    """
    if path in dataset_directories.keys():
        path = dataset_directories[path.upper()]
    counter = 0
    while counter < max_counter:
        counter += 1
        directory = path
        while not isfile(directory):
            directory = join_path(directory, choice(listdir(directory)))
        directory = pic_direc(directory)
        if directory in history:
            continue
    history.append(directory)  # append the direc to the history
    pictures = listdir(directory)
    if counter > max_counter:
        return None, directory
    return pictures, directory


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


def walk_statu_filter(wsl, ws):
    # wsl: walking status list
    # ws: walking status
    wsl2 = []
    for status in wsl:
        if ws in status:
            wsl2.append(status)
    return wsl2


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


def put_fps(img, fps, late, put_fps=True, put_latency=False):
    if put_latency:
        late = str(late).split(".")[-1][:3]
        cv.putText(img, 'Latency: {:3} ms'.format(
            late), (10, 40), default_font, default_fontscale, fps_lat_color, default_thickness)
    if put_fps:
        cv.putText(img, 'FPS: {:0.1f}'.format(fps), (10, 80), default_font,
                   default_fontscale, fps_lat_color, default_thickness)
    return img


def prepare_scene(pic, floor, direc, fps, late):
    img = cv.imread(join_path(direc, pic))
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


def new_coordinate(old_coord, old_dim, new_dim):
    """ return a new_coordinates from an old image dimension and coordinates.
    when resizing images, sometimes we need to locate some points from the old image
    in the new image, this function does the job.

    Args:
        old_coord (tuple): the coordinates of the point we're using in the old image.
        old_dim (tuple): the dimension of the old image.
        new_dim (tuple): the dimension of the new image.

    Returns:
        tuple: the coordinates of the point we're using in the new image.
    """
    # [:2]: just to be sure that its only width and height.
    old_x, old_y = old_dim[:2]
    new_x, new_y = new_dim[:2]
    x, y = old_coord

    Rx = int(new_x/old_x)
    Ry = int(new_y/old_y)
    # Rx = int(old_x/new_x)
    # Ry = int(old_y/new_y)
    new_x, new_y = (round(Rx * x), round(Ry * y))
    return new_x, new_y
