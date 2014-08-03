#!/usr/bin/env python
# encoding: utf-8
"""
It will show all image in my computer.
"""
import cv2 as cv
import os
def justShow(windname, imgfile):
    """
    Just show the input image in the window
    """
    img = cv.imread(imgfile, 0)
    cv.imshow(windname, img)
    cv.waitKey(1000)


def findKindofFile(dirpath, kind):
    """
    It will get a list under the 'dirpath' which is 'kind' style
    """
    result = []
    list_dir = os.walk(dirpath)
    for root, dirs, files in list_dir:
        for file in files:
            if kind in file:
                result.append(os.path.join(root, file))
    return result
if __name__ == '__main__' :
    allfiles = findKindofFile('/home/roubo/Pictures', 'png')
    cv.namedWindow('imageshow', cv.WINDOW_NORMAL)
    for imgfile in allfiles:
        print(imgfile)
        justShow('imageshow', imgfile)
    cv.destroyAllWindows()
