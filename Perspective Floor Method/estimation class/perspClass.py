import cv2 as cv
import numpy as np
from perspLib import scoop
from math import sqrt, acos, tan, atan, degrees


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    # def __eq__(self, other):
    #     return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.__x > other.getX() and self.__y > other.getY()

    def __str__(self):
        return f"({self.x}, {self.y})"

    def isLower(self, other):
        if self.__y > other.getY():
            return self
        return other

    @classmethod
    def zero(cls):
        return cls(0, 0)


class PerspectiveFloor:

    def __init__(self, dim):
        width, height, depth = dim
        self.dim = dim
        self.v_point = (int(width//2), 0)  # 72
        # First/Last block measure
        self.fbw = self.dim[0]//18
        self.lbw = self.dim[0]//14
        # horizons and columns dict + ranges and angles range
        self.colum_angle_range = {}
        self.horizen_range = {}
        self.main_area = {
            'N': [(width//2, height//2),     (width-1,    height*3//4-1)],
            'E': [(width//2, height*3//4),   (width-1,    height-1)],
            'S': [(0,        height*3//4),   (width//2-1, height-1)],
            'W': [(0,        height//2),     (width//2-1, height*3//4-1)]
        }
        # black image to draw the
        self.blank = np.zero((height, width, depth), np.unit8)

        ribs = self.dim[0]//2 - self.v_point[0]
        previous_angle = 0
        last = 0
        adt = 0
        # horizon range beginning
        hrb_range = height//2
        # lines colors (BGR)
        vplcs = (255, 0, 0)  # vanishing lines
        line_color = (0, 255, 0)
        ml_color = (0, 0, 255)  # main lines color

        # main lines construction
        cv.line(self.blank, (0, height//2), (width, height//2),
                ml_color, 1)  # Main horizon line
        cv.line(self.blank, (width//2, height//2),
                (width//2, height), ml_color, 1)  # Main vertical line
        cv.line(self.blank, (0, height*3//4),
                (width-1, height*3//4), ml_color, 1)  # Zone's line

        # Horizons lines:
        while True:
            last += 6
            end_range = height//2+last+adt
            # saving the horizons ranges
            if end_range >= height:
                self.horizen_range[chr(65+index)] = [hrb_range, height-1]
                break
            self.horizen_range[chr(65+index)] = [hrb_range, end_range-1]

            cv.line(self.blank, (0, end_range),
                    (width, end_range), (0, 255, 0), 1)
            hrb_range = end_range
            last += adt
            adt += 2
        # Right/Left lines:
        while True:
            index = 1
            try:
                cv.line(self.blank, (width//2 + fbw*index, height//2),
                        (width//2 + fbw*index + lbw*index, height), line_color, 1)
                # cv.line(self.blank, (width//2 + fbw*index, height//2), (width//2 + fbw*index - lbw*index, 0), vplcs, 1)
                cv.line(self.blank, (width//2 - fbw*index, height//2),
                        (width//2 - fbw*index - lbw*index, height), line_color, 1)
                # cv.line(self.blank, (width//2 - fbw*index, height//2), (width//2 - fbw*index + lbw*index, 0), vplcs, 1)
                # calculating and saving the angles
                base = fbw*index
                tire = sqrt(ribs**2+base**2)
                curent_angle = degrees(acos(ribs/tire))
                self.colum_angle_range[str(index)] = [
                    previous_angle, curent_angle]
                previous_angle = curent_angle
            except:
                pass
            if width//2 + fbw*index >= width:
                break
            index += 1

        # deleting  extra variables
        del width
        del height
        del depth
        del dim
        del last
        del adt
        del vplcs
        del line_color
        del ml_color
        del ribs
        del base
        del tire
        del curent_angle
        del previous_angle
        del hrb_range
        del end_range
        del index
        del fbw
        del lbw

    def getFloor(self):
        return self.blank

    def getColumAngleRange(self):
        return self.colum_angle_range

    def getHorizonRange(self):
        return self.horizen_range

    def getWidth(self):
        return self.dim[0]

    def getHeight(self):
        return self.dim[1]
    
    def getMainAreas(self):
        return self.main_area


class Scene:

    def __init__(self, floor, img1, img2=False, points1=False, points2=False):
        if img2:
            self.scene = cv.bitwise_xor(img1, img2)
        self.scene = cv.bitwise_or(self.scene, floor)

        if points1:
            cv.circle(self.scene, points1[0], 6, (0, 255, 0), -1)
            cv.circle(self.scene, points1[1], 6, (0, 255, 0), -1)
            scoop
        if points2:
            cv.circle(self.scene, points2[0], 6, (0, 255, 0), -1)
            cv.circle(self.scene, points2[1], 6, (0, 255, 0), -1)
        if all[points1, points2]:
            lowest_point = points1.isLower(points2)
            scoop(lowest_point)
        else:
            if points1:
                scoop(points1)
            else:
                scoop(points2)
    
    def drawPoint(self, point):
        cv.circle(self.scene, point, 6, (0, 255, 0), -1)
    
    def drawScoop(self, point):
        scoop(point)
    
    def getScene(self):
        return self.scene

