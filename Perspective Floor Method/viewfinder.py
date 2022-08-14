import cv2 as cv
import numpy as np

"""function that draw a small viewfinder in the given image.
    """


def viewfinder(img, coord):
    """draw a small viewfinder in the given image.

    Args:
        img (numpy.ndarray): numpy array(image in our case).
        coord (tuple): the center of the point coordinate.
    """
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


if __name__ == '__main__':
    blank = np.zeros((200, 300, 3), np.uint8)
    viewfinder(blank, (50, 50))
    viewfinder(blank, (50, 100))
    viewfinder(blank, (100, 100))
    cv.imshow('viewfinder Test', blank)
    cv.waitKey()
    cv.destroyAllWindows()
